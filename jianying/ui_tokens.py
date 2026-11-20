#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""剪映 UI 设计令牌提取：从 CSS 资产里还原调色板、字号阶梯、圆角、间距、组件名。

剪映的界面分三块：C++/Qt 自绘的时间轴与主窗、Lynx 页面（JS 打包）、CEF 里的
React 画布（AIGC 页面）。后两块的设计系统全在 CSS 里，且用了 CSS 自定义属性
（`--studio-*`），等于把令牌表直接交给了我们。

用法:
    python ui_tokens.py --install "<剪映安装根>" --out reports/ui_jianying
"""
import argparse
import collections
import io
import json
import os
import re

VAR_DEF = re.compile(r"(--[\w-]+)\s*:\s*([^;}]+)")
HEX = re.compile(r"#([0-9a-fA-F]{3,8})\b")
RGBA = re.compile(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*([\d.]+)\s*)?\)")
HSLA = re.compile(r"hsla?\(\s*[\d.]+\s*,\s*[\d.]+%\s*,\s*[\d.]+%\s*(?:,\s*([\d.]+)\s*)?\)")
FONT_SIZE = re.compile(r"font-size\s*:\s*(\d+(?:\.\d+)?)px")
LINE_HEIGHT = re.compile(r"line-height\s*:\s*(\d+(?:\.\d+)?)")
RADIUS = re.compile(r"border-radius\s*:\s*([\d.]+)px")
SPACING = re.compile(r"(?:gap|padding|margin)\s*:\s*([^;}]+)")
FONT_FAMILY = re.compile(r"font-family\s*:\s*([^;}]+)")
CLASS = re.compile(r"\.([a-zA-Z][\w-]{2,40})[-_][A-Za-z0-9_]{4,8}\b")
BLUR = re.compile(r"backdrop-filter\s*:\s*blur\((\d+)px\)")
ANIM = re.compile(r"cubic-bezier\(([^)]+)\)")


def scan_css(paths):
    tokens = collections.defaultdict(collections.Counter)
    colors = collections.Counter()
    fonts, sizes, radii, blurs, easing = collections.Counter(), collections.Counter(), \
        collections.Counter(), collections.Counter(), collections.Counter()
    components = collections.Counter()
    for p in paths:
        try:
            t = io.open(p, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        for name, val in VAR_DEF.findall(t):
            tokens[name][val.strip()[:60]] += 1
        for m in HEX.findall(t):
            if len(m) in (6, 3):
                colors["#" + m.lower()] += 1
        for r, g, b, a in RGBA.findall(t):
            colors[f"rgba({r},{g},{b},{a or '1'})"] += 1
        for a in HSLA.findall(t):
            colors[f"hsla(…, {a or '1'})"] += 1
        for x in FONT_SIZE.findall(t):
            sizes[f"{x}px"] += 1
        for x in FONT_FAMILY.findall(t):
            fonts[x.strip()[:60]] += 1
        for x in RADIUS.findall(t):
            radii[f"{x}px"] += 1
        for x in BLUR.findall(t):
            blurs[f"{x}px"] += 1
        for x in ANIM.findall(t):
            easing[x.replace(" ", "")] += 1
        for c in CLASS.findall(t):
            components[c] += 1
    return {"tokens": {k: dict(v.most_common(3)) for k, v in tokens.items()},
            "colors": dict(colors.most_common(40)),
            "font_sizes": dict(sizes.most_common(20)),
            "font_families": dict(fonts.most_common(8)),
            "radii": dict(radii.most_common(15)),
            "blur": dict(blurs.most_common(8)),
            "easing": dict(easing.most_common(8)),
            "components": dict(components.most_common(40))}


def fingerprint(paths):
    """从 JS 包里认框架（React / react-flow / lv- 组件库）。"""
    hits = collections.Counter()
    keys = {"react-flow": "react-flow", "React": "react", "__REACT": "react",
            "lv-modal": "lv- 组件库", "lv-btn": "lv- 组件库", "lynx": "Lynx",
            "preact": "preact", "vue": "vue", "tailwind": "tailwind", "zustand": "zustand",
            "immer": "immer", "fabric": "fabric.js", "konva": "konva"}
    scanned = 0
    for p in paths:
        if not p.lower().endswith((".js", ".mjs", ".cjs")):
            continue
        if os.path.getsize(p) > 8 * 1024 * 1024:
            continue
        try:
            t = io.open(p, encoding="utf-8", errors="replace").read(400000)
        except OSError:
            continue
        scanned += 1
        for k, label in keys.items():
            if k in t:
                hits[label] += 1
    return {"scanned": scanned, "hits": dict(hits.most_common())}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--install", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    css, js, qml, svg = [], [], [], []
    for base, _, files in os.walk(a.install):
        for f in files:
            p = os.path.join(base, f)
            low = f.lower()
            if low.endswith(".css"):
                css.append(p)
            elif low.endswith((".js", ".mjs", ".cjs")):
                js.append(p)
            elif low.endswith(".qml"):
                qml.append(p)
            elif low.endswith(".svg"):
                svg.append(p)

    r = scan_css(css)
    r["fingerprint"] = fingerprint(js)
    r["counts"] = {"css": len(css), "js": len(js), "qml": len(qml), "svg": len(svg),
                   "css_mb": round(sum(os.path.getsize(p) for p in css) / 1048576, 2)}

    md = ["# 剪映 UI 设计系统（从 CSS / JS 资产还原）", "",
          f"- 资产：CSS **{r['counts']['css']}** 个（{r['counts']['css_mb']} MB）/ JS **{r['counts']['js']}** / "
          f"QML **{r['counts']['qml']}** / SVG **{r['counts']['svg']}**",
          f"- 技术指纹：{json.dumps(r['fingerprint']['hits'], ensure_ascii=False)}", "",
          "## 一、CSS 自定义属性（它的令牌表，直接可抄）", "",
          "| 令牌 | 主要取值 |", "| --- | --- |"]
    for k, v in sorted(r["tokens"].items()):
        vals = " / ".join(f"`{x}`" for x in v)
        md.append(f"| `{k}` | {vals} |")

    md += ["", "## 二、调色板（按出现频次）", "", "| 颜色 | 次数 |", "| --- | ---: |"]
    for k, v in r["colors"].items():
        md.append(f"| `{k}` | {v} |")

    md += ["", "## 三、字号阶梯 / 行高 / 圆角 / 模糊 / 缓动", "",
           "| 类目 | 取值 |", "| --- | --- |"]
    for label, key in (("字号", "font_sizes"), ("圆角", "radii"), ("背景模糊", "blur"), ("缓动曲线", "easing")):
        vals = " / ".join(f"`{k}`({v})" for k, v in r[key].items())
        md.append(f"| {label} | {vals} |")
    md.append("| 字体族 | " + " / ".join(f"`{k[:50]}`" for k in r["font_families"]) + " |")

    md += ["", "## 四、组件名（去哈希后的类名，反映界面结构）", "", "```"]
    md += [f"{k}  x{v}" for k, v in r["components"].items()]
    md += ["```"]

    io.open(a.out + ".md", "w", encoding="utf-8", newline="\n").write("\n".join(md))
    json.dump(r, io.open(a.out + ".json", "w", encoding="utf-8", newline="\n"),
              ensure_ascii=False, indent=2)
    print(f"CSS {len(css)} / 令牌 {len(r['tokens'])} / 颜色 {len(r['colors'])} / "
          f"字号档 {len(r['font_sizes'])} / 组件 {len(r['components'])}")


if __name__ == "__main__":
    main()