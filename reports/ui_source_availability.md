# UI 源码可得性：能拿到多少、拿到什么形态

先给结论：**「完整 UI 源码」只能部分拿到，而且两家的拿法完全不同。**

| 目标 | 能拿到 | 形态 | 可用度 |
| --- | --- | --- | --- |
| 剪映 Lynx/React 前端页 | **292 个原始源文件**（1 个包的 sourcemap 带 `sourcesContent`） | 原始源码：React + TSX + SCSS，含原始 import 路径 | **可直接复用** |
| 剪映其余 340 个前端包 | 压缩代码 → 去压缩后 **86.8MB / 单包最高 19 万行** | 可读代码（结构还原，变量名仍是 a/b/c） | 可读、可改、可对照 |
| 剪映 CSS（123 个） | **5.3MB 完整源码** + **1,704 个 CSS 令牌** | 原始源码 | **可直接复用** |
| 剪映主界面 / 时间轴 | 无源码：C++ + Qt 自绘，QML 只在 Qt 自带目录 | 只剩类名与资源 | 不可得，只能照结构重写 |
| 达芬奇 UI 控件 | 无源码：Qt Widgets 自绘 + `UI_Resource\Steinway` 1,332 张 BMP | 切图资产 | 设计可抄，代码不可得 |
| 达芬奇 Fusion 皮肤 | **`Fusion.fuskin` = ZIP，含 3 套 `.skin` 文本定义 + 7,190 PNG** | **皮肤 DSL 明文**（颜色令牌 64 / 尺寸常量 18 / 控件类别树） | **可直接复用** |
| 达芬奇 QML | 453 个全是 Qt 自带 Controls.2 / Extras / Dialogs | 第三方 | 无应用代码 |

一句话：**剪映的 Web 化界面能拿到源码（1 个包是原文，其余是可读代码），C++ 主界面拿不到；达芬奇只有皮肤 DSL 与切图，控件代码全在编译产物里。**

---

## 一、剪映：sourcemap 是唯一直通道

### 1.1 命中了什么

`jianying/sourcemap_extract.py` 扫了 351 个 JS 包：

```
带可用 sourcemap 的包：1 个     → 还原 292 个源文件 / 0.5MB
无 sourceMappingURL：340 个
有 map 引用但文件缺失：10 个
```

命中的那个包是 `Resources\image_h5_videocutpc_guide\guide\index.ac06fa4c.js`（引导页），还原出来的目录：

```
index.ac06fa4c\
├─ src\container\Guide\index.tsx        页面组件
├─ src\…                                业务模块
├─ .ace\plugin-mpa\guide\bootstrapApp.tsx
├─ node_modules\…                       依赖（含原文）
└─ webpack\…                            配置残留
```

还原出来的确实是原文，三条铁证：

1. 原始 import 语句完整：`import React, { useState } from 'react';`、`import style from './style.module.scss';`
2. 内部包路径没被改写：`@byted/hooks`、`@bridge/d`、`@ies/ace-renderer-react`
3. **构建机的绝对路径还在**：`/Users/bytedance/Desktop/image_lv_pc_web/node_modules/…` —— macOS 打包，工程根目录 `image_lv_pc_web`

语言分布：JavaScript 288 / TSX 3 / TypeScript 1 / SCSS 1 / 无后缀 6。

### 1.2 剩下 340 个包怎么办

它们没有 map，只能去压缩。`tools/js_beautify.py` 用状态机做安全换行（识别字符串、模板串、正则、注释，不破坏内容），跑完：

```
311 个包（≥8KB）：70.2MB → 86.8MB，全部可读
最重的几个：
  app-server.mjs                              12.6MB → 190,957 行
  image_h5_smart_voiceover_script_v3/393.js    2.4MB →  84,047 行
  local-document-worker.mjs                    2.4MB →  77,190 行
  canvas_agent async/4707.js                   2.1MB →  72,446 行
```

**这给的是「能读能改的代码」，不是原始命名。** 做行为对照、抄交互逻辑、抄数据流都够用；想拿原始变量名与注释，只有那 292 个文件有。

### 1.3 剪映的 UI 是四套技术拼出来的

从资源形态反推（`[实测]`）：

| 区块 | 技术 | 证据 |
| --- | --- | --- |
| 主窗 / 时间轴 / 监视器 | C++ + Qt Widgets 自绘 | 二进制里无 rcc（`qres` 0 命中），磁盘上无应用 QML |
| 面板与画布（AIGC 节点） | React + react-flow + 自研 `lv-` 组件库 | CSS 里有 `react-flow__*` 全套变量、`lv-modal` / `lv-btn` / `lv-input` |
| 运营页 / 商城 / 活动 | Lynx（字节跨端框架） | `lynx.dll` + `lynx_core.js` + `lynx_config\*` 页面包 |
| 引导 / 智能文案等 H5 | React + webpack（CEF 承载） | 这次还原出源码的那批 |

**这条结构判断很值钱**：它说明专业剪辑软件的「重交互主界面」用原生自绘，而「运营与 AI 面板」用 Web 技术栈。我们要照这个分工定 UI 架构——时间轴自绘、面板 Web 化。

---

## 二、剪映：设计系统是白送的

`jianying/ui_tokens.py` 扫完 123 个 CSS，抽出 **1,704 个 CSS 自定义属性**，等于把它的令牌表直接交出来。核心一组：

```
背景      #141414（应用底） #262626（弹层） #1c1c1c（输入框） #3b3b3b（次按钮）
文字      #e0e0e0（主） #949494（次） #7a7a7a（占位） #525252（提示）
强调      #00c1cd（青，选中/描边） #f5f6ff（主按钮底） #151822（主按钮字）
语义      #ef4444（危险） #ea3223（错误）
描边      hsla(0,0%,100%,.06/.08/.12/.2) 四档，统一 0.5px 发丝线
模糊      backdrop-filter: blur(48px/24px/20px) 三档
圆角      6 / 8 / 9 / 10 / 12 / 14px
字号      9 10 11 12 13 14 16px，行高 12 14 16 18 20 24
字体      PingFang SC, Inter, ui-sans-serif, system-ui
动效      cubic-bezier(.34,1.32,.64,1) 0.4s 入场 / 0.22s 淡入 / 1s 旋转 / 2.6s 微光
组件尺寸  工具条 40px、按钮 32px、图标按钮 22/24/36px、输入 28/36/40px、
          弹窗宽 300/420/459/480px、预览块 44/48px、封面板 126px、文本域 240px
```

这套数字不是猜的，是它生产环境的取值。**我们做 UI 可以直接把它当基线**，不必从零调。

## 三、达芬奇：皮肤是明文 DSL

`Fusion.fuskin` 是 ZIP（22.6MB / 7,201 条目），里面三样东西：

```
Fusion.skin   289KB   颜色令牌 64 + 控件类别树 + 状态样式
Neutral.skin    7.6KB  中性灰一套（同结构、无色相）
Tablet.skin    44KB   纯度量：LabelW=132  ButtonH=26  CheckBoxH=17  ComboH=24  EditW=55  LabelH=16
```

`Tablet.skin` 那段是 UI 布局规格的原文：

```
LabelAlign = "Right"
ControlLabel = { MarginX = 5, MarginY = 4, FixedX = LabelW, FixedY = LabelH, Control = "label", Align = LabelAlign }
Skin = { ID = "Tb80", Name = "Fusion 8", Controls = Category { Button = Category { Layout = { HGroup { MarginT=4, MarginB=4, … } } } } }
```

颜色命名是一套海洋生物代号（`DropShipGray` `PoseidonGray` `DolphinGray` `NewtGray` `JaguarGray` `JellyFishGray` `OctopusGray` `PenguinGray` `PlanktonGray` `SquidGray`），每色另给 40% / 70% 透明度变体 `…Col`。

资产层：7,190 张 PNG（其中 **3,444 张是 @2x HiDPI 变体**，占 48%），分区按 UI 区域：`Tools` 4,376（Fusion 节点图标库）/ `Tracker` 350 / `ViewStrip` 324 / `Icons` 282 / `Polyline` 222 / `Text` 168 / `Spline` 166 / `Transport` 158 / `Paint` 148 / `Controls` 110 / `Color` 86 / `Views` 82。交互态全是切图（hover/pressed/disabled/selected/mask）。

主界面皮肤：`UI_Resource\Steinway\` 1,332 张 BMP（Steinway 是 Resolve 的 UI 代号），配 `Control\PanelLCDControlFile.txt`（206KB）——一张 `MODE | AREA | LEVEL | LAYER | PIXEL_OFFSET | LINE_OFFSET | MIX_RATIO | BAR_ENABLE | PARAM_ID | IMAGE_PATH` 的映射表，把硬件调色面板的每个按键/屏幕位置对到具体 BMP 与参数 ID。

**结论：达芬奇的 UI 代码拿不到，但它的皮肤语言、度量规格、图标分区、HiDPI 策略全部明文。抄设计够用，控件代码没有。**

---

## 四、能不能「直接复用」——分三档说清

**A 档：可直接放进我们工程的（真源码/真规格）**

| 东西 | 来源 | 怎么用 |
| --- | --- | --- |
| 剪映 CSS 令牌表（1,704 条） | `reports/ui_jianying.json` | 做成我们的 design token 文件，换皮即用 |
| 剪映 292 个原始源文件 | `ui_src/`（本地，未入库） | 照它的组件组织与 bridge 调用方式写我们的面板 |
| Fusion `.skin` 三套 | `reports/ui_resolve_skin.json` | 抄它的「颜色令牌 + 空间度量 + 控件类别树」三层结构 |
| Fusion 图标分区与命名 | `reports/ui_resolve_skin.md` | 直接决定我们节点库的图标组织方式 |
| PanelLCD 映射表 | `Control\PanelLCDControlFile.txt` | 做硬件面板支持时照这张表建模 |

**B 档：能读能改，但要从压缩代码里读（311 个包 / 86.8MB）**

拿来做交互行为对照：节点面板怎么开、参数怎么同步、撤销怎么撤销、AI 面板的状态机怎么走。**照行为重写，不照代码搬。**

**C 档：拿不到（C++ 自绘）**

时间轴绘制、监视器合成、波形绘制、调色轮。这些只能靠观察 + 我们的自研实现，没有捷径。

---

## 五、为什么恢复出来的源码没有入库

`ui_src/`（292 个原始源文件）与 `ui_src_beautified/`（86.8MB 可读代码）**留在本地，不进仓库**：

- 那是第三方产品的原文，入库等于公开转载它的代码；
- 工具是我们的，方法论是我们的，产物不是。

仓库里留的是：提取工具（`sourcemap_extract.py` / `js_beautify.py` / `ui_tokens.py` / `skin_parse.py`）、可复现命令、以及**不含量化源码的结果报告**。谁都能在自己的副本上跑出同样的东西。

---

## 六、复核命令

```bash
# 1) 还原带 sourcemap 的原始源码（产出在本地 ui_src/）
python jianying/sourcemap_extract.py --install "<剪映安装根>" --out ui_src

# 2) 其余包去压缩（产出 ui_src_beautified/，单包最高 19 万行）
python tools/js_beautify.py --install "<剪映安装根>" --out ui_src_beautified --min-kb 8

# 3) 剪映设计令牌（1704 条 CSS 变量 + 调色板 + 字号/圆角/动效）
python jianying/ui_tokens.py --install "<剪映安装根>" --out reports/ui_jianying

# 4) 达芬奇 Fusion 皮肤（3 套 skin + 7201 条目 + 3444 HiDPI）
python resolve/skin_parse.py "<Resolve 安装根>/Skins/Fusion.fuskin" --out reports/ui_resolve_skin
```