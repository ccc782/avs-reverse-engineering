# 剪映 / 达芬奇 / AE 代码级逆向工具集

对三款闭源视频软件的成品二进制做静态逆向，产出**可复现的脚本**与**真实数据**：类地图、接口面、源码树、工程格式解析器。目标是把工程文件的可移植性拿回来。

配套仓库：`ai-video-studio-research`（架构、工程格式设计、选型、路线图）。

**先读**：[`REVERSE_ENGINEERING.md`](REVERSE_ENGINEERING.md) —— 全部数字来自本仓库脚本对真机二进制的实跑。
**审阅结论**：[`AUDIT.md`](AUDIT.md) —— 本仓逐文件审计 + 两个仓库的交叉审计。

---

## 战果一览

| 目标 | 拿到的 | 工具 |
| --- | --- | --- |
| 剪映 `videoeditor.dll` | **15,041** 个 RTTI 类名 / 60 命名空间 / **770** 个 lyra 接口 / **1,391** 个源文件路径 / 199 条命令 / 加密实现证据链 | `rtti_dump` `api_surface` `src_tree` `find_crypto` `command_table` |
| 达芬奇 `Resolve.exe` + DLL | 251 万唯一串、OpenSSL+CNG 双加密栈、`.drp` 包结构与时间轴解析、**530** 个脚本 API | `strings_extract` `find_crypto` `drp_tool` `pyi_to_md` |
| AE `.aep` | RIFX chunk 走查器（自检 PASS） | `rifx_parse` |
| 剪映草稿 | 明文/密文自动识别 + 结构画像 | `draft_reader` |
| 剪映 AI 层 | **21** 项能力 / **567** 个 AI RPC / **45** 个端侧模型包 / **139** 个云服务 | `ai_surface` `ai_deep` `endpoint_scan` |
| 剪映 AI 层 | **21** 项能力 / **567** 个 AI RPC / **45** 个端侧模型包 / **139** 个云服务 | `ai_surface` `ai_deep` `endpoint_scan` |

## 目录

```
REVERSE_ENGINEERING.md      结论正文（数字 + 证据 + 复核命令）
tools/                      通用二进制工具
  pe_info.py                PE 头/节/链接器/PDB/Rich/版本/清单/导入
  rtti_dump.py              MSVC RTTI 类名提取
  rtti_report.py            类地图报告（命名空间聚类 + 能力面命中）
  api_surface.py            从 Req/Resp 结构体反推接口清单
  src_tree.py               回收源码树（__FILE__ 残留路径）
  strings_extract.py        分类字符串提取
  find_crypto.py            算法常量 + 库指纹 + 指令特征
  check_words.py            交付文档用词扫描（递归）
jianying/
  draft_reader.py           草稿读取（明文解剖 / 密文壳特征）
  command_table.py          原生编辑命令表抽取（含模型安全子集）
  ai_surface.py             AI 能力矩阵：端侧/云侧/双路 × 类名/命令/端点证据
  ai_deep.py                AI 深挖：567 个 RPC / 流水线目录 / 模型规格 / 云服务目录
  endpoint_scan.py          18 个模块的 URL / 主机 / 路径扫描
  ai_surface.py             AI 能力矩阵：端侧/云侧/双路 × 类名/命令/端点证据
  ai_deep.py                AI 深挖：567 个 RPC / 流水线目录 / 模型规格 / 云服务目录
  endpoint_scan.py          18 个模块的 URL / 主机 / 路径扫描
resolve/
  drp_tool.py               .drp 拆包/解剖/重打包/差异/时间轴解析
  pyi_to_md.py              .pyi → 接口清单
  api_client.py             连活实例的脚本客户端
ae/
  rifx_parse.py             .aep RIFX 走查（带自检）
reports/                    实跑产物（json + md），INDEX.md 列出全部

> 口径提示：`src_tree.py` 抓的是 `__FILE__` 残留路径，跨模块日志里会带进别的模块的 .cpp，回收数量是「提及量」不是「文件数下限」；`rtti_dump.py` 统计的是类型描述符出现次数去重后的类名，模板实例化会重复计数一次。
```

## 环境

```bash
python -m pip install pefile capstone
python --version   # 3.10+
```

## 快速上手

```bash
# 1) 看一个 DLL 的家底
python tools/pe_info.py "C:\...\videoeditor.dll"

# 2) 抽类地图 + 反推接口
python tools/rtti_dump.py "C:\...\videoeditor.dll" --json reports/rtti_jy_veditor.json
python tools/rtti_report.py reports/rtti_jy_veditor.json --md reports/rtti_jy_veditor.md
python tools/api_surface.py reports/rtti_jy_veditor.json --md reports/api_jy_lyra.md --ns lyra

# 3) 回收源码树
python tools/src_tree.py "C:\...\videoeditor.dll" --out reports/src_jy_veditor --root jianying_build

# 4) 加密实现识别
python tools/find_crypto.py "C:\...\videoeditor.dll"

# 5) 工程格式
python resolve/drp_tool.py info  some.drp
python resolve/drp_tool.py seq   some.drp --json out.json
python jianying/draft_reader.py  "<草稿目录>" --json out.json
python ae/rifx_parse.py --selftest
```

## 边界

仓库只做**结构与格式**的逆向：字节布局、类与接口面、协议结构、工程格式、加密实现的识别与分类。

不做：激活/授权绕过、密钥提取、密文解密、绕过账号或云服务控制。加密部分的代码只到「判定这是明文还是密文、密文用哪套格式」，不提供开口器。

## 目标版本

| 软件 | 版本 | 环境 |
| --- | --- | --- |
| 剪映专业版 | 11.7.0.14652 | 官方安装包解包到隔离目录，数据目录重定向 |
| DaVinci Resolve | 21.2 build 6 | `msiexec /a` 展开到隔离目录 |
| After Effects | 27.0 | 本机未装，按公开 RIFX 规格实现 + 自造样本自检 |

## 协议

工具与文档版权归仓库所有者。第三方项目按其自身协议引用（Crypto++、FFmpeg 等）。