# 审计报告（反向仓）

审计对象：`avs-reverse-engineering` 全部 57 个文件 —— `tools/`（9 个）、`jianying/`（2 个）、`resolve/`（3 个）、`ae/`（1 个）、`reports/`（41 个产物 + INDEX）。
方法：干净克隆后逐个跑 `--help` / `--selftest` / 实数据；对正文数字做机器核对（`_audit/rev_claims.py`）；代码静态检查（编译、裸 except、硬编码路径、死代码）。

结论：**数据本身可信（每个数字都能用仓库里的脚本复现），但正文有 2 处数字写错、1 处统计口径未交代、若干处死代码与静默异常。已全部处置。**

---

## 一、高优先级（已修）

### H1　`api_surface.py` 产出过 1 行空方法名，正文却写 770

`lyra` 命名空间里有两个裸类 `ReqStruct` / `RespStruct`（没有方法名前缀），配对后产生一个空 base，表格多一行、计数多 1。

- 现象：`reports/api_jy_lyra.md` 有 771 个表行，正文写「770 个方法」——数字对不上表。
- 处置：`tools/api_surface.py` 在渲染与计数时过滤空 base（两处），重跑后 **770 / 770 一致**。

### H2　`.drp` 压缩比算错

正文写「压缩比 21:1（171KB→11KB）」。实际 `171466 / 10950 = 15.7:1`。算术错误，已改。

---

## 二、中优先级（已修 / 已标注）

| # | 位置 | 问题 | 处置 |
| --- | --- | --- | --- |
| M1 | `REVERSE_ENGINEERING.md` §1.4 | 写「`lyra` 命名空间下 3,420 个类」，实测 3,545 | 已改 3,545 |
| M2 | `resolve/drp_tool.py` | `_parse_xml_safe()` 是废弃路径（现在用结构化正则），死函数 | 已删 |
| M3 | `jianying/draft_reader.py` | 连续性检查默认 `tracks[0]` 是主轨，代码里没写这个假设 | 报告里加 `assumed_main_track: true` + 行内注释 |
| M4 | `tools/src_tree.py` | 回收数会被别的模块日志污染（跨模块 `__FILE__`） | README 加「口径提示」：这是「提及量」不是「文件数下限」 |
| M5 | `tools/rtti_dump.py` | 模板实例化会让同名类多次出现，`hits` 是出现次数 | 同上口径提示里说明 |
| M6 | `reports/INDEX.md` | 手工生成，重跑工具后与实际不同步 | 已在 README 说明它是快照；重生成命令见文件头 |

---

## 三、低优先级（记录）

| # | 项 | 说明 |
| --- | --- | --- |
| L1 | `tools/pe_info.py` 3 处 `except: pass` | 版本资源与清单解析容错用，吞掉异常后字段为空。可接受，但排障时看不到原因 |
| L2 | `tools/strings_extract.py` | `Resolve.exe`（581MB）跑一次约 1-2 分钟、峰值内存 ~1.5GB；`reports/*.txt` 达 91MB，已排除出仓库（`.gitignore`） |
| L3 | `jianying/draft_reader.py` 密文判定 | 用 Base64 字符集 + 长度 4 整除去判，边角情形（带 BOM、短文件）会误判成 `binary-envelope`；结论仍成立（非明文），只是分类标签粗 |
| L4 | `resolve/api_client.py` | 本机没能在隔离副本上跑通（缺首次初始化），只能做静态审阅；调用契约来自官方 README 与 `.pyi`，未见运行时验证 |
| L5 | `reports/api_jy_lyra.md`（84KB） | 表里 `RespStruct` 缺失的行不少（只声明了请求体），说明 RTTI 里没生成对应响应类型，不是抽取漏了 |

---

## 四、功能复测（干净克隆）

| 检查 | 结果 |
| --- | --- |
| 15 个 `.py` 编译 | 全部通过 |
| `ae/rifx_parse.py --selftest` | `PASS`（chunk 计数 `has_Egg=true`、`comp_count_hint=1`） |
| `resolve/drp_tool.py --help` / `info` / `seq` | 正常；`seq` 解析出 2 轨道、1 片段、`start=86400` `duration=120` |
| `jianying/command_table.py` | 18 域 / 199 条 / 安全子集 26 条 |
| `jianying/draft_reader.py` | 明文 `plaintext-json`（3 轨 / 46 素材类 / 95 片段）、密文 `base64-envelope` 判定稳定 |
| `tools/rtti_dump.py` + `rtti_report.py` | 15,041 类 / 60 命名空间，报告生成正常 |
| 硬编码绝对路径 | 0 处 |
| TODO / FIXME | 0 处 |

---

## 五、与正文数字的逐条核对

| 正文 | 实测 | 判定 |
| --- | --- | --- |
| 剪映 RTTI 15,041 类 | 15,041 | ✅ |
| 源码树 1,391 文件 / 313 目录 | 1,391 | ✅ |
| lyra 770 接口 | 770（修完空行后） | ✅ |
| lyra 3,420 类 | 3,545 | 已改 |
| 命令 199 条 / 26 安全子集 | 199 / 26 | ✅ |
| AESENC 12 处 | 12 | ✅ |
| Resolve 251 万唯一串 | 2,516,225 | ✅ |
| 网络 961 / 加密 1,742 / GPU 13,134 | 961 / 1,742 / 13,134 | ✅ |
| `.drp` 压缩比 21:1 | 15.7:1 | 已改 |
| 达芬奇 530 方法 / 16 类 | 530 / 16 | ✅ |
| Fairlight 2,064 类 | 2,064 | ✅ |

---

## 六、交叉审计（与研究仓对照）

详见 [`ai-video-studio-research/docs/AUDIT.md`](https://github.com/ccc782/ai-video-studio-research/blob/main/docs/AUDIT.md)。要点：

1. **研究仓的判断没有一条被本仓证据推翻。** 剪映非 Electron、`.drp` = ZIP(XML)、达芬奇脚本 API 规模、命令表结构，全部对得上。
2. **3 条口径按本仓实测收紧**：命令表 200+→199、达芬奇 22 类→16 类、加密「推断」→「实测」。
3. **唯一悬空项是 AE**：本仓没有真 `.aep` 样本，`rifx_parse.py` 只过了自造样本。研究仓 AE 那一章的 chunk 表仍是公开资料 + 第三方解析器，属未在真样本上验证的结论。
4. **本仓的两处数字错误说明同一件事**：工具能复现数据，但正文是手写的，手写就会飘。所以两仓都加了「正文数字必须能被脚本产出」这条。

---

## 七、修复清单（本次提交）

```
tools/api_surface.py            过滤空方法名（渲染 + 计数两处）
resolve/drp_tool.py             删死函数 _parse_xml_safe
jianying/draft_reader.py        假设显式化 assumed_main_track
REVERSE_ENGINEERING.md          lyra 3,545、压缩比 15.7:1
README.md                       补 check_words.py、补统计口径提示
reports/api_jy_lyra.md          重生成（770 行）
reports/api_jy_clipflow.md      重生成（4 个）
AUDIT.md                        本文件
```