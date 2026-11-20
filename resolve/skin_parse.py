#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""解析 Fusion 皮肤包（.fuskin 是 ZIP，内含 .skin 文本定义 + PNG 资产）。

.skin 是 Fusion 的自研声明式皮肤语言：
    颜色名 = { R, G, B [, A] }
    Control = Category { Layout = { HGroup { ... } } }
    尺寸常量 = 132
本脚本抽出三件事：颜色令牌表、控件尺寸指标、控件类别树，用于抄它的设计系统。

用法:
    python skin_parse.py <Fusion.fuskin> --out reports/ui_resolve_skin
"""
import argparse
import collections
import io
import json
import os
import re
import zipfile

COLOR_RE = re.compile(r"^\s*(\w+)\s*=\s*\{\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})\s*(?:,\s*(\d{1,3})\s*)?\}\s*$", re.M)
ALIAS_RE = re.compile(r"^\s*(\w+)\s*=\s*\{\s*(\w+)\s*\}\s*$", re.M)
NUM_RE = re.compile(r"^\s*(\w+)\s*=\s*(\d{1,4})\s*$", re.M)
CATEGORY_RE = re.compile(r"^\s*(\w+)\s*=\s*Category\s*\{", re.M)
SKIN_ID_RE = re.compile(r'ID\s*=\s*"([^"]+)"')
SKIN_NAME_RE = re.compile(r'Name\s*=\s*"([^"]+)"')


def parse_skin(text):
    colors = {}
    for name, r, g, b, a in COLOR_RE.findall(text):
        colors[name] = {"rgb": [int(r), int(g), int(b)],
                        "a": int(a) if a else 255,
                        "hex": "#%02x%02x%02x" % (int(r), int(g), int(b))}
    aliases = {k: v for k, v in ALIAS_RE.findall(text)}
    metrics = {k: int(v) for k, v in NUM_RE.findall(text)}
    categories = [m for m in CATEGORY_RE.findall(text)]
    idm, namem = SKIN_ID_RE.search(text), SKIN_NAME_RE.search(text)
    return {
        "id": idm.group(1) if idm else None,
        "name": namem.group(1) if namem else None,
        "colors": colors,
        "aliases": aliases,
        "metrics": metrics,
        "categories": categories,
        "bytes": len(text),
    }


def inventory(z):
    names = z.namelist()
    ext = collections.Counter(os.path.splitext(n)[1].lower() for n in names)
    top = collections.Counter(n.split("/")[0] for n in names)
    states = collections.Counter()
    for n in names:
        base = os.path.basename(n).lower()
        for st in ("hover", "pressed", "disabled", "selected", "active", "focus", "mask", "dark", "light"):
            if st in base:
                states[st] += 1
    hidpi = sum(1 for n in names if "@2x" in n or "@3x" in n)
    return {"entries": len(names), "ext": dict(ext), "top_dirs": dict(top.most_common(20)),
            "state_assets": dict(states.most_common(12)), "hidpi_assets": hidpi}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("fuskin")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    z = zipfile.ZipFile(a.fuskin)
    inv = inventory(z)
    skins = {}
    for n in z.namelist():
        if n.lower().endswith(".skin"):
            skins[n] = parse_skin(z.read(n).decode("utf-8", "replace"))

    md = ["# Fusion 皮肤包解剖（DaVinci Resolve 21.2 内嵌 Fusion）", "",
          f"- 包体：`{os.path.basename(a.fuskin)}`，{os.path.getsize(a.fuskin)/1024/1024:.1f} MB",
          f"- 条目：**{inv['entries']}**（PNG {inv['ext'].get('.png',0)} / skin {inv['ext'].get('.skin',0)} / 其它 {inv['entries']-inv['ext'].get('.png',0)-inv['ext'].get('.skin',0)}）",
          f"- HiDPI 变体（@2x/@3x）：**{inv['hidpi_assets']}** 个，占 {inv['hidpi_assets']/max(1,inv['entries'])*100:.0f}%",
          ""]

    md += ["## 一、顶层分区（资产按 UI 区域组织）", "", "| 分区 | 资产数 |", "| --- | ---: |"]
    for k, v in inv["top_dirs"].items():
        md.append(f"| `{k}` | {v} |")

    md += ["", "## 二、状态资产（交互态是切图，不是代码）", "", "| 状态 | 资产数 |", "| --- | ---: |"]
    for k, v in inv["state_assets"].items():
        md.append(f"| {k} | {v} |")

    for name, s in skins.items():
        md += ["", f"## 三、`{name}`（{s['id']} / {s['name']}，{s['bytes']//1024} KB）", ""]
        md += [f"- 颜色令牌：**{len(s['colors'])}** 个（含别名 {len(s['aliases'])}）",
               f"- 尺寸常量：**{len(s['metrics'])}** 个",
               f"- 控件类别：**{len(s['categories'])}** 个", ""]
        if s["colors"]:
            md += ["### 调色板（前 40）", "", "| 令牌 | HEX | RGBA |", "| --- | --- | --- |"]
            for k, v in list(s["colors"].items())[:40]:
                md.append(f"| `{k}` | `{v['hex']}` | {v['rgb']} / a={v['a']} |")
        if s["metrics"]:
            md += ["", "### 尺寸指标（前 40）", "", "| 常量 | 值 |", "| --- | ---: |"]
            for k, v in list(s["metrics"].items())[:40]:
                md.append(f"| `{k}` | {v} |")
        if s["categories"]:
            md += ["", "### 控件类别树", "", "```"]
            md += s["categories"][:120]
            md += ["```"]

    io.open(a.out + ".md", "w", encoding="utf-8", newline="\n").write("\n".join(md))
    json.dump({"inventory": inv, "skins": skins}, io.open(a.out + ".json", "w", encoding="utf-8", newline="\n"),
              ensure_ascii=False, indent=2)
    print(f"皮 {len(skins)} 套 / 条目 {inv['entries']} / HiDPI {inv['hidpi_assets']} / "
          f"颜色 {sum(len(s['colors']) for s in skins.values())} / 指标 {sum(len(s['metrics']) for s in skins.values())}")


if __name__ == "__main__":
    main()