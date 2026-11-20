#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""达芬奇 .drp 工程包工具：拆包 / 结构解剖 / 重打包 / 差异。

.drp 是 ZIP：project.xml + MediaPool/Master/MpFolder.xml + SeqContainer/<uuid>.xml + Gallery.xml
本工具只处理明文 XML 层，不碰 CompositionBA 里的压缩块。

用法:
    python drp_tool.py info  <x.drp>
    python drp_tool.py dump  <x.drp> --out dir
    python drp_tool.py pack  <dir> --out y.drp
    python drp_tool.py diff  <a.drp> <b.drp>
    python drp_tool.py seq   <x.drp> --json seq.json
"""
import argparse
import hashlib
import json
import os
import re
import sys
import zipfile
import xml.etree.ElementTree as ET


def info(path):
    with zipfile.ZipFile(path) as z:
        members = [{"name": i.filename, "size": i.file_size,
                    "comp": i.compress_size, "crc": f"{i.CRC:08x}"} for i in z.infolist()]
        proj = z.read("project.xml").decode("utf-8", "replace")
    meta = {}
    m = re.search(r'DbAppVer="([^"]+)"', proj)
    if m:
        meta["app_ver"] = m.group(1)
    m = re.search(r'DbPrjVer="([^"]+)"', proj)
    if m:
        meta["project_ver"] = m.group(1)
    m = re.search(r"<ProjectName>([^<]*)</ProjectName>", proj)
    if m:
        meta["project_name"] = m.group(1)
    return {"file": os.path.basename(path), "members": members, "meta": meta,
            "sha256": hashlib.sha256(open(path, "rb").read()).hexdigest()}


def _parse_xml_safe(raw: bytes):
    """达芬奇的 XML 里会混进裸控制字节（编码块/版本表），先清洗再解析。"""
    text = raw.decode("utf-8", "replace")
    cleaned = "".join(ch for ch in text if ch in "\t\n\r" or ord(ch) >= 0x20)
    try:
        return ET.fromstring(cleaned)
    except ET.ParseError:
        # 兜底：把解析器塞不下的段落整体剥掉，只保留结构标签
        cleaned = re.sub(r">[^<>]{0,8000}<", "><", cleaned)
        return ET.fromstring(cleaned)


def _tag_text(block, tag, default=None):
    m = re.search(rf"<{tag}>([^<]*)</{tag}>", block)
    return m.group(1) if m else default


def seqs(path):
    """解析 SeqContainer 里的轨道/片段结构。

    达芬奇的 XML 里混有裸控制字节，ElementTree 会直接拒绝；这里用结构化正则
    按标签切块取字段，既不依赖 XML 严格性，也足够做结构分析。
    """
    out = []
    with zipfile.ZipFile(path) as z:
        for name in z.namelist():
            if not name.startswith("SeqContainer/") or not name.endswith(".xml"):
                continue
            text = z.read(name).decode("utf-8", "replace")
            container_id = (re.search(r'<Sm2SequenceContainer DbId="([^"]+)"', text) or
                            [None, None])[1]
            tracks = []
            for tblock in re.split(r"<Sm2TiTrack\b", text)[1:]:
                tblock = tblock.split("</Sm2TiTrack>")[0]
                tid = (re.search(r'DbId="([^"]+)"', tblock) or [None, None])[1]
                clips = []
                for tag in ("Sm2TiVideoClip", "Sm2TiAudioClip", "Sm2TiSubtitleClip"):
                    for cblock in re.split(rf"<{tag}\b", tblock)[1:]:
                        cblock = cblock.split(f"</{tag}>")[0]
                        clips.append({
                            "tag": tag,
                            "db_id": (re.search(r'DbId="([^"]+)"', cblock) or [None, None])[1],
                            "type": _tag_text(cblock, "PrettyType", ""),
                            "name": _tag_text(cblock, "Name"),
                            "start": int(_tag_text(cblock, "Start", "0") or 0),
                            "duration": int(_tag_text(cblock, "Duration", "0") or 0),
                            "has_composition": "<CompositionTable>" in cblock,
                        })
                tracks.append({
                    "db_id": tid,
                    "type": _tag_text(tblock, "Type"),
                    "sub_type": _tag_text(tblock, "SubType"),
                    "sequence": _tag_text(tblock, "Sequence"),
                    "clips": sorted(clips, key=lambda x: x["start"]),
                })
            out.append({"member": name, "db_id": container_id, "tracks": tracks})
    return out


def dump(path, outdir):
    os.makedirs(outdir, exist_ok=True)
    with zipfile.ZipFile(path) as z:
        z.extractall(outdir)
    print(f"解到 {outdir}（{len(os.listdir(outdir))} 项）")


def pack(dirpath, out):
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for base, _, files in os.walk(dirpath):
            for f in files:
                full = os.path.join(base, f)
                z.write(full, os.path.relpath(full, dirpath).replace("\\", "/"))
    print(f"打包 {out}（{os.path.getsize(out)} 字节）")


def diff(a, b):
    ia, ib = info(a), info(b)
    sa = {m["name"]: m for m in ia["members"]}
    sb = {m["name"]: m for m in ib["members"]}
    only_a = sorted(set(sa) - set(sb))
    only_b = sorted(set(sb) - set(sa))
    changed = sorted(n for n in set(sa) & set(sb) if sa[n]["crc"] != sb[n]["crc"])
    return {"only_in_a": only_a, "only_in_b": only_b, "changed": changed,
            "meta_a": ia["meta"], "meta_b": ib["meta"]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["info", "dump", "pack", "diff", "seq"])
    ap.add_argument("path")
    ap.add_argument("path2", nargs="?")
    ap.add_argument("--out")
    ap.add_argument("--json")
    a = ap.parse_args()

    if a.cmd == "info":
        r = info(a.path)
        print(json.dumps(r, ensure_ascii=False, indent=2))
    elif a.cmd == "dump":
        dump(a.path, a.out or (a.path + "_x"))
    elif a.cmd == "pack":
        pack(a.path, a.out or "repack.drp")
    elif a.cmd == "diff":
        r = diff(a.path, a.path2)
        print(json.dumps(r, ensure_ascii=False, indent=2))
    else:
        r = seqs(a.path)
        text = json.dumps(r, ensure_ascii=False, indent=2)
        if a.json:
            open(a.json, "w", encoding="utf-8").write(text)
            print(f"{len(r)} 个序列容器，{sum(len(s['tracks']) for s in r)} 条轨道 -> {a.json}")
        else:
            print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())