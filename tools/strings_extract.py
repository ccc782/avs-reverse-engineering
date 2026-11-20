#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""分类字符串提取：ASCII + UTF-16LE，按用途打桶。

用法:
    python strings_extract.py <binary> --out prefix [--min 5] [--grep 关键字]
产物:
    <prefix>.json   分桶计数 + 每桶样本
    <prefix>.txt    全量原始串（去重）
"""
import argparse
import json
import re
import sys

BUCKETS = {
    "网络与协议": ["http://", "https://", "ws://", "/api/", "Content-Type", "User-Agent",
                   "Authorization", "X-TT-", "grpc", "websocket", "upload", "cdn"],
    "加密与许可": ["cipher", "encrypt", "decrypt", "aes", "rsa", "signature", "license",
                   "activat", "jypack", "key_store", "keystore", "trial", "expire"],
    "工程与格式键": ["draft", "timerange", "material", "segment", "track", "keyframe",
                     "effect", "transition", "canvas", "fps", "project", "sequence",
                     "schema", "version"],
    "命令与动作": ["set", "add", "delete", "update", "move", "split", "trim", "apply",
                   "validate", "plan", "patch", "batch"],
    "环境变量与开关": ["JY_", "RESOLVE_", "VIDEO_PLAYER_", "CUSTOM_AGENT_", "enabled",
                       "allow", "debug", "verbose", "log_level"],
    "AI 与模型": ["model", "onnx", "infer", "embedding", "clip", "vlm", "llm", "token",
                  "prompt", "embedding", "transcri", "asr", "tts"],
    "GPU 与渲染": ["cuda", "vulkan", "d3d", "shader", "texture", "render", "decoder",
                   "encoder", "nv12", "yuv", "prores", "dnxhr"],
    "错误与诊断": ["error", "fail", "exception", "assert", "crash", "dump", "invalid",
                   "missing", "conflict", "denied", "timeout"],
}

ASCII_RE = re.compile(rb"[\x20-\x7e]{5,300}")
UTF16_RE = re.compile(rb"(?:[\x20-\x7e]\x00){5,300}")


def extract(data, min_len=5):
    out = set()
    for m in ASCII_RE.finditer(data):
        s = m.group(0).decode("latin-1").strip()
        if len(s) >= min_len:
            out.add(s)
    for m in UTF16_RE.finditer(data):
        s = m.group(0).decode("utf-16-le").strip()
        if len(s) >= min_len:
            out.add(s)
    return out


def bucketize(strings):
    buckets = {k: [] for k in BUCKETS}
    buckets["未归类"] = []
    for s in strings:
        low = s.lower()
        hit = False
        for cat, keys in BUCKETS.items():
            if any(k.lower() in low for k in keys):
                buckets[cat].append(s)
                hit = True
        if not hit:
            buckets["未归类"].append(s)
    return buckets


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("binary")
    ap.add_argument("--out", required=True)
    ap.add_argument("--min", type=int, default=5)
    ap.add_argument("--grep")
    a = ap.parse_args()

    data = open(a.binary, "rb").read()
    strings = extract(data, a.min)
    buckets = bucketize(strings)

    summary = {
        "file": a.binary.split("\\")[-1],
        "size": len(data),
        "unique_strings": len(strings),
        "buckets": {k: {"count": len(v), "sample": v[:40]} for k, v in buckets.items()},
    }
    json.dump(summary, open(a.out + ".json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    with open(a.out + ".txt", "w", encoding="utf-8") as f:
        for s in sorted(strings):
            f.write(s + "\n")
    print(f"{summary['file']}: 唯一串 {len(strings)}，"
          + "，".join(f"{k}={v['count']}" for k, v in summary["buckets"].items() if v["count"]))
    if a.grep:
        kw = a.grep.lower()
        hits = [s for s in strings if kw in s.lower()]
        print(f"\n--grep {a.grep}: {len(hits)} 条")
        for s in hits[:60]:
            print("  " + s)
    return 0


if __name__ == "__main__":
    sys.exit(main())