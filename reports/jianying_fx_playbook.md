# 特效 / 转场 / 贴纸 / 文字 / 音频效果 —— 逆向结论与接管方案

先回答：**五类全能逆向，而且比 UI 好拿——因为这些资产本来就是「数据 + 着色器源码 + JS 模板」，不是编译后的控件代码。**

| 类别 | 本地形态 | 拿到的程度 | 复用判定 |
| --- | --- | --- | --- |
| 转场 / 混合模式 | 10 个包，每包 `config.json` + `content.json` + `material` + `prefab` + `xshader` + **GLSL 与 Metal 双份 frag/vert** | 着色器 **源码级**，参数名可读 | **可直接移植**（着色器改写进我们的节点） |
| 特效（色度键 / 抠像 / 调色） | 19 个包，**124 个着色器文件**（gles 88 / metal 36） | 同上，工程量大但路径清楚 | **可直接移植** |
| 贴纸模板 | JS 模板包（`template.js` 622KB，带 sourcemap 声明） | **引擎桥 API 全暴露** | 可复用运行时设计 |
| 文字模板 | JS 模板包（`aigc_text_template/js/main.js` 267KB + `template.js`） | **`text_params` 字段表完整** | 可直接照字段建我们自己的文字模型 |
| 音频效果 | `audioeffect.dll` + 草稿 `audio_effects` 材质类 | **124 个效果名**，DSP 黑盒 | 名字照抄，DSP 用 JUCE + 开源替 |

规模账（`jianying/fx_packs.py` 实跑）：

```
五个类别共 37 个资产条目
混合/转场      10 包  着色器 gles 20 / metal 20 / xshader 10
色度键与抠像    12 包  着色器 gles 72 / metal 36 / xshader 32
调色控件资源     7 包  着色器 gles 16 / xshader 14
贴纸 / 文字      3 包  无着色器，纯 JS 模板
音频效果名      124 个
```

**GLSL 与 Metal 双份源码**是关键：它意味着这些效果在 PC（Windows/Linux ANGLE）与 macOS（Metal）两条后端上都有效果的**完整实现**，我们照着 GLSL 那一份改写 WGSL 就能直接跑在自家渲染管线上。

---

## 一、特效包格式：完整解剖

一个包（以 `Resources\MixMode\042aa15b71b1e17bca0bd928eec6fba7` 为例）：

```
042aa15b…\                              ← 包 ID = 32 位十六进制
├─ config.json        0.2KB             效果元信息 + 链接类型
├─ content.json       0.1KB             filemap：prefab 指向
├─ anim.prefab        0.6KB             实体树（二进制）
├─ blend.material     0.7KB             材质与属性表（二进制）
├─ xshader\blend.xshader  3.1KB         着色器入口
└─ Library\ShaderData\<hash>\
   ├─ shaderGLES\<hash>.frag  2.5KB      GLSL 片元
   ├─ shaderGLES\<hash>.vert  2.3KB      GLSL 顶点
   ├─ shaderMetal\<hash>.frag 6.7KB      Metal 片元
   └─ shaderMetal\<hash>.vert 3.1KB      Metal 顶点
```

### 1.1 config.json：一句说清这个效果挂在哪

```json
{ "effect": { "Link": [ { "type": "InfoSticker" } ] }, "alphaState": 2, "version": "5.7.0" }
```

`Link.type` 决定它能挂到哪类素材：`InfoSticker`（贴纸/信息层）、视频、文字。`alphaState` 是混合的 alpha 处理档位。**这套「声明挂载点」的做法值得抄**——效果不是全类型通用，靠 Link 声明适用范围，宿主据此过滤。

### 1.2 content.json：只有一个映射

```json
{ "filemap": { "prefab": "anim.prefab" } }
```

### 1.3 material / prefab：二进制，但属性名全露

两份文件都以魔数开头：

```
%SerializedFormat%@  ← 自定义序列化格式（同一个引擎）
```

实测能从里面直接读到这些标识符：

```
inputWidth  inputHeight  _alpha  baseTex  _MainTex
share://input.texture                        ← 输入纹理槽协议
blend_material  blend_propertySheet          ← 材质与属性表
blend_Prefab  root_entity  meshRenderer      ← 实体树结构
```

**结构判断**：这是「实体树（prefab）+ 网格渲染器（meshRenderer）+ 材质属性表（propertySheet）+ 纹理槽（baseTex/_MainTex 绑到 `share://input.texture`）」的四件套。跟上文文字模板里的 `Amaz` ECS 引擎是同一套运行时——`meshRenderer`、`root_entity`、`Scene`、`System` 全是它的话术。

`share://input.texture` 这个协议很关键：效果不自己取帧，而是从宿主的输入槽拿。我们照这个做，效果包就能与主机解耦。

### 1.4 着色器入口 xshader

`blend.xshader` 是入口描述（3.1KB），配 `Library\ShaderData\<hash>` 里按后端编译的源码。**同一份效果有三套落地：GLES 版、Metal 版、以及入口描述。** 我们只需要抄 GLES 那份的语言结构（GLSL→WGSL 是机械翻译），Metal 那份留着做 Apple 端交叉校验。

---

## 二、文字与贴纸：Amaz 引擎 + 模板桥

### 2.1 它不是「动画预设」，是一个 ECS 运行时

从 `template_sticker/js/template/template.js`（622KB，末尾带 `sourceMappingURL`）里读出的系统清单：

```
EventSystem  TransformSystem  BehaviorSystem  TweenSystem  ScriptSystem  JSScriptSystem
CameraSystem  AnimSeqSystem  GifAnimSeqSystem  VideoAnimSeqSystem  BuiltinObjectSystem
Sprite2DRendererSystem  MeshRendererSystem  SDFTextSystem  TextSystem
TextLayerRendererSystem  RenderSystem  UserEventHandleSystem  IFRootSystem  PostProcessSystem
```

19 个系统，能力覆盖：变换、补间、行为树、序列动画、GIF 动画、视频动画、2D 精灵、网格、**SDF 文字**（有向距离场，所以文字任意缩放不糊）、文字图层渲染、后处理。

场景构建方式是标准 ECS：`Amaz.Scene.create([...系统...])` + `AssetManager.rootDir` + `addCameraEntityToNativeScene`（正交相机、`orthoScale=1`、`clearType=DONT`、绑定 `SceneOutputRT`）。

### 2.2 模板桥 API 全表（可直接照建）

`Template` 类对外暴露的方法（原样）：

```
init(pathPrefix, screenWidth, screenHeight, dependResource, scriptPath)
createAnimationController(textComp, entity, startTime, endTime)
createStudioAnimBridge(...)          ← 给「Studio 动画」用的桥
setParametersForScript(parameters)   ← 宿主把参数塞进 JS
getParametersForScript(parameters)   ← JS 把状态回吐宿主
setParameters / getParameters
setAnimations(animParams) / setAnimsParameters(arr)
setKeyFrameParams / setCaptionParams / setCaptionDurationInfo
setRichTextParameters / setTextCapital
updateAnimationController(t) / postUpdateForScript(t) / reloadAllAnimationForScript()
setTimeRange(start,end) / setResolutionType(t) / onResize(w,h)
createLayer(name,param) / removeLayer(name)
updateSeekParamsToJS(seekParams)
getRuntimeScenes() / clearCache() / destroy()
```

**这套桥的设计值得整段抄**：宿主负责时间与布局，JS 负责表现，两边只通过 `setParameters/getParameters` 交换 JSON；`createLayer/removeLayer` 让 JS 能往宿主场景里加层；`updateSeekParamsToJS` 支持拖拽时间轴时的高频 seek。

### 2.3 text_params 字段表（文字的完整数据模型）

从 `template.js` 的 `parameters` getter 里逐个抠出来的字段，就是我们做文字模型该有的字段：

```
排版      richText  typeSettingKind  typeSettingAlign  enableMergeLines  lineMaxWidth
          lineSpacing  letterSpacing  innerPadding  oneLineCutOff  cutOffPostfix
          directionLevel  textLoopOnPathEnable  textExceedsPathProcessType
          offsetOnPath  typeSettingPathParam{typeSettingPathsFile, index, desc{geomType, paths[]}, curvesInfo[]}
画布      canvas  canvasColor  canvasRoundCorner  canvasRoundRadius  canvasRoundRadiusScale
          canvasWrapped  canvasCustomized  canvasWHCustomized  canvasWHFixed
          canvasOffsetCustomized  canvasAdvancedInfo{shapeType, fill}
字形      boldValue  italicDegree  decorationWidth  decorationOffset
          sdfTextAlpha  fallbackFontPathList[]
发光      bloomPath  bloomColorCustomized  bloomColor  bloomStrength  bloomRange
          bloomDirX  bloomDirY  bloomBlurDegree
颜色      selectedColor  ktvColor  ktvOutlineColor  ktvShadowColor   ← KTV 逐字上色三色
自适应    autoAdaptDpiEnabled
时序      caption_duration_info  keyframe_params  text_keyframe_params  anims[]
关联      association_params（文字跟随贴纸/说话人）
```

三个高价值发现：

1. **`ktvColor` / `ktvOutlineColor` / `ktvShadowColor` 三色**：这是「卡拉 OK 逐字上色」的实现机制——同一段文字三套颜色槽，按时间推进切换，不用逐字建节点。
2. **`typeSettingPathParam` 里带 `curvesInfo[].points`（每点 x/y）+ `geomType`**：文字可以沿贝塞尔路径排布，且路径数据直接进参数。
3. **`sdfTextAlpha` + `bloomStrength/bloomRange/bloomDir/bloomBlurDegree`**：文字是 SDF 渲染 + 独立发光通道，不是普通贴图加模糊。这两条决定了文字清晰度与质感，我们要照做。

---

## 三、转场：靠「混合模式 + 挂载声明」，不靠独立对象

`MixMode.json` 是索引表，每条三段 ID：

```json
{ "nameId": "color_filter", "effectId": "871339", "resourceId": "6758325170760323597", "path": "d9c1d4ca7ab91df4f48d12b339f2da88" }
```

- `nameId` 是语义名（`color_filter` `dark_en` `bright_en` `over_lay` `glare_pc` `soft_light` `linear_deepening` `darken_color` `color_dodge` `multiply_blend_mode`）——**这 10 个是本地内置的混合模式，全是 blend 类，不是「转场」。**
- `effectId` / `resourceId` 是平台侧的素材 ID，与云端素材库对齐。

结论：**本地只有混合模式包；真正的转场（溶解/推拉/闪白等视觉转场）在云端素材库，用时下载。** 但下载下来的包结构与 MixMode 完全一致（同一套 material/prefab/xshader），所以格式已经掌握，缺的只是素材本体。

`config.json` 里的 `Link.type=InfoSticker` 说明这类包是「挂在信息层上的混合器」，转场在草稿里以 `materials.transitions` + 片段两侧的切点引用表达（见主仓 A 文档 1.4.3）。

---

## 四、音频效果：124 个名字，DSP 是黑盒

`jianying/fx_packs.py` 从 `audioeffect.dll` 与音频模块字符串里提出 **124 个**效果名候选，覆盖混响、合唱、镶边、移相、延迟、压缩、限幅、均衡、高通、低通、变调、颤音、失真、降噪、去混响。

- **能拿到的**：效果名清单、参数命名习惯、链路顺序（草稿 `materials.audio_effects` 是数组，顺序即链序）。
- **拿不到的**：DSP 实现（在 DLL 里，是编译后的 C++）。

**接管方式**：名字与链路照抄（用户认知一致），实现换成 JUCE 自带 DSP + 开源模块：

| 剪映的效果类 | 我们的实现 |
| --- | --- |
| 混响 / 延迟 / 合唱 / 镶边 / 移相 | JUCE `Reverb` / `DelayLine` / `Chorus` / `Phaser` |
| 压缩 / 限幅 / 门限 | JUCE `Compressor` / `Limiter` |
| 均衡 / 高通 / 低通 | JUCE `IIR` 滤波器组 |
| 变调 / 变速 | Rubber Band（进程外） |
| 降噪 / 去混响 | DeepFilterNet3 / RNNoise |

参数面直接对齐剪映的命名（`intensity` `mix` `rate` `depth` `feedback` `threshold` `ratio`），用户从剪映迁过来不用重新理解。

---

## 五、字体：16 个随包字体就是它的排版基线

`Resources\Font` 里 27.8MB 字体，含自有字体（`后现代体.otf` 0.94MB、`悠然体.ttf` 2.8MB、`新青年体.ttf` 1.3MB）+ 系统字体兜底（`SystemFont\en.ttf`、`JuliaMono-Regular.ttf`）+ `Effect\seguiemj.ttf`（emoji）。

**它把「效果专用字体」单独放在 `Effect\` 下**——这跟我们文字模型里的 `fallbackFontPathList` 对得上：主字体缺失时按列表回退，emoji 单独一路。

---

## 六、可复用性判定（照 A/B/C 三档）

**A 档：可直接改成我们的实现**

| 资产 | 数量 | 做法 |
| --- | --- | --- |
| GLSL 片元/顶点着色器 | 88 个（gles） | 逐个翻 WGSL，落进我们的节点库；先挑 mixmode 与色度键各 3 个验证 |
| 效果包格式（config/content/material/prefab/xshader） | 全量 | 直接采用，改扩展名为 `.avsfx` |
| `share://input.texture` 输入槽协议 | 1 套 | 照抄，效果与宿主解耦 |
| `Template` 桥 API（20 个方法） | 1 套 | 照抄接口，内部换成我们的场景运行时 |
| `text_params` 字段表（50+ 字段） | 1 套 | 直接作为我们文字模型的字段基准 |
| `ktvColor` 三色逐字上色 | 1 个机制 | 照抄，做卡拉 OK 字幕 |
| 字体回退链（`fallbackFontPathList` + `Effect\` 专用字体） | 1 套 | 照抄 |

**B 档：能读、能对照，不直接搬**

- `material` / `prefab` 二进制本体（属性名可读，值要解析）。
- `template.js` / `main.js`（622KB / 267KB，压缩 + 有 sourcemap 声明，可以试着恢复）。
- 音频效果链路命名与顺序。

**C 档：拿不到**

- 音频 DSP 实现。
- SDF 字形生成器（在 `VECreator.dll` / `cccreator.dll` 里）。
- 云端素材库的素材本体（格式已知，内容要下载）。

---

## 七、移植顺序（按性价比）

```
① 效果包格式 + input.texture 协议（1 周，地基）
② 6 个着色器翻 WGSL：mixmode 3 个（soft_light / glare / color_dodge）+ 色度键 3 个
③ text_params 落成我们的文字模型（50 字段 + ktv 三色 + SDF 发光）
④ Template 桥按 20 个方法实现，先接一个贴纸模板跑通
⑤ 音频效果：124 个名字对齐 JUCE DSP，先做 12 个常用的
⑥ 转场：格式已通，等云端素材或自研 6 个基础转场（溶解/擦除/推/拉/缩放/闪白）
```

---

## 八、复核命令

```bash
# 五类资产清点（37 条目 / 52 组双后端着色器 / 124 个音频效果名）
python jianying/fx_packs.py --install "<剪映安装根>" \
  --audio-dll "<剪映安装根>/audioeffect.dll" --out reports/jianying_fx_packs

# 模板 JS 与文字参数（在安装目录里直接读）
#   Resources/template_sticker/js/template/template.js     622KB，Amaz 引擎桥
#   Resources/aigc_text_template/js/main.js                267KB，模板实例
#   Resources/aigc_text_template/content.json              模板声明

# 一个完整效果包的结构（对着看 material/prefab/xshader/ShaderData）
#   Resources/MixMode/042aa15b71b1e17bca0bd928eec6fba7/
```

> 恢复出的着色器源码与模板 JS 与我们此前处理 UI 源码的原则一致：**只在本地持有，不入库**。仓库里留解析工具与资产清单。