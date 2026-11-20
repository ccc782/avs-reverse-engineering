#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""RIFX / AE 工程文件走查。

.aep = RIFF 的大端变体（RIFX），格式标识 `Egg!`：
    'RIFX' | uint32 size | 'Egg!' | chunk 序列
    chunk = 4 字节标识 + uint32 长度 + 数据（奇数补 1 字节）
    LIST   = 4 字节子类型 + 嵌套 chunk

本脚本走完整棵 chunk 树，输出结构树与关键字段（合成/图层/属性/关键帧计数），
用于在没有 AE 的机器上做静态审计。不执行、不求值表达式。

用法:
    python rifx_parse.py <file.aep> [--json out.json] [--tree]
    python rifx_parse.py --selftest
"""
import argparse
import json
import struct
import sys

KNOWN = {
    "head": "文件头/版本指纹",
    "Fold": "根文件夹", "Sfdr": "子文件夹", "Item": "工程项",
    "idta": "项标识(1文件夹/4合成/7素材)", "cdta": "合成参数",
    "Layr": "图层", "ldta": "图层参数", "tdgp": "属性组",
    "tdsb": "属性组 flags", "tdsn": "属性组名", "tdmn": "匹配名",
    "tdbs": "属性定义", "tdb4": "属性细节", "cdat": "静态值",
    "list": "关键帧容器", "lhd3": "关键帧头", "ldat": "关键帧数据",
    "opti": "素材信息", "sspc": "素材尺寸", "CLRS": "色彩配置",
    "shap": "形状", "shph": "形状路径", "btdk": "特殊块",
    "Egg!": "AEP 根",
}


def parse_chunks(buf, start, end, depth=0, out=None, max_depth=64):
    if out is None:
        out = []
    pos = start
    while pos + 8 <= end:
        cid = buf[pos:pos + 4]
        try:
            size = struct.unpack(">I", buf[pos + 4:pos + 8])[0]
        except struct.error:
            break
        data_start = pos + 8
        data_end = data_start + size
        if size < 0 or data_end > end:
            break
        name = cid.decode("latin-1")
        node = {"id": name, "offset": pos, "size": size, "depth": depth,
                "meaning": KNOWN.get(name.strip("\x00"), "")}
        if name == "LIST" and depth < max_depth:
            sub = buf[data_start:data_start + 4].decode("latin-1")
            node["list_type"] = sub
            node["children"] = parse_chunks(buf, data_start + 4, data_end, depth + 1,
                                            None, max_depth)
        out.append(node)
        pos = data_end + (size & 1)
    return out


def walk(nodes, fn):
    for n in nodes:
        fn(n)
        if "children" in n:
            walk(n["children"], fn)


def summarize(tree):
    from collections import Counter
    c = Counter()
    walk(tree, lambda n: c.update([n["id"]]))

    def field(buf, name, fmt, off=0):
        try:
            p = buf.find(name.encode("latin-1"))
            if p < 0:
                return None
            return struct.unpack(fmt, buf[p + 8 + off:p + 8 + off + struct.calcsize(fmt)])[0]
        except Exception:
            return None

    return {
        "chunk_counts": dict(c.most_common(30)),
        "has_Egg": "Egg!" in c,
        "comp_count_hint": c.get("cdta", 0),
        "layer_count_hint": c.get("ldta", 0),
        "property_groups": c.get("tdgp", 0),
        "keyframe_blocks": c.get("lhd3", 0),
    }


def selftest():
    """自造一个最小 RIFX 样本，证明解析路径可用。"""
    def chunk(cid, data):
        pad = b"\x00" if len(data) % 2 else b""
        return cid + struct.pack(">I", len(data)) + data + pad

    def lst(sub, *kids):
        return chunk(b"LIST", sub + b"".join(kids))

    head = chunk(b"head", b"\x00\x00\x0d\xbc\x00\x0b\x00\x01")
    cdta = chunk(b"cdta", struct.pack(">HHHIIIHH", 1, 1, 0, 0, 0, 1500, 1920, 1080))
    item = lst(b"Item", chunk(b"idta", struct.pack(">HI", 3, 4)), chunk(b"Utf8", b"comp\x00"),
               cdta)
    body = b"Egg!" + lst(b"Fold", item)
    blob = b"RIFX" + struct.pack(">I", len(body) + 8) + body

    tree = parse_chunks(blob, 12, len(blob))
    s = summarize(tree)
    s["has_Egg"] = blob[8:12] == b"Egg!"
    ok = s["has_Egg"] and s["comp_count_hint"] == 1
    print(json.dumps({"selftest": "PASS" if ok else "FAIL", "summary": s,
                      "tree": tree}, ensure_ascii=False, indent=2))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?")
    ap.add_argument("--json")
    ap.add_argument("--tree", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.file:
        print("给个 .aep，或者用 --selftest")
        return 1
    buf = open(a.file, "rb").read()
    if buf[:4] != b"RIFX":
        print(f"不是 RIFX：头 4 字节 = {buf[:4]!r}")
        return 2
    size = struct.unpack(">I", buf[4:8])[0]
    tree = parse_chunks(buf, 12, min(len(buf), size + 8))
    out = {"file": a.file, "declared_size": size, "actual_size": len(buf),
           "summary": summarize(tree)}
    out["summary"]["has_Egg"] = buf[8:12] == b"Egg!"
    if a.tree:
        out["tree"] = tree
    text = json.dumps(out, ensure_ascii=False, indent=2)
    if a.json:
        open(a.json, "w", encoding="utf-8").write(text)
        print(f"{a.file}: {out['summary']}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())