#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 RTTI 类名清单变成可读的类地图报告（Markdown）。

输入：rtti_dump.py 产出的 json
输出：按命名空间聚类的类地图 + 关键词命中表

用法:
    python rtti_report.py <rtti.json> --md out.md [--top 40]
"""
import argparse
import collections
import json
import re

# 关心的能力面 → 关键词
KEYWORDS = {
    "草稿与工程": ["Draft", "Project", "Workspace", "Document"],
    "时间轴": ["Timeline", "Track", "Sequence", "TimeLine"],
    "片段与素材": ["Segment", "Clip", "Material", "Media", "Asset", "Source"],
    "命令与撤销": ["Command", "Undo", "Redo", "Transaction", "Patch", "Operation"],
    "加密与授权校验": ["Cipher", "Crypt", "Aes", "Rsa", "KeyStore", "Key", "Sign", "Auth", "License"],
    "特效与合成": ["Effect", "Filter", "Transition", "Composite", "Render", "Node", "Graph"],
    "AI 与算法": ["Matting", "Chroma", "Segment", "Infer", "Model", "Nn", "Onnx", "Track", "Beauty"],
    "编解码": ["Decoder", "Encoder", "Codec", "Ffmpeg", "Avc", "Hevc", "Hdr"],
    "Agent": ["Agent", "Lyra", "Skill", "Tool", "Llm", "Prompt"],
    "UI 与框架": ["View", "Widget", "Controller", "Panel", "Window", "Model"],
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("json")
    ap.add_argument("--md", required=True)
    ap.add_argument("--top", type=int, default=40)
    a = ap.parse_args()

    rows = json.load(open(a.json, encoding="utf-8"))
    names = [r["name"] for r in rows]

    ns = collections.Counter()
    for n in names:
        parts = n.split("::")
        ns["::".join(parts[:-1]) if len(parts) > 1 else "(全局)"] += 1

    lines = [f"# RTTI 类地图：{a.json.split(chr(92))[-1]}", "",
             f"- 类名总数：**{len(names)}**",
             f"- 命名空间数：**{len(ns)}**", "",
             "## 命名空间分布（前 {}）".format(a.top), "",
             "| 数量 | 命名空间 |", "| ---: | --- |"]
    for k, v in ns.most_common(a.top):
        lines.append(f"| {v} | `{k}` |")

    lines += ["", "## 能力面命中", "",
              "| 能力面 | 命中 | 样例 |", "| --- | ---: | --- |"]
    for cap, keys in KEYWORDS.items():
        hit = [n for n in names if any(k.lower() in n.lower() for k in keys)]
        sample = "<br>".join(f"`{n}`" for n in sorted(hit)[:8]) or "—"
        lines.append(f"| {cap} | {len(hit)} | {sample} |")

    lines += ["", "## 全量类名", "", "```"]
    lines += sorted(names)
    lines += ["```"]

    open(a.md, "w", encoding="utf-8").write("\n".join(lines))
    print(f"写出 {a.md}（{len(names)} 类，{len(ns)} 命名空间）")


if __name__ == "__main__":
    main()