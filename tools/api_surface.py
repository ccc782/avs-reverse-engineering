#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 RTTI 类名反推协议/接口面。

C++ 工程里请求/响应/参数/事件结构体的命名高度规律化：
    <方法名>ReqStruct / <方法名>RespStruct / <方法名>Param / <方法名>Args / <方法名>Event
把两侧配对，就得到一份「方法 → 请求体 → 响应体」的接口清单，不需要调试器。

用法:
    python api_surface.py <rtti.json> --md out.md [--ns lyra]
"""
import argparse
import collections
import json
import re

PAIRS = [
    ("ReqStruct", "RespStruct"),
    ("Request", "Response"),
    ("Req", "Resp"),
    ("Args", "Result"),
]
SUFFIX_OTHER = ["Param", "Params", "Struct", "Event", "Notify", "Info", "Data",
                "Config", "Option", "Options", "Desc", "Descriptor", "Node", "Hooker"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("json")
    ap.add_argument("--md", required=True)
    ap.add_argument("--ns", default=None, help="只看某个命名空间前缀")
    a = ap.parse_args()

    rows = json.load(open(a.json, encoding="utf-8"))
    names = [r["name"] for r in rows]
    if a.ns:
        names = [n for n in names if n.startswith(a.ns + "::")]

    # 按命名空间分组
    by_ns = collections.defaultdict(list)
    for n in names:
        parts = n.split("::")
        by_ns["::".join(parts[:-1]) if len(parts) > 1 else "(全局)"].append(parts[-1])

    md = [f"# 接口面反推：{a.json.split(chr(92))[-1]}", ""]
    if a.ns:
        md.append(f"- 限定命名空间：`{a.ns}`")
    md += [f"- 输入类名：{len(names)}", ""]

    total_methods = 0
    for ns in sorted(by_ns, key=lambda k: -len(by_ns[k])):
        simple = by_ns[ns]
        # 配对
        methods = {}
        for req_s, resp_s in PAIRS:
            for s in simple:
                if s.endswith(req_s):
                    base = s[: -len(req_s)]
                    methods.setdefault(base, {})["req"] = s
                    methods[base]["req_suffix"] = req_s
        for base, d in methods.items():
            rs = d.get("req_suffix", "")
            for req_s, resp_s in PAIRS:
                if rs == req_s and (base + resp_s) in simple:
                    d["resp"] = base + resp_s
        if not methods:
            continue
        total_methods += len([m for m in methods if m])
        md += [f"## `{ns}` — {len(methods)} 个方法（类总数 {len(simple)}）", "",
               "| 方法 | 请求结构 | 响应结构 | 其它同族结构 |",
               "| --- | --- | --- | --- |"]
        for base in sorted(m for m in methods if m):
            d = methods[base]
            family = [s for s in simple
                      if s.startswith(base) and s not in (d.get("req"), d.get("resp"))][:4]
            md.append("| `{}` | {} | {} | {} |".format(
                base,
                f"`{d['req']}`" if d.get("req") else "—",
                f"`{d['resp']}`" if d.get("resp") else "—",
                "<br>".join(f"`{x}`" for x in family) or "—"))
        md.append("")

    md.insert(3, f"- 反推出的方法总数：**{total_methods}**")
    open(a.md, "w", encoding="utf-8").write("\n".join(md))
    print(f"写出 {a.md}，方法 {total_methods} 个")


if __name__ == "__main__":
    main()