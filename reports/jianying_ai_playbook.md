# 剪映 AI 接管手册

一句话：**21 项 AI 能力，3 类落点（端侧 45 个模型包 240MB / 云侧 139 个服务条目 / 双路 5 项），内部 567 个 AI RPC，外部只有 26 条安全命令。** 这一层是剪映最值钱的部分，也是它的护城河，本手册的目标是把它拆成我们能直接实现的规格。

数据来源：`jianying_ai_matrix.md`（能力×落点×证据）、`jianying_ai_deep.md`（RPC 全表 567 / 流水线目录 40 / 模型规格 45 / 云服务 139）。两份都由本仓库脚本从真实安装与二进制里跑出来。

---

## 一、三层结构（一眼看清它怎么搭的）

```
UI / 前端（Qt6 + Lynx + CEF）
   │  26 条安全命令（模型可调）
   ▼
lyra 层（videoeditor.dll，567 个 AI RPC）
   ├── 任务调度：CreateAsyncTasks / GetAsyncTask / CancelAsyncTask / GetSegmentProgress
   ├── 流水线：CreateClipFlowNode / DecisionNode / AddClipflowNodeHooker
   ├── AIGC：AddAigcGenerate / ApplyAigcGenerateVideoWriteBack / CheckAllAIGCContent
   └── 效果：AIGCEffectStartVETaskMixNode / AddDigitalHuman / AddMatting
   │
   ├──► 端侧推理（onnxruntime+CUDA / OpenVINO+NPU / QNN+Hexagon / ByteNN）
   │      45 个模型包，`<name>_v<major>.<minor>.model`，按能力分目录
   │
   └──► 云端（139 个服务条目，`lv-api.ulikecam.com` / `lv-pc-api.ulikecam.com`）
          common_task{new,query,sync,cancel} / capflow{submit,query,cancel,history_task}
          audio_subtitle{subimit,query,highlight,get_keyword} / text_to_video{submit,query}
          voice{voice_clone_condition,delete,release} / copilot{conversation,modify_message}
```

**两个立刻可用的判断**：
1. **它把 AI 当成异步任务做，不当成同步函数**。567 个 RPC 里 44 个专管任务生命周期，草稿里还有 `attachment.insertAsyncTasks / updateAsyncTasksStatus` 落状态位——任务句柄进了工程文件。
2. **它自己不做 LLM**。`copilot/conversation` 在云侧，端侧只有 CV/音频小模型。所以它的「AI 剪辑」= 云上大模型决策 + 端侧小模型执行 + 本地流水线编排。

---

## 二、五个可以直接搬的模式

### M1　异步任务模型（搬这个最省事）

```
CreateAsyncTasks / CreateAsyncTasksWithCallback / CreateBatchAsyncTasksWithPrepare
GetAsyncTask / GetAsyncTasks / GetSegmentProgress
CancelAsyncTask / CancelAsyncTasks / CancelDraftAsyncTasks
AppendAsyncTaskListener / GetAsyncTaskPersistDir / GetAsyncTaskPostRealProgressEnable
```

要点全在方法名里：
- **持久化目录**（`GetAsyncTaskPersistDir`）→ 任务状态落盘，重启能续。
- **分段进度**（`GetSegmentProgress`）→ 长任务按片段汇报，不是一根进度条。
- **真实进度开关**（`GetAsyncTaskPostRealProgressEnable`）→ 它明确区分「上报进度」与「真实进度」，说明有过假进度的问题。
- **批任务 + 准备阶段**（`...WithPrepare`）→ 先做准备（分配资源/落盘），再批执行。
- **监听器可追加**（`AppendAsyncTaskListener`）→ 多消费者订阅同一任务。

→ 我们的落地：AI 进程里做 `TaskLedger`，状态机 `prepare → run → partial → done|failed|cancelled`，进度按「片段/帧区间」上报，落 SQLite；对外用 MCP `notifications/progress`（progress 单调递增、`total` 可浮点）。

### M2　clipflow 节点图（它的剪辑流水线本体）

```
CreateClipFlowNode / ClipflowNode / DecisionNode / AddClipflowNodeHooker / AddClipflowTaskHooker
ApplySegmentSmartEdit / ApplySmartCrop / ApplyTextSmartSplit / AddScenes / GetAllFeatureSceneSegment
```

源码树里对应的实现目录：`ve_wrapper/clipflow/shell/common_node`（11 文件）、`clipflow/task/material_generation/node`（8）、`clipflow/task/subtitle_recognize/node`（7）。

→ 结论：**它的「智能剪辑」是一张节点图，节点是「素材生成」「字幕识别」这种任务，决策点是 `DecisionNode`，钩子让宿主能插手**。我们的 Director/Editor 用一个 DAG 承载同样语义，节点类型先定 8 个：`analyze → script → select → arrange → text → effect → mix → verify`。

### M3　AIGC 附件数据模型（生成物怎么回写工程）

```
AddAigcGenerate / AddAigcGenerateItems / AddAigcSegment / BatchAddAigcSegments
ApplyAigcGenerateAttachment / ApplyAigcGenerateAudio / ApplyAiGenerateImageWriteBack
ApplyAiGenerateVideoWriteBack / ApplyScriptAiCutClipInfoToMainDraft
CheckAllAIGCContent / CheckUseAIGCContent / AigcWatermarkStatusCallback
```

`lyra/generated/attachment/model` 下 86 个源文件就是这套附件模型的全部类型。

→ 三个可搬的设计：
1. **生成物是「附件」不是「素材」**：先落附件，再回写（`WriteBack`）成轨道片段。这样生成失败不污染工程。
2. **AIGC 内容要过检查**（`CheckAllAIGCContent`）再进工程，水印状态单独回调。这套我们照做（内容标识与审核）。
3. **脚本剪辑结果整体回主草稿**（`ApplyScriptAiCutClipInfoToMainDraft`）→ 对应我们的「脚本 → 时间轴」一次性落地。

### M4　云任务四件套（它的云端长任务协议）

```
common_task/new → common_task/query → common_task/sync → common_task/cancel
capflow/submit → capflow/query → capflow/cancel → capflow/history_task
text_to_video/submit_generate_video_task → query_generate_video_task
```

四件套 = 提交 / 轮询 / 同步拉结果 / 取消。`history_task` 说明任务记录在服务端留档。

→ 我们的网关统一成同一套：`submit → poll → fetch → cancel`，本地 `capflow` 这一层就是 M1 的 `TaskLedger`，云端只是执行器。

### M5　模型货架规范（目录即能力清单）

`Resources\models\` 45 个目录，文件名一律 `<name>_v<major>.<minor>.model`，实测样本：

| 包 | 文件 | MB | 说明 |
| --- | --- | --- | --- |
| `mattingmodel` | `tt_matting_video_v1.0` 5.8 / `tt_matting_video_gru_v1.0` 3.5 / `saliency_matting_v1.0` 6.9 / `tt_matting_big_v15.0` 0.2 | 20 | 视频抠像走 GRU 时序；0.2MB 那档是轻量兜底 |
| `interpolation` | `lens_vfi_v1.0` | 10.3 | 插帧单模型 |
| `audiomodel` | `aed40_10m` 9.6 / `sentence_score_v1.1` 4.6 / `bt_espresso_mobile_offline_v1.4` 0.4 / `bt_streaming_espresso_v1.2` 0.5 | 31 | **本地有 ASR（espresso）**、有音频事件检测（aed）、有句子打分 |
| `depthmodel` | `tt_depth_estimation_v3.0` | 1.2 | 深度估计 |
| `rnnoise`（在 Resources 根） | `rnnoise_v2.0` | 0.12 | 端侧降噪 |

→ 三个可搬的规范：**目录名 = 能力 ID；文件名带语义版本；同一能力允许多档（轻量/标准/大）并存，运行时按算力选档。**

---

## 三、逐能力接管表

| 能力 | 剪映落点 | 硬证据 | 开源替代（我们真正用） | 工作量 |
| --- | --- | --- | --- | --- |
| 人像抠像 / 视频分割 | 端侧 | 9 个模型包 52MB + 59 个类（`AIMattingClient`） | SAM 2（提示分割）+ BiRefNet（人像），MIT/Apache | ★★★ |
| 绿幕 / 色度键 | 端侧 | `Chroma`/`Chroma2` 资源 + 42 个类 + 6 条命令 | 自研色度键 shader | ★ |
| 美颜 / 美妆 / 塑形 | 端侧 | 7 个模型包 + 74 个类 + `setFigure/setMakeupRoot` | 开源美颜（FaceVerse/GFPGAN 系，注意协议） | ★★★★ |
| 人脸识别 / 聚类 | 端侧 | 3 个包（faceclusting/faceverify/freid） | InsightFace（MIT 需核）+ 自研聚类 | ★★ |
| 手部 / 骨骼 / 数字人驱动 | 双路 | 4 个包 + 113 个类 + 数字人云端点 | MediaPipe Hands / RTMPose | ★★★★ |
| 深度 / 显著性 | 端侧 | depth 1.2MB + saliency 3.7MB | DepthAnything / U2Net | ★★ |
| 插帧 / 超分 / 去闪烁 | 端侧 | `lens_vfi` 10.3MB + 31 个类 | RIFE / Real-ESRGAN（BSD/Apache 需核） | ★★★ |
| 防抖 | 端侧 | 18 个类 + `setStable` | vidstab（FFmpeg 内置） | ★ |
| 画 / 音降噪 | 端侧 | rnnoise 121KB + 2 包 + 4 命令 | DeepFilterNet3 + RNNoise | ★★ |
| 人声分离 / 修音 / 变声 | 端侧 | `audiomodel` + 43 个类 + 9 条命令 | Demucs v4（MIT）+ Rubber Band | ★★★ |
| 语音识别（本地档） | **双路** | `bt_espresso_mobile_offline` 0.4MB + `bt_streaming_espresso` 0.5MB | whisper.cpp / sherpa-onnx | ★★★ |
| 语音识别（云侧高质量） | 云 | `audio_subtitle/{submit,query,highlight,get_keyword}` | 自建 faster-whisper 服务 | ★★ |
| 句子打分 / 水词判定 | 端侧 | `sentence_score_v1.0/1.1` 10.8MB + `aed40_10m` | 自研（转写 + 规则 + 小分类器） | ★★★ |
| TTS / 音色克隆 | 云 | `text_to_audio` + `voice/{clone_condition,delete,release}` + `aigc_text/get_voiceclone_text` | IndexTTS/CosyVoice（协议需核） | ★★★★ |
| 视觉跟踪 / 物体锁定 | 端侧 | `object_tracking` + 84 个类 + 12 条命令 | ByteTrack（MIT）+ SAM2 | ★★★ |
| 智能裁剪 / 运镜 | 端侧 | `saliency_seg` + 24 个类 + `ApplySmartCrop` | 自研（显著性 + 构图规则） | ★★ |
| 智能打光 / 眼神 / 画质修复 | 端侧 | `idream` + 74 个类 + `setVideoAlgorithm` | IC-Light 系 / 自研 | ★★★★ |
| 素材语义检索 | 双路 | `media_search` 31.6MB + 8 条端点 | CLIP/Chinese-CLIP + sqlite-vec | ★★ |
| AIGC 生成（文/图/视频） | 双路 | 106 个 RPC + `zenith/submit_image_task` + `text_to_video/*` + `ai_writing/*` | 接外部模型（ComfyUI 进程外 / API） | ★★★★★ |
| 数字人 | 双路 | 2 个包 + 47 个类 + `digital_human` 端点 | 开源驱动 + 自研渲染 | ★★★★★ |
| 场景检测 / 镜头切分 | 云 | `smart_recognition` + `audio_subtitle/highlight` + 7 个类 | PySceneDetect + 自研音频辅助 | ★★ |
| 隐形水印 / AI 标识 | 双路 | `invisible_watermark` + 60 个类 + `updateDraftAIGCWatermark` | 自研（频域水印） | ★★★ |
| 内容审核 / 版权检查 | 云 | `image/{anime_copyright_checker,content_classifier,face_compare}` + `CheckAllAIGCContent` | 自建审核链 | ★★ |

---

## 四、反向工程挖到的四个硬事实（都能改我们的设计）

1. **本地 ASR 真的存在，而且很小**：`bt_espresso_mobile_offline_v1.4` 只有 0.4MB，`bt_streaming_espresso_v1.2` 0.5MB。之前把它判成「纯云侧」是错的——它是**双路**：本地流式出草稿字幕，云端出高质量修正。这条已回写进 `jianying_ai_matrix.md`。
2. **「去水词」不是规则，是模型**：`sentence_score_v1.0/1.1`（4.6–6.2MB）+ `aed40_10m`（音频事件检测 9.5MB）。说明它把「这句要不要留」交给一个句子级打分器，再用音频事件（笑点/停顿/掌声）校正。我们做同类功能直接照这个两段式：句子打分 + 音频事件。
3. **AI 任务句柄进工程文件**：草稿里有 `attachment.insertAsyncTasks / updateAsyncTasksStatus`，还专门有 `GetAsyncTaskPersistDir`。**它的工程文件能记录「哪些片段的 AI 处理还没跑完」。** 我们 AVS 的 `ai.runs[].steps[]` 要补同样的持久化语义。
4. **云端有 copilot 会话接口**：`copilot/{conversation,modify_message,section,upload_material}`。这就是它在应用内聊天的后端——**它的「AI 剪辑」最终落在一个云上对话式 Agent**，跟前端 UI 绑死。我们的架构优势在这里：Agent 在本地、工程在本地、可被外部 MCP 编排。

---

## 五、我们要落的东西（对应主仓 D 文档的层）

| 我们要建 | 对应剪映 | 对应主仓层 | 阶段 |
| --- | --- | --- | --- |
| `TaskLedger`（准备/运行/分段进度/取消/持久化） | M1 异步任务模型 | L9 视频理解 | 3 |
| `Pipeline DAG`（8 类节点） | M2 clipflow | L10 内部 Agent | 3-4 |
| `ai_decision` 表 + 生成物回写事务 | M3 AIGC 附件模型 | L3 工程存储 | 3 |
| 网关长任务四件套 | M4 common_task | L11 模型网关 | 2 |
| 模型包规范（目录即能力 + 语义版本 + 多档） | M5 模型货架 | L9 + 打包 | 3 |
| 本地 ASR 档 + 云侧精修档 | espresso 双路 | L9 | 3 |
| 句子打分 + 音频事件（去水词） | sentence_score + aed | L9 | 4 |
| 内容审核与水印链 | 审核端点 + 水印包 | L12 交付 | 5 |

---

## 六、复核命令

```bash
# 能力矩阵（端侧/云侧/双路 × 证据）
python jianying/ai_surface.py --install "<剪映安装根>" \
  --rtti reports/rtti_jy_veditor.json --commands reports/commands_jy.json \
  --strings reports/str_jy_veditor.txt --endpoints reports/jy_endpoints.txt \
  --out reports/jianying_ai_matrix

# 深挖（567 个 AI RPC / 40 个流水线目录 / 45 个模型规格 / 139 个云服务）
python jianying/ai_deep.py --install "<剪映安装根>" \
  --rtti reports/rtti_jy_veditor.json --src reports/src_jy_veditor.json \
  --endpoints reports/jy_endpoints.txt --out reports/jianying_ai_deep

# 端点扫描（18 个模块，URL 214 / 主机 133 / 路径 629）
python jianying/endpoint_scan.py --dir "<剪映安装根>" --out reports/jy_endpoints.txt
```