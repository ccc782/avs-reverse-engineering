#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""把压缩过的 JS 包整理成可读代码（不还原变量名，只还原结构）。

sourcemap 只覆盖了一部分包；剩下的是 minified 单行代码。这个脚本做：
  - 安全的换行与缩进（识别字符串、模板串、正则、注释，不破坏内容）
  - 统计处理前后行数与字节数
学不到原始命名，但能得到「能读、能改、能跑」的源码形态，够做行为对照与二次实现。

用法:
    python js_beautify.py --install "<剪映安装根>" --out ui_src_beautified [--min-kb 1]
"""
import argparse
import io
import json
import os

PAIRS = {"(": ")", "[": "]", "{": "}"}
CLOSERS = set(")]}")


def beautify(src, indent="  ", width_limit=110):
    out = []
    depth = 0
    i, n = 0, len(src)
    line_len = 0
    # 状态机：string / template / regex / comment 内部不做结构处理
    state = None
    quote = ""

    def emit(text):
        nonlocal line_len
        out.append(text)
        line_len += len(text)

    def newline(force=False):
        nonlocal line_len
        if force or line_len > 0:
            out.append("\n" + indent * max(depth, 0))
            line_len = 0

    while i < n:
        c = src[i]
        nxt = src[i + 1] if i + 1 < n else ""

        if state == "line_comment":
            emit(c)
            if c == "\n":
                state = None
                newline()
            i += 1
            continue
        if state == "block_comment":
            emit(c)
            if c == "*" and nxt == "/":
                emit(nxt)
                i += 2
                state = None
                newline()
                continue
            i += 1
            continue
        if state in ("string", "template"):
            emit(c)
            if c == "\\":
                if i + 1 < n:
                    emit(src[i + 1])
                i += 2
                continue
            if state == "string" and c == quote:
                state = None
            elif state == "template" and c == "`":
                state = None
            i += 1
            continue
        if state == "regex":
            emit(c)
            if c == "\\":
                if i + 1 < n:
                    emit(src[i + 1])
                i += 2
                continue
            if c == "/":
                state = None
            i += 1
            continue

        # 普通代码区
        if c == "/" and nxt == "/":
            state = "line_comment"
            emit(c)
            i += 1
            continue
        if c == "/" and nxt == "*":
            state = "block_comment"
            emit(c)
            i += 1
            continue
        if c in "\"'":
            state, quote = "string", c
            emit(c)
            i += 1
            continue
        if c == "`":
            state = "template"
            emit(c)
            i += 1
            continue
        if c == "/" and out and out[-1] and out[-1][-1] in "(,=:[!&|?{};+-*%~^<>":
            state = "regex"          # 前一个字符表明这是正则字面量
            emit(c)
            i += 1
            continue

        if c == "{":
            emit(c)
            depth += 1
            newline(force=True)
            i += 1
            continue
        if c == "}":
            depth = max(0, depth - 1)
            newline(force=True)
            emit(c)
            if nxt not in (";", ",", ")", "]", "}"):
                newline(force=True)
            i += 1
            continue
        if c == ";":
            emit(c)
            newline(force=True)
            i += 1
            continue
        if c == "," and line_len > width_limit:
            emit(c)
            newline(force=True)
            i += 1
            continue
        if c == "\n":
            newline(force=True)
            i += 1
            continue
        if c in " \t":
            # 压缩代码里的多余空白丢掉，行首缩进由 newline 负责
            if line_len and not out[-1].endswith(("\n",)) and not out[-1].endswith(indent):
                emit(" ")
            i += 1
            continue
        emit(c)
        i += 1

    return "".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--install", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--min-kb", type=float, default=1.0)
    a = ap.parse_args()

    os.makedirs(a.out, exist_ok=True)
    done = []
    total_in = total_out = 0
    for base, dirs, files in os.walk(a.install):
        if "node_modules" in base:
            continue
        for f in files:
            if not f.lower().endswith((".js", ".mjs")):
                continue
            p = os.path.join(base, f)
            size = os.path.getsize(p)
            if size < a.min_kb * 1024:
                continue
            raw = io.open(p, encoding="utf-8", errors="replace").read()
            try:
                pretty = beautify(raw)
            except Exception:
                continue
            rel = os.path.relpath(p, a.install).replace("\\", "__")
            dest = os.path.join(a.out, rel + ".pretty.js")
            io.open(dest, "w", encoding="utf-8", newline="\n").write(pretty)
            done.append({"src": os.path.relpath(p, a.install), "bytes_in": size,
                         "bytes_out": len(pretty), "lines_out": pretty.count("\n") + 1})
            total_in += size
            total_out += len(pretty)

    json.dump({"files": len(done), "bytes_in": total_in, "bytes_out": total_out,
               "items": sorted(done, key=lambda x: -x["bytes_in"])},
              io.open(os.path.join(a.out, "INDEX.json"), "w", encoding="utf-8", newline="\n"),
              ensure_ascii=False, indent=2)
    print(f"整理 {len(done)} 个包：{total_in/1048576:.1f}MB -> {total_out/1048576:.1f}MB")
    for d in sorted(done, key=lambda x: -x["bytes_in"])[:6]:
        print(f"  {d['bytes_in']/1024:8.0f}KB -> {d['lines_out']:7d} 行  {d['src'][:70]}")


if __name__ == "__main__":
    main()