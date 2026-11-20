#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把达芬奇官方的 DaVinciResolveScript.pyi 变成可直接用的接口清单。

.pyi 是官方随包的类型存根，等于一份免费的 API 契约。本脚本解析出
  「类 → 方法 → 签名 → 一句话说明」
并输出 Markdown 与 JSON，省掉手抄 530 个方法的力气。

用法:
    python pyi_to_md.py <DaVinciResolveScript.pyi> --md out.md --json out.json
"""
import argparse
import json
import re

CLASS_RE = re.compile(r"^class\s+(\w+)\s*[:(]")
DEF_RE = re.compile(r"^\tdef\s+(\w+)\((.*?)\)\s*(?:->\s*(.+?))?:\s*$")
DOC_RE = re.compile(r'^\t\t"""(.*?)"""', re.S)


def parse(path):
    lines = open(path, encoding="utf-8").read().splitlines()
    classes = {}
    cur = None
    i = 0
    while i < len(lines):
        line = lines[i]
        m = CLASS_RE.match(line)
        if m:
            cur = m.group(1)
            classes.setdefault(cur, {"methods": [], "doc": ""})
            i += 1
            continue
        m = DEF_RE.match(line)
        if m and cur:
            name, args, ret = m.group(1), m.group(2), (m.group(3) or "").strip()
            # 紧邻的 docstring
            doc = ""
            j = i + 1
            if j < len(lines) and lines[j].strip().startswith('"""'):
                buf = [lines[j]]
                while '"""' not in lines[j][lines[j].find('"""') + 3:] and j + 1 < len(lines):
                    j += 1
                    buf.append(lines[j])
                doc = " ".join(x.strip().strip('"').strip() for x in buf).strip()
            classes[cur]["methods"].append({
                "name": name,
                "args": re.sub(r"\s+", " ", args).strip(),
                "returns": ret,
                "doc": doc,
            })
            i = j + 1
            continue
        i += 1
    return classes


def to_md(classes, src_name):
    total = sum(len(c["methods"]) for c in classes.values())
    md = [f"# 达芬奇脚本 API 接口清单（解析自 {src_name}）", "",
          f"- 类：**{len(classes)}**",
          f"- 方法：**{total}**", "",
          "## 类一览", "", "| 类 | 方法数 |", "| --- | ---: |"]
    for k in sorted(classes, key=lambda x: -len(classes[x]["methods"])):
        if classes[k]["methods"]:
            md.append(f"| `{k}` | {len(classes[k]['methods'])} |")
    for k in sorted(classes):
        if not classes[k]["methods"]:
            continue
        md += ["", f"## `{k}`", "", "| 方法 | 签名 | 返回 | 说明 |", "| --- | --- | --- | --- |"]
        for m in classes[k]["methods"]:
            doc = (m["doc"] or "").replace("|", "\\|")[:160]
            md.append(f"| `{m['name']}` | `{m['args'][:120]}` | `{m['returns']}` | {doc} |")
    return "\n".join(md), total


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pyi")
    ap.add_argument("--md")
    ap.add_argument("--json")
    a = ap.parse_args()
    classes = parse(a.pyi)
    md, total = to_md(classes, a.pyi.split("\\")[-1])
    if a.md:
        open(a.md, "w", encoding="utf-8").write(md)
    if a.json:
        json.dump(classes, open(a.json, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"{len([c for c in classes.values() if c['methods']])} 个类 / {total} 个方法")


if __name__ == "__main__":
    main()