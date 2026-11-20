# 代码级逆向结果：剪映 11.7 + DaVinci Resolve 21.2 + AE 27.0

本文所有数字都来自本仓库脚本对真实二进制的实跑，命令与产物一一对应。复核方式见每节末尾。

| 目标 | 产物 |
| --- | --- |
| 剪映 `videoeditor.dll`（70.42MB） | PE 报告、15,041 个 RTTI 类名、1,391 个源文件路径、770 个 lyra 接口、199 条命令表、加密实现证据链 |
| 达芬奇 `Resolve.exe`（581MB）+ `fusionscript.dll` | 251 万条唯一串、OpenSSL/CNG 指纹、530 个脚本 API、`.drp` 结构与时间轴解析 |
| AE `.aep` | RIFX chunk 走查器 + 自检样本 PASS |

---

## 一、剪映专业版 11.7.0.14652

### 1.1 二进制身份（`pe_info.py`）

| 文件 | 大小 | 链接器 | 编译时间(UTC) | PDB 路径 |
| --- | ---: | --- | --- | --- |
| `videoeditor.dll` | 70.42MB | 14.29（VS2019 16.11） | 2026-10-28 12:18:51 | `D:\j\workspace\lv-window-Release@2\WorkSpace\bin\JYPacket\11.7.0.14652\videoeditor.pdb` |
| `JianyingPro.exe` | 0.42MB | 14.29 | 2026-10-28 12:53:34 | `D:\j\workspace\lv-window-Release@2\WorkSpace\bin\JYPacket\11.7.0.14652\JianyingPro.pdb` |
| `jianying-agent-cli.exe` | 0.12MB | 14.29 | 2026-10-28 12:19:25 | `D:\j\workspace\lv-window-Release@2\WorkSpace\bin\JYPacket\11.7.0.14652\jianying-agent-cli.pdb` |

三条结论：
1. CI 工作区名 `lv-window-Release@2`（`lv` = 剪映内部代号，与草稿 `platform.app_source="lv"` 完全对上）。
2. 三个产物时间戳集中在 2026-10-28 12:18–12:53，说明是同一次构建流水线出的整包。
3. PDB 没剥离 → 构建路径、模块划分全部暴露（下一节直接吃这条）。

### 1.2 源码树回收：1,391 个文件、313 个目录（`src_tree.py`）

`assert` 与日志里残留的 `__FILE__` 直接还原出内核的模块结构：

```
videoeditor\lyra\
├─ generated\draft\                    296 个 .cpp   ← 草稿对象与补丁协议（机器生成）
├─ generated\attachment\model\         265 个 .cpp   ← 素材附件模型（机器生成）
├─ generated\action\params\             31 个 .cpp   ← 动作参数结构
├─ service\video\                       16 个        ← 视频服务
├─ service\patch\helper\patch_extra_handlers\{,algorithm}\  11+11 个
├─ service\text\ , text_template\ , text_template_editor\   7+7+8 个
├─ service\draft\repair\tasks\           8 个        ← 草稿自修复
├─ service\draft\linkage_refactor\consumer\  7 个
├─ trash_src\migration\tasks\           16 个        ← 版本迁移
├─ trash_src\keyframe\                  10 个
├─ trash_src\draftstore\                 9 个
├─ trash_src\draft_cross\template\{json_parser,publish\functions}\  10+10 个
├─ ve_wrapper\segment_prerender\high_complexity\  12 个
├─ ve_wrapper\clipflow\{shell\common_node,task\...}\  11+8 个
└─ trash_platform\pubapi\               22 个        ← 对外 API 层
```

读法：`generated/` 下 561 个文件是 IDL/代码生成器的产物，对应第三节那 770 个接口；`trash_*` 是重构后扔进去的旧模块（`draft_cross`＝跨端草稿、`migration`＝版本迁移、`pubapi`＝对外 API），这批目录名本身就是架构演进史。

### 1.3 类地图：15,041 个 RTTI 类名、60 个命名空间（`rtti_dump.py` / `rtti_report.py`）

未剥离 RTTI，`.?AV...@@` 类型描述符直接可读。能力面命中数：

| 能力面 | 命中类 | 代表类 |
| --- | ---: | --- |
| Agent 与协议 | 3,584 | `lyra::ApplyPatchReqStruct`、`lyra::AddPatchHandler`、`clipflow::DecisionNodeResp` |
| 片段与素材 | 1,020 | `lvve::MaterialDigitalHumanModelDressing`、`ShapeScriptTextStickerClipData` |
| AI 与算法 | 757 | `lvve::AIMattingClient`、`lvve::AiMattingApplyParams`、`lvve::AigcWorkflowDraftSegmentInfo` |
| 特效与合成 | 626 | `lvve::AttachmentAigcPrompt`、`lvve::...` 效果/滤镜附件族 |
| 草稿与工程 | 398 | `SerializerDraftFuncImpl`、`DeserializerDraftFuncImpl`、`DraftDowngradeFuncImpl`、`CloudDraftGenerator` |
| 加密与授权校验 | 257 | `CryptoPP::GCM_Base`、`CryptoPP::CTR_ModePolicy`、`CryptoPP::Rijndael_Info` |
| 时间轴 | 174 | `lvve::MainTrackAdsorbParam`、`lvve::AudioTrackIndexParam`、`AttachmentPCTimelineControl` |
| 命令与撤销 | 77 | `lvve::RichTextCommand`、`clipflow::UndoRedoTasksReqStruct` |

两个立刻可用的判断：
- `generated\draft` 的 296 个文件 + `lyra` 命名空间的 Req/Resp 结构体成对出现 → 草稿修改是**请求/响应式 RPC**，不是函数直调。
- `clipflow::` 前缀说明剪辑流程本身被抽象成了**节点图**（`DecisionNodeResp`、`common_node`、`task\material_generation\node`），AI 的每一步就是一个节点。

### 1.4 接口面反推：lyra 770 个方法（`api_surface.py`）

C++ 里 `<方法>ReqStruct` / `<方法>RespStruct` 成对命名，配对即可还原接口清单。`lyra` 命名空间下 3,420 个类反推出 **770 个方法**，示例（原样取自 RTTI）：

```
AddAudio            AddAudioReqStruct            AddAudioRespStruct
AddCommonKeyframe   AddCommonKeyframeReqStruct   AddCommonKeyframeRespStruct
AddMatting          AddMattingReqStruct          AddMattingRespStruct   (+ AddMattingListenerRespStruct)
AddMaskTracking     AddMaskTrackingReqStruct     AddMaskTrackingRespStruct
AddCustomMatting    …                            …
AIGCEffectStartVETaskMixNode  …Req/…Resp  (+ …Param, …ConvertResp)
```

完整清单：`reports/api_jy_lyra.md`（84KB，一张表把 770 个方法、请求体、响应体、同族结构列全）。

顺带三个副产品：`reports/api_jy_lvve.md`（0 个 —— `lvve::` 用附件/服务命名而不是 Req/Resp，说明内核层是直接调用，RPC 只在 lyra 层）；`reports/api_jy_clipflow.md`（5 个，节点图接口）。

### 1.5 原生命令表：18 个域 / 199 条 / 模型安全子集 26 条（`command_table.py`）

从 `Resources\canvas_agent\runtime\app-server.mjs` 里冻结的白名单对象抽出（JS 侧是 C++ 命令面的镜像）：

| 域 | 条数 | 域 | 条数 |
| --- | ---: | --- | ---: |
| video | 56 | attachment | 13 |
| audio | 24 | story | 11 |
| segment | 19 | textTemplate | 8 |
| text | 16 | sticker | 7 |
| draft | 14 | undoRedo | 6 |

安全子集 26 条（`IX1=Object.freeze([...])`），含 `draft.setCanvasSize`、`track.add`、`segment.split/setTimeRange/delete`、`video.add/setVolume/muteOn`、`audio.add/setVolume`、`text.add`、`undoRedo.*`、`invokeBatch`。

**这条是剪映给 AI 划权限边界的方式：199 条给内核与内部脚本，26 条给模型。**

### 1.6 草稿加密：证据链（不解密）

`find_crypto.py` 在 `videoeditor.dll` 里命中：

```
常量    AES_SBOX_FIPS197 @ 0x353BD10      AES_INV_SBOX @ 0x353BE10
库指纹  CryptoPP / Rijndael_Info / CTR_ModePolicy / GCM_Base
指令    AESENC 簇 12 处
```

日志与函数名字符串（原样）：

```
[DRAFT_IO_MANAGER] IOManagerPrivate::tryDecrypt: decrypt fail, may be raw content, path: {}
[DRAFT_IO_MANAGER] IOManagerPrivate::decryptKV2: file: {}, is not crypted by KV2
[Business]: read_encode_string error, because encrypt error!
VipDraft::from_parcel_reader, decrypt failed, {}
VipDraft::to_parcel_writer, encrypt failed, {}
high_aes_general_v40s / high_aes_general_v41s / aip_high_aes_general_v43s_jm
VerifyBusinessAttachmentSecurity / verifyBusinessAttachmentSecurity
D:\j\workspace\lv-window-Release@2\jianying_build\CPM_current\videoeditor\lyra\trash_src\business\internal\serialize\vip_draft_serialize.cpp
```

由此可得流程轮廓：`IOManager` 先按 KV2 密钥库判定是否加密 → 走版本化 AES 实现（`high_aes_general_v40s/v41s/v43s` 是三套密文格式版本）→ 结果以 parcel 写入。密文外壳实测为单行 Base64（`draft_reader.py` 判定 `base64-envelope`），熵接近 8。

本仓库到「识别与分类」为止：`jianying/draft_reader.py` 能判定明文/密文并给出壳特征，不解密、不提密钥。

### 1.7 剪映侧复核命令

```bash
python tools/pe_info.py <...>/videoeditor.dll
python tools/rtti_dump.py <...>/videoeditor.dll --json reports/rtti_jy_veditor.json
python tools/rtti_report.py reports/rtti_jy_veditor.json --md reports/rtti_jy_veditor.md
python tools/api_surface.py reports/rtti_jy_veditor.json --md reports/api_jy_lyra.md --ns lyra
python tools/src_tree.py <...>/videoeditor.dll --out reports/src_jy_veditor --root jianying_build
python tools/find_crypto.py <...>/videoeditor.dll
python jianying/command_table.py <...>/app-server.mjs --json reports/commands_jy.json
python jianying/draft_reader.py <草稿目录> --json reports/draft_plain.json
```

---

## 二、DaVinci Resolve 21.2

### 2.1 二进制画像

| 目标 | 大小 | 链接器 | PDB 路径（关键） |
| --- | ---: | --- | --- |
| `FairlightPage.dll` | 31.77MB | 14.44（VS2022 17.14） | `C:\jenkins\workspace\fairlight\Fairlight\Tests\FairlightBridge\build\x64\release\release\FairlightPage.pdb` |
| `fusionscript.dll` | 3.55MB | 14.44 | `C:\jenkins\workspace\fusion\Fusion\Projects\vc17\Lite\fusionscript.pdb` |
| `fusiongraphics.dll` | 3.47MB | 14.44 | `C:\jenkins\workspace\fusion\Fusion\Projects\vc17\Lite\fusiongraphics.pdb` |
| `Resolve.exe` | 581MB | — | 251 万条唯一串，网络面 961 / 加密面 1,742 / GPU 面 13,134 |

结论三条：
1. **Jenkins + VS2022**，Fusion 走 `Projects\vc17\Lite` —— "Lite" 是 Resolve 内嵌的 Fusion 构建档位。
2. Fairlight 有独立的 `Tests\FairlightBridge` 目录 → 音频桥有自动化测试工程。
3. `Resolve.exe` 里 OpenSSL + Windows CNG 两套加密栈并存（`EVP_*` 与 `BCrypt*` 同时在），AES S-box 命中。

### 2.2 `.drp` 工程包：结构、CRC、可重打包（`drp_tool.py`）

实测 `Fuse.drp`（29,564 字节）：

| 成员 | 原始 | 压缩后 | CRC32 |
| --- | ---: | ---: | --- |
| `project.xml` | 8,149 | 3,775 | `fd1cfb51` |
| `MediaPool/Master/MpFolder.xml` | 171,466 | 10,950 | `0628ff1b` |
| `SeqContainer/c9dd78a8-….xml` | 24,124 | 13,025 | `68c4faea` |
| `Gallery.xml` | 8,917 | 1,216 | — |

压缩比 21:1（171KB→11KB），因为 XML 里全是重复标签名，适合 deflate。

### 2.3 时间轴解析（`drp_tool.py seq`）

```
容器 c9dd78a8-594a-4198-9c9b-2d9138040406
├─ 轨道 type=0 sub=0  片段 1
│    └─ [Sm2TiVideoClip] Fusion Title  start=86400  duration=120  composition=yes
└─ 轨道 type=1 sub=0  片段 0
```

`start=86400` / `duration=120` 是**帧号**；86400 帧 @24fps = 3600 秒 = `01:00:00:00`，与达芬奇时间线起点的惯例一致（首帧不从 0 计）。这条实测坐实了「达芬奇时间轴带基线偏移」的判断。

解析器没有用 XML 库：`SeqContainer` 的 XML 里混着裸控制字节，`ElementTree` 直接拒收，改成按标签切块取字段（`_tag_text` / `re.split`），稳健且不做格式猜测。

### 2.4 脚本 API：16 个类 / 530 个方法（`pyi_to_md.py`）

`DaVinciResolveScript.pyi` 是官方随包类型存根，解析后直接成表（`reports/api_resolve.md`，74KB，每个方法带参数、返回类型、官方说明）。方法数分布：`TimelineItem` 110、`Timeline` 70、`Project` 67、`Resolve` 50、`MediaPoolItem` 49、`MediaPool` 32、`ProjectManager` 27、`Graph` 15。

### 2.5 达芬奇侧复核命令

```bash
python tools/pe_info.py "<...>/FairlightPage.dll"
python tools/src_tree.py "<...>/FairlightPage.dll" --out reports/src_dv_fairlight
python resolve/drp_tool.py info <x.drp>
python resolve/drp_tool.py seq  <x.drp> --json reports/drp_fuse_seq.json
python resolve/drp_tool.py dump <x.drp> --out dir
python resolve/pyi_to_md.py <...>/DaVinciResolveScript.pyi --md reports/api_resolve.md
```

`resolve/api_client.py` 是连活实例的客户端封装（走 `fusionscript` 桥），本仓库不生成本机实测数据（隔离副本没有首次初始化，`-nogui` 起不来）。

---

## 三、After Effects 27.0

本机没有 AE，`.aep` 解析器按公开的 RIFX 规格实现，并用自造样本跑通闭环（`rifx_parse.py --selftest` → `PASS`）：

```
RIFX | uint32 size | Egg! | chunk…
chunk = 4B 标识 + uint32 长度 + 数据（奇数补 1）
LIST  = 4B 子类型 + 嵌套 chunk
```

覆盖的 chunk：`head` `Fold` `Sfdr` `Item` `idta` `cdta` `Layr` `ldta` `tdgp` `tdsb` `tdsn` `tdmn` `tdbs` `tdb4` `cdat` `list` `lhd3` `ldat` `opti` `sspc` `CLRS` `shap`。自检样本输出的 `comp_count_hint=1`、`has_Egg=true` 说明走查路径可用。

---

## 四、这份仓库做什么、不做什么

**做**：字节级结构、类与接口面、协议结构、工程文件格式、加密实现的**识别**、可复现的解析工具。目标是把闭源软件的**数据可移植性**拿回来，让自有工具能读写这些工程。

**不做**：激活/授权绕过、密钥提取、密文解密、绕过账号或云服务控制。仓库里的加密部分只到「判定与分类」，不提供开口器。这条边界写进代码注释里，改代码的人一眼能看到。

其余交付（架构、工程格式设计、选型、路线图）在配套仓库 `ai-video-studio-research`。