#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""剪映特效/转场/贴纸/文字/音频效果 五类资产清点与规格提取。

资产形态（实测）：
  包 = config.json + content.json + <name>.material + <name>.prefab（二进制，属性名可读）
       + xshader/*.xshader（着色器入口）
       + Library/ShaderData/<hash>/shaderGLES/*.frag|.vert
       + Library/ShaderData/<hash>/shaderMetal/*.frag|.vert     ← GLSL 与 MSL 双份源码
  文字/贴纸 = JS 模板包（template.js 是 Amaz ECS 引擎的运行时桥）

本脚本产出：分类清单、每个包的资产构成、材质/预制体里可读的属性名、着色器分后端计数、
模板 JS 规模、字体表、音频效果名（从 DLL 字符串与草稿材质类反推）。

用法:
    python fx_packs.py --install "<剪映安装根>" [--audio-dll <audioeffect.dll>] --out reports/jianying_fx_packs
"""
import argparse
import collections
import io
import json
import os
import re

# 五类资产在安装目录里的驻留点
CATEGORIES = {
    "混合/转场（MixMode）": ["Resources/MixMode"],
    "色度键/抠像混合": ["Resources/Chroma", "Resources/Chroma2", "Resources/mattingBlend",
                    "Resources/mattingBlendV2", "Resources/mattingBlendCloud"],
    "调色控件资源": ["Resources/Curves", "Resources/LogWheel", "Resources/PrimaryWheel", "Resources/lut"],
    "贴纸模板": ["Resources/template_sticker", "Resources/image_h5_sticker_publish"],
    "文字模板": ["Resources/aigc_text_template", "Resources/image_h5_text_template_publish",
             "Resources/image_h5_smart_text", "Resources/image_h5_smart_text_old"],
    "字体": ["Resources/Font"],
    "音频素材": ["Resources/notice_sound", "Resources/audiosami", "Resources/audio_metrics", "Resources/tts"],
}

PROP_RE = re.compile(rb"[A-Za-z_][A-Za-z0-9_]{3,40}")
# 二进制材质里出现的已知属性名（去掉噪声）
PROP_ALLOW = re.compile(r"^(input|output|blend|base|main|src|dst|uv|tex|alpha|color|intensity|"
                        r"progress|strength|radius|angle|offset|scale|width|height|time|frame|"
                        r"mix|mode|ratio|_|\w*(Tex|Texture|Map|Sheet|Material|Prefab|Entity|Renderer)\w*)$",
                        re.I)


def walk_files(root):
    for base, _, files in os.walk(root):
        for f in files:
            yield os.path.join(base, f)


def ascii_props(path, limit=64):
    """从二进制 material/prefab 里抠可读标识符（属性名、实体名、纹理槽）。"""
    try:
        data = open(path, "rb").read()
    except OSError:
        return []
    out, seen = [], set()
    for m in PROP_RE.finditer(data):
        s = m.group(0).decode("latin-1")
        if s in seen or not PROP_ALLOW.match(s):
            continue
        seen.add(s)
        out.append(s)
        if len(out) >= limit:
            break
    return out


def analyze_pack(packdir):
    files = list(walk_files(packdir))
    rel = [os.path.relpath(f, packdir).replace("\\", "/") for f in files]
    shaders = collections.Counter()
    props = []
    js = []
    sizes = 0
    for f, r in zip(files, rel):
        sizes += os.path.getsize(f)
        low = r.lower()
        if low.endswith((".frag", ".vert", ".xshader")):
            be = "metal" if "metal" in low else ("gles" if ("gles" in low or low.endswith((".frag", ".vert"))) else "xshader")
            shaders[be] += 1
        elif low.endswith(".js"):
            js.append({"file": r, "kb": round(os.path.getsize(f) / 1024, 1)})
        elif low.endswith((".material", ".prefab")):
            props += ascii_props(f)
    cfg = {}
    for name in ("config.json", "content.json"):
        p = os.path.join(packdir, name)
        if os.path.exists(p):
            try:
                cfg[name] = json.load(io.open(p, encoding="utf-8", errors="replace"))
            except Exception:
                cfg[name] = "parse-fail"
    return {"pack": os.path.basename(packdir), "kb": round(sizes / 1024, 1),
            "files": len(files), "shaders": dict(shaders),
            "props": sorted(set(props))[:40], "js": js[:6], "config": cfg}


def audio_effects(dll_path, strings_txt):
    """音频效果：优先从 audioeffect.dll 的字符串里认出效果名，其次用草稿材质类兜底。"""
    names = []
    if strings_txt and os.path.exists(strings_txt):
        for line in io.open(strings_txt, encoding="utf-8", errors="replace"):
            if re.search(r"(reverb|chorus|flanger|phaser|delay|echo|compressor|limiter|gate|eq|"
                         r"highpass|lowpass|pitch|vibrato|tremolo|distortion|denoise|dereverb)", line, re.I):
                names.append(line.strip())
    if dll_path and os.path.exists(dll_path):
        data = open(dll_path, "rb").read()
        for m in re.finditer(rb"[A-Za-z][A-Za-z0-9_]{4,30}", data):
            s = m.group(0).decode("latin-1")
            if re.search(r"(Reverb|Chorus|Flanger|Phaser|Delay|Compressor|Limiter|Equalizer|"
                         r"HighPass|LowPass|PitchShift|Vibrato|Tremolo|Distortion|Denoise|DeReverb)", s):
                names.append(s)
    return sorted(set(names))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--install", required=True)
    ap.add_argument("--audio-dll", default=None)
    ap.add_argument("--strings", default=None)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    inv = {}
    for cat, dirs in CATEGORIES.items():
        items = []
        for d in dirs:
            root = os.path.join(a.install, d.replace("/", os.sep))
            if not os.path.isdir(root):
                continue
            # 目录本身是包 vs 目录下每个子目录是包
            subs = [p for p in os.listdir(root) if os.path.isdir(os.path.join(root, p))]
            if any(os.path.exists(os.path.join(root, n)) for n in ("config.json", "content.json")):
                items.append({"dir": d, **analyze_pack(root), "role": "single-pack"})
            for s in subs:
                sp = os.path.join(root, s)
                if any(os.path.exists(os.path.join(sp, n))
                       for n in ("config.json", "content.json", "content.scene")):
                    items.append({"dir": f"{d}/{s}", **analyze_pack(sp), "role": "pack"})
                elif s.lower() in ("js", "library", "xshader"):
                    continue
                else:
                    items.append({"dir": f"{d}/{s}", "pack": s, "role": "asset-dir",
                                  "files": sum(1 for _ in walk_files(sp)),
                                  "kb": round(sum(os.path.getsize(f) for f in walk_files(sp)) / 1024, 1)})
        inv[cat] = items

    # MixMode 索引
    mix_index = []
    mi = os.path.join(a.install, "Resources", "MixMode", "MixMode.json")
    if os.path.exists(mi):
        j = json.load(io.open(mi, encoding="utf-8", errors="replace"))
        mix_index = j.get("resourceList", [])

    fx = audio_effects(a.audio_dll, a.strings)

    # 汇总
    md = ["# 剪映 特效 / 转场 / 贴纸 / 文字 / 音频效果 —— 资产清点与规格", ""]
    total_pack = sum(len(v) for v in inv.values())
    md += [f"- 五类资产条目：**{total_pack}**",
           f"- 混合模式索引（MixMode.json）：**{len(mix_index)}** 条",
           f"- 音频效果名命中：**{len(fx)}**", ""]

    for cat, items in inv.items():
        packs = [x for x in items if x.get("role") in ("pack", "single-pack")]
        shaders = collections.Counter()
        for p in packs:
            for k, v in (p.get("shaders") or {}).items():
                shaders[k] += v
        md += [f"## {cat}", "",
               f"- 条目 {len(items)}，其中可解析的包 {len(packs)}",
               "- 着色器分后端：" + ("，".join(f"{k} {v}" for k, v in shaders.items()) or "—"), "",
               "| 条目 | 体积 | 文件 | 着色器 | 模板 JS | 可读属性名（前 8） |",
               "| --- | ---: | ---: | --- | --- | --- |"]
        for p in items[:40]:
            sh = "，".join(f"{k}:{v}" for k, v in (p.get("shaders") or {}).items()) or "—"
            js = "，".join(f"{x['file'].split('/')[-1]} {x['kb']}KB" for x in (p.get("js") or [])) or "—"
            props = "，".join((p.get("props") or [])[:8]) or "—"
            md.append(f"| `{p['dir']}` | {p.get('kb', 0)}KB | {p.get('files', 0)} | {sh} | {js} | {props} |")
        md.append("")

    if mix_index:
        md += ["## 混合模式索引（前 10 条，含三段 ID）", "",
               "| nameId | effectId | resourceId | 资源目录 |", "| --- | --- | --- | --- |"]
        for r in mix_index[:10]:
            md.append(f"| `{r.get('nameId')}` | `{r.get('effectId')}` | `{r.get('resourceId')}` | `{r.get('path')}` |")
        md.append("")

    if fx:
        md += ["## 音频效果候选名（从 DLL 与音频模块字符串里提取）", "", "```"] + fx[:60] + ["```", ""]

    io.open(a.out + ".md", "w", encoding="utf-8", newline="\n").write("\n".join(md))
    json.dump({"categories": inv, "mixmode_index": mix_index, "audio_effect_names": fx},
              io.open(a.out + ".json", "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=2)
    print(f"五类条目 {total_pack} / MixMode {len(mix_index)} / 音频效果名 {len(fx)}")
    for cat, items in inv.items():
        packs = [x for x in items if x.get("role") in ("pack", "single-pack")]
        sh = collections.Counter()
        for p in packs:
            for k, v in (p.get("shaders") or {}).items():
                sh[k] += v
        print(f"  {cat:22s} 条目 {len(items):3d} 包 {len(packs):3d} 着色器 {dict(sh)}")


if __name__ == "__main__":
    main()