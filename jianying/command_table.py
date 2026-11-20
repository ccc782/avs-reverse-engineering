#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从剪映的 Agent Runtime 里抽出原生编辑命令表。

剪映 11.x 的 `Resources\\canvas_agent\\runtime\\app-server.mjs` 里冻结了一份
按域组织的命令白名单（变量名 FN3），这是 C++ 内核 videoeditor.dll 对外暴露的
命令面在 JS 侧的镜像。本脚本把它解析成结构化 JSON 与 Markdown，不需要运行剪映。

用法:
    python command_table.py <app-server.mjs> [--json out.json] [--md out.md]
"""
import argparse
import json
import re
import sys

FN3_RE = re.compile(r"var\s+FN3\s*=\s*\{(.*?)\}\s*,\s*\w+\s*=\s*new\s+Set\(", re.S)
PAIR_RE = re.compile(r'(\w+)\s*:\s*\[([^\]]*)\]')
SAFE_RE = re.compile(r"Object\.freeze\(\[(.*?)\]\)", re.S)


def pick_safe_subset(src):
    """安全子集是模型可调命令的闭集，特征是元素都是 '域.动作' 形式。
    文件里有多个 Object.freeze([...])，取元素最长且带点的那个。"""
    best = []
    for m in SAFE_RE.finditer(src):
        items = re.findall(r'"([^"]+)"', m.group(1))
        dotted = [x for x in items if "." in x]
        if len(dotted) >= 3 and len(dotted) > len(best):
            best = dotted
    return best


def parse(mjs_path):
    src = open(mjs_path, encoding="utf-8", errors="replace").read()
    m = FN3_RE.search(src)
    if not m:
        raise SystemExit("没找到 FN3 命令表，可能版本不同或在别的 chunk 里")
    body = m.group(1)
    table = {}
    for domain, items in PAIR_RE.findall(body):
        cmds = re.findall(r'"([^"]+)"', items)
        if cmds:
            table[domain] = cmds
    safe = pick_safe_subset(src)
    return table, safe


def to_md(table, safe):
    total = sum(len(v) for v in table.values())
    lines = ["# 剪映原生编辑命令表（从 app-server.mjs 抽取）", "",
             f"- 域：**{len(table)}**",
             f"- 命令：**{total}**",
             f"- 模型可用安全子集：**{len(safe)}**", "",
             "| 域 | 命令数 | 命令 |", "| --- | ---: | --- |"]
    for d in sorted(table, key=lambda k: -len(table[k])):
        lines.append(f"| `{d}` | {len(table[d])} | " +
                     "<br>".join(f"`{c}`" for c in table[d]) + " |")
    lines += ["", "## 安全子集（模型只能调这些）", "", "```"]
    lines += safe
    lines += ["```"]
    return "\n".join(lines), total


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mjs")
    ap.add_argument("--json")
    ap.add_argument("--md")
    a = ap.parse_args()
    table, safe = parse(a.mjs)
    md, total = to_md(table, safe)
    if a.json:
        json.dump({"domains": table, "safe_subset": safe, "total": total},
                  open(a.json, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    if a.md:
        open(a.md, "w", encoding="utf-8").write(md)
    print(f"{len(table)} 个域 / {total} 条命令 / 安全子集 {len(safe)} 条")
    for d in sorted(table, key=lambda k: -len(table[k])):
        print(f"  {d:20s} {len(table[d])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())