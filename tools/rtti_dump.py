#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MSVC RTTI 类名提取。

未 strip 的 MSVC 二进制里，虚类的类型描述符固定形如 ".?AVClassName@@" / ".?AUStruct@@"，
UTF-8 直接可读。这是从成品二进制里拿到「类级结构」的最省力一刀。

用法:
    python rtti_dump.py <binary> [--json out.json] [--min 3]
"""
import argparse
import json
import re
import sys

# .?AV<name>@@ / .?AU<name>@@ ，名字里允许 namespace 的 @ 分隔
RTTI_RE = re.compile(rb"\.\?A[VU]([ -~]{2,240}?)@@")


def demangle(name: str):
    """把 a@b@c@@ 这种 MSVC 形式还原成 a::b::c。"""
    parts = [p for p in name.split("@") if p]
    if not parts:
        return name
    # 末段是类名，其余是外层作用域，反序
    return "::".join(reversed(parts))


def dump(path, min_len=3):
    data = open(path, "rb").read()
    found = {}
    for m in RTTI_RE.finditer(data):
        raw = m.group(1).decode("utf-8", "replace").strip("?")
        if len(raw) < min_len:
            continue
        cls = demangle(raw)
        if not re.match(r"^[\w:<>,\s\*&\[\]~]+$", cls):
            continue
        found[cls] = found.get(cls, 0) + 1
    return [{"name": k, "hits": v} for k, v in sorted(found.items())]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("binary")
    ap.add_argument("--json")
    ap.add_argument("--min", type=int, default=3)
    a = ap.parse_args()
    rows = dump(a.binary, a.min)
    if a.json:
        json.dump(rows, open(a.json, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print(f"{a.binary}: {len(rows)} 个 RTTI 类名 -> {a.json}")
    else:
        for r in rows:
            print(r["name"])
    return 0


if __name__ == "__main__":
    sys.exit(main())