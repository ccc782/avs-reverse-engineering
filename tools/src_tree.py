#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从二进制里回收源码树。

Release 构建不会删掉 assert / 日志 / __FILE__ 里的源文件路径，
于是一份成品 DLL 就能反推出整个模块目录结构与文件名。

用法:
    python src_tree.py <binary> --out prefix [--root jianying_build]
产物:
    <prefix>.json  路径清单
    <prefix>.md    目录树 + 文件统计
"""
import argparse
import collections
import json
import os
import re
import sys

# Windows 绝对路径 + 常见源码后缀
PATH_RE = re.compile(
    rb"[A-Za-z]:\\[ -~]{4,300}?\.(?:cpp|cc|cxx|c|hpp|hh|h|mm|m|proto|idl|fbs|json|cu|metal|as|js|ts)"
)


def scan(path, root_filter=None):
    data = open(path, "rb").read()
    hits = collections.Counter()
    for m in PATH_RE.finditer(data):
        s = m.group(0).decode("utf-8", "replace").replace("\\\\", "\\")
        if root_filter and root_filter.lower() not in s.lower():
            continue
        hits[s] += 1
    return hits


def build_tree(paths, strip_prefix=None):
    tree = {}
    for p in paths:
        if strip_prefix and p.lower().startswith(strip_prefix.lower()):
            p = p[len(strip_prefix):].lstrip("\\")
        parts = p.split("\\")
        node = tree
        for seg in parts[:-1]:
            node = node.setdefault(seg + "\\", {})
        node.setdefault("__files__", []).append(parts[-1])
    return tree


def emit(node, depth=0, out=None):
    if out is None:
        out = []
    for k in sorted(node):
        if k == "__files__":
            for f in sorted(node[k]):
                out.append("  " * depth + f)
            continue
        sub = node[k]
        n = len(sub.get("__files__", []))
        out.append("  " * depth + k + (f"   [{n} 文件]" if n else ""))
        emit(sub, depth + 1, out)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("binary")
    ap.add_argument("--out", required=True)
    ap.add_argument("--root", default=None, help="只保留包含该前缀的路径")
    ap.add_argument("--strip", default=None, help="树里去掉该前缀")
    a = ap.parse_args()

    hits = scan(a.binary, a.root)
    paths = sorted(hits)
    json.dump({"file": os.path.basename(a.binary), "count": len(paths),
               "paths": {p: hits[p] for p in paths}},
              open(a.out + ".json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    exts = collections.Counter(os.path.splitext(p)[1].lower() for p in paths)
    dirs = collections.Counter(p.rsplit("\\", 1)[0] for p in paths)
    md = [f"# 源码树回收：{os.path.basename(a.binary)}", "",
          f"- 回收到的源文件名：**{len(paths)}**",
          f"- 目录数：**{len(dirs)}**", "",
          "## 后缀分布", "", "| 后缀 | 数量 |", "| --- | ---: |"]
    for e, c in exts.most_common():
        md.append(f"| `{e}` | {c} |")
    md += ["", "## 目录热度（前 40）", "", "| 文件数 | 目录 |", "| ---: | --- |"]
    for d, c in dirs.most_common(40):
        md.append(f"| {c} | `{d}` |")
    md += ["", "## 目录结构", "", "```"]
    md += emit(build_tree(paths, a.strip))
    md += ["```", "", "## 全量路径", "", "```"]
    md += paths
    md += ["```"]
    open(a.out + ".md", "w", encoding="utf-8").write("\n".join(md))
    print(f"{os.path.basename(a.binary)}: 回收 {len(paths)} 个源文件路径，{len(dirs)} 个目录 -> {a.out}.md")


if __name__ == "__main__":
    main()