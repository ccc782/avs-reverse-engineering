#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""剪映草稿读取器：明文/密文自动识别 + 结构解剖。

它做什么：
  1. 判断 draft_content.json 是明文 JSON 还是被加密（单行 Base64 / 二进制壳）
  2. 明文：解析出 轨道 / 片段 / 素材池 / 关键帧 的结构画像与统计
  3. 密文：给出壳特征（首字节、字符集、长度、熵），不做解密
  4. 产出结构化 JSON 报告，可用于跨版本比对与自有格式移植

用法:
    python draft_reader.py <draft_dir_or_file> [--json out.json] [--sample 3]
"""
import argparse
import json
import math
import os
import re
import sys

B64_RE = re.compile(rb"^[A-Za-z0-9+/=\r\n]+$")


def entropy(b):
    if not b:
        return 0.0
    freq = [0] * 256
    for x in b:
        freq[x] += 1
    n = len(b)
    return round(-sum((c / n) * math.log2(c / n) for c in freq if c), 3)


def classify(path):
    raw = open(path, "rb").read()
    stripped = raw.lstrip()
    if stripped[:1] in (b"{", b"["):
        return "plaintext-json", raw
    if B64_RE.match(raw[:4096]) and len(raw.strip()) % 4 == 0:
        return "base64-envelope", raw
    return "binary-envelope", raw


def probe_envelope(raw):
    head = raw[:64]
    return {
        "size": len(raw),
        "entropy": entropy(raw[:65536]),
        "first_16_hex": head[:16].hex(),
        "printable_ratio": round(sum(1 for b in raw[:4096] if 32 <= b < 127) / max(1, len(raw[:4096])), 3),
        "looks_like_base64": bool(B64_RE.match(raw[:4096])),
    }


def summarize_segment(seg, idx, sample_n):
    keep = ["id", "material_id", "render_index", "speed", "volume", "visible",
            "track_render_index", "extra_material_refs"]
    d = {k: seg.get(k) for k in keep if k in seg}
    for tk in ("target_timerange", "source_timerange"):
        if isinstance(seg.get(tk), dict):
            d[tk] = seg[tk]
    clip = seg.get("clip") or {}
    if clip:
        d["clip"] = {k: clip.get(k) for k in ("alpha", "rotation", "scale", "transform", "flip") if k in clip}
    d["_keyframe_count"] = len(seg.get("common_keyframes") or [])
    return d if idx < sample_n else None


def analyze_draft(path, sample_n=3):
    kind, raw = classify(path)
    out = {"file": os.path.basename(path), "kind": kind}
    if kind != "plaintext-json":
        out["envelope"] = probe_envelope(raw)
        out["note"] = "密文/封装态：不解密，仅记录壳特征。剪映 6.0+ 由云端配置决定是否上锁。"
        return out

    doc = json.loads(raw.decode("utf-8"))
    out["top_keys"] = sorted(doc.keys())
    out["version"] = doc.get("version")
    out["new_version"] = doc.get("new_version")
    out["canvas"] = doc.get("canvas_config")
    out["fps"] = doc.get("fps")
    out["duration_us"] = doc.get("duration")
    out["platform"] = doc.get("platform")

    mats = doc.get("materials") or {}
    out["materials"] = {
        "classes": len(mats),
        "non_empty": {k: len(v) for k, v in mats.items() if isinstance(v, list) and v},
        "empty_classes": sorted(k for k, v in mats.items() if isinstance(v, list) and not v),
    }

    tracks = doc.get("tracks") or []
    out["tracks"] = []
    for t in tracks:
        segs = t.get("segments") or []
        out["tracks"].append({
            "id": t.get("id"),
            "type": t.get("type"),
            "attribute": t.get("attribute"),
            "flag": t.get("flag"),
            "segment_count": len(segs),
            "segments": [s for s in (summarize_segment(x, i, sample_n) for i, x in enumerate(segs)) if s],
        })

    # 时间连续性检查（主轨应当首尾相接）
    if out["tracks"]:
        main = out["tracks"][0]
        cursor = 0
        gaps = 0
        for s in (doc["tracks"][0].get("segments") or []):
            tr = s.get("target_timerange") or {}
            start, dur = tr.get("start", 0), tr.get("duration", 0)
            if start != cursor:
                gaps += 1
            cursor = start + dur
        main["contiguity_gaps"] = gaps
        main["track_end_us"] = cursor

    out["keyframes_top"] = {k: len(v) for k, v in (doc.get("keyframes") or {}).items() if isinstance(v, list)}
    out["config_keys"] = sorted((doc.get("config") or {}).keys())
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target")
    ap.add_argument("--json")
    ap.add_argument("--sample", type=int, default=3)
    a = ap.parse_args()

    t = a.target
    if os.path.isdir(t):
        cand = [os.path.join(t, n) for n in ("draft_content.json", "draft_info.json")]
        path = next((c for c in cand if os.path.exists(c)), None)
        if not path:
            print("目录里没有 draft_content.json / draft_info.json")
            return 1
    else:
        path = t

    r = analyze_draft(path, a.sample)
    text = json.dumps(r, ensure_ascii=False, indent=2)
    if a.json:
        open(a.json, "w", encoding="utf-8").write(text)
        print(f"{r['file']}: {r['kind']} -> {a.json}")
        if r["kind"] == "plaintext-json":
            print(f"  轨道 {len(r['tracks'])}，素材类 {r['materials']['classes']}，"
                  f"主轨片段 {r['tracks'][0]['segment_count'] if r['tracks'] else 0}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())