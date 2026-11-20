#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""从 JS 包里还原原始源码（sourcemap → sourcesContent）。

原理：构建产物末尾会带 `//# sourceMappingURL=...`，指向的 map 里若含
`sourcesContent`，那就是**压缩前的原文**。剪映的 Lynx/React 前端包就带了这一份。

支持三种 map 形态：
  1. 内联 data URI：`data:application/json;base64,...`
  2. 同名外部文件：`xxx.js.map`
  3. 外部路径：`map/xxx.map`

用法:
    python sourcemap_extract.py --install "<剪映安装根>" --out ui_src [--include-node-modules]
产物:
    <out>/<bundle名>/<原始相对路径>      还原出的源码
    <out>/INDEX.json                    包 → 文件数 / 语言分布 / 字节数
"""
import argparse
import base64
import collections
import hashlib
import io
import json
import os
import re
import sys
import urllib.parse

MAP_RE = re.compile(rb"sourceMappingURL=([^\s'\"*]+)")
EXT_LANG = {".ts": "TypeScript", ".tsx": "TSX", ".js": "JavaScript", ".jsx": "JSX",
            ".css": "CSS", ".scss": "SCSS", ".less": "LESS", ".json": "JSON",
            ".vue": "Vue", ".mjs": "ESM", ".cjs": "CJS", ".html": "HTML"}


def safe_rel(name):
    """把 webpack:// 或绝对路径统一成可落盘的相对路径，防目录穿越。"""
    n = name.replace("\\", "/")
    n = re.sub(r"^webpack://[^/]*/", "", n)
    n = re.sub(r"^\./", "", n)
    n = re.sub(r"^/+", "", n)
    parts = [p for p in n.split("/") if p not in ("", ".", "..")]
    return "/".join(parts) or "unnamed"


def load_map(js_path, tail_bytes=8192):
    """返回 (map_dict, 来源描述) 或 (None, 原因)。"""
    try:
        with open(js_path, "rb") as f:
            f.seek(max(0, os.path.getsize(js_path) - tail_bytes))
            tail = f.read()
    except OSError as e:
        return None, f"读失败 {e}"
    m = MAP_RE.search(tail)
    if not m:
        return None, "无 sourceMappingURL"
    url = m.group(1).decode("utf-8", "replace")
    if url.startswith("data:"):
        try:
            b64 = url.split(",", 1)[1]
            raw = base64.b64decode(b64 + "=" * (-len(b64) % 4))
            return json.loads(raw), "内联 base64"
        except Exception as e:
            return None, f"内联解析失败 {e}"
    # 外部文件
    cand = os.path.join(os.path.dirname(js_path), urllib.parse.unquote(url))
    if not os.path.exists(cand) and not url.lower().endswith(".map"):
        cand2 = cand + ".map"
        cand = cand2 if os.path.exists(cand2) else cand
    if not os.path.exists(cand):
        return None, f"map 不存在 {url}"
    try:
        return json.load(io.open(cand, encoding="utf-8", errors="replace")), "外部 map"
    except Exception as e:
        return None, f"map 解析失败 {e}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--install", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--include-node-modules", action="store_true")
    ap.add_argument("--max-mb", type=float, default=64.0, help="单个 map 上限")
    a = ap.parse_args()

    os.makedirs(a.out, exist_ok=True)
    bundles = []
    for base, dirs, files in os.walk(a.install):
        if not a.include_node_modules and "node_modules" in base:
            continue
        for f in files:
            if f.lower().endswith((".js", ".mjs", ".cjs")):
                bundles.append(os.path.join(base, f))

    index = []
    seen_hash = {}
    total_files = total_bytes = 0
    reasons = collections.Counter()

    for js in bundles:
        m, why = load_map(js)
        if m is None:
            reasons[why.split(" ")[0]] += 1
            continue
        contents = m.get("sourcesContent") or []
        sources = m.get("sources") or []
        if not contents:
            reasons["map 无 sourcesContent"] += 1
            continue
        bundle_name = os.path.splitext(os.path.basename(js))[0][:60]
        outdir = os.path.join(a.out, bundle_name)
        wrote, skipped, langs = 0, 0, collections.Counter()
        for src, content in zip(sources, contents):
            if content is None:
                skipped += 1
                continue
            rel = safe_rel(src)
            ext = os.path.splitext(rel)[1].lower()
            langs[EXT_LANG.get(ext, ext or "(无后缀)")] += 1
            h = hashlib.sha256(content.encode("utf-8", "replace")).hexdigest()
            if h in seen_hash:          # 同一份源码被多个包打包，只留一份
                skipped += 1
                continue
            seen_hash[h] = True
            dest = os.path.join(outdir, rel)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with io.open(dest, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(content)
            wrote += 1
            total_bytes += len(content.encode("utf-8", "replace"))
        total_files += wrote
        index.append({"bundle": bundle_name, "bundle_path": os.path.relpath(js, a.install),
                      "map_source": why, "sources": len(sources), "written": wrote,
                      "skipped_dup_or_null": skipped, "languages": dict(langs)})

    json.dump({"total_written": total_files, "total_bytes": total_bytes,
               "bundles_with_sourcemap": len(index), "skip_reasons": dict(reasons),
               "bundles": index},
              io.open(os.path.join(a.out, "INDEX.json"), "w", encoding="utf-8", newline="\n"),
              ensure_ascii=False, indent=2)

    print(f"扫 {len(bundles)} 个 JS 包；带可用 sourcemap 的 {len(index)} 个")
    print(f"还原源码 {total_files} 个文件 / {total_bytes/1048576:.1f} MB")
    if reasons:
        print("跳过原因：" + "，".join(f"{k} {v}" for k, v in reasons.most_common(6)))
    top = sorted(index, key=lambda x: -x["written"])[:10]
    for b in top:
        print(f"  {b['written']:5d} 文件  {b['bundle'][:48]:48s} {b['languages']}")


if __name__ == "__main__":
    main()