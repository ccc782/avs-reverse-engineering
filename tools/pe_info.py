#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PE 静态解剖：头、节表、链接器、PDB 路径、Rich 头、版本资源、清单、签名。

用法:
    python pe_info.py <binary> [--json out.json]
只读文件，不执行、不改动目标。
"""
import argparse
import hashlib
import json
import os
import sys

import pefile


def rich_header(pe):
    """解析 Rich 头：MSVC 编译时每个 obj 的 key/prodID/count，可反推工具链版本。"""
    out = []
    try:
        data = pe.__data__
    except AttributeError:
        return out
    idx = data.find(b"Rich")
    if idx < 0:
        return out
    # Rich 头后面 4 字节是 key
    key = int.from_bytes(data[idx + 4:idx + 8], "little") if idx + 8 <= len(data) else 0
    pos = idx - 4
    entries = []
    while pos >= 16:
        chunk = data[pos - 12:pos]
        if len(chunk) < 12:
            break
        comp_id = int.from_bytes(chunk[0:4], "little")
        count = int.from_bytes(chunk[4:8], "little")
        if comp_id == 0 or count == 0:
            break
        prod_id = (comp_id ^ key) >> 16
        build = (comp_id ^ key) & 0xFFFF
        entries.append({"prod_id": prod_id, "build": build, "count": count})
        pos -= 8
        if len(entries) > 512:
            break
    for e in reversed(entries):
        out.append(e)
    return out


def version_info(pe):
    """VS_VERSIONINFO → dict（公司名、产品名、原始文件名、版本）。"""
    info = {}
    if not hasattr(pe, "FileInfo"):
        return info
    for fileinfo_list in pe.FileInfo:
        for fi in fileinfo_list:
            if isinstance(fi, pefile.Structure) and getattr(fi, "Key", b"") == b"StringFileInfo":
                for st in fi.StringTable:
                    for k, v in st.entries.items():
                        info[k.decode("utf-8", "replace")] = v.decode("utf-8", "replace")
            if isinstance(fi, pefile.Structure) and getattr(fi, "Key", b"") == b"VarFileInfo":
                try:
                    for entry in fi.Var:
                        pairs = getattr(entry, "entry", None)
                        if isinstance(pairs, list) and pairs and isinstance(pairs[0], (list, tuple)):
                            info["Translation"] = ",".join(
                                f"{p[0]:04x}{p[1]:04x}" for p in pairs if len(p) >= 2)
                        else:
                            info["Translation"] = str(entry.entry)
                except Exception:
                    pass
    return info


def section_entropy(sections_data):
    import math
    if not sections_data:
        return 0.0
    freq = [0] * 256
    for b in sections_data:
        freq[b] += 1
    n = len(sections_data)
    ent = 0.0
    for f in freq:
        if f:
            p = f / n
            ent -= p * math.log2(p)
    return round(ent, 3)


def analyze(path, cap_entropy_bytes=4 * 1024 * 1024):
    pe = pefile.PE(path, fast_load=False)
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)

    out = {
        "file": os.path.basename(path),
        "size": os.path.getsize(path),
        "sha256": h.hexdigest(),
        "machine": pefile.MACHINE_TYPE.get(pe.FILE_HEADER.Machine, hex(pe.FILE_HEADER.Machine)),
        "characteristics": hex(pe.FILE_HEADER.Characteristics),
        "dll_characteristics": hex(pe.OPTIONAL_HEADER.DllCharacteristics),
        "timestamp_utc": pe.FILE_HEADER.TimeDateStamp,
        "linker": f"{pe.OPTIONAL_HEADER.MajorLinkerVersion}.{pe.OPTIONAL_HEADER.MinorLinkerVersion}",
        "image_base": hex(pe.OPTIONAL_HEADER.ImageBase),
        "entry_point": hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint),
        "subsystem_dll": bool(pe.FILE_HEADER.Characteristics & 0x2000),
        "aslr": bool(pe.OPTIONAL_HEADER.DllCharacteristics & 0x40),
        "dep": bool(pe.OPTIONAL_HEADER.DllCharacteristics & 0x100),
        "cfg": bool(pe.OPTIONAL_HEADER.DllCharacteristics & 0x4000),
        "high_entropy_va": bool(pe.OPTIONAL_HEADER.DllCharacteristics & 0x20),
        "certificate": bool(pe.OPTIONAL_HEADER.DATA_DIRECTORY[4].Size),
        "sections": [],
    }
    import datetime
    try:
        out["timestamp_iso"] = datetime.datetime.utcfromtimestamp(
            pe.FILE_HEADER.TimeDateStamp).isoformat() + "Z"
    except Exception:
        pass

    for s in pe.sections:
        name = s.Name.rstrip(b"\x00").decode("utf-8", "replace")
        raw = s.get_data()[:cap_entropy_bytes]
        out["sections"].append({
            "name": name,
            "va": hex(s.VirtualAddress),
            "vsize": s.Misc_VirtualSize,
            "raw_size": s.SizeOfRawData,
            "entropy": section_entropy(raw),
            "exec": bool(s.Characteristics & 0x20000000),
            "write": bool(s.Characteristics & 0x80000000),
        })

    # PDB 路径（链接器泄漏的构建路径，最值钱的一条）
    pdbs = []
    if hasattr(pe, "DIRECTORY_ENTRY_DEBUG"):
        for d in pe.DIRECTORY_ENTRY_DEBUG:
            try:
                if hasattr(d.entry, "PdbFileName"):
                    pdbs.append(d.entry.PdbFileName.rstrip(b"\x00").decode("utf-8", "replace"))
            except Exception:
                pass
    out["pdb"] = pdbs
    out["rich_header"] = rich_header(pe)
    out["version_info"] = version_info(pe)

    # 加载资源里的 manifest
    manifests = []
    try:
        if hasattr(pe, "DIRECTORY_ENTRY_RESOURCE"):
            for rt in pe.DIRECTORY_ENTRY_RESOURCE.entries:
                if rt.id == 24:  # RT_MANIFEST
                    for e in rt.directory.entries:
                        for lang in e.directory.entries:
                            d = pe.get_data(lang.data.struct.OffsetToData,
                                            lang.data.struct.Size)
                            manifests.append(d[:4096].decode("utf-8", "replace"))
    except Exception:
        pass
    out["manifest_head"] = manifests[0][:600] if manifests else ""

    # 导入表依赖树
    deps = []
    if hasattr(pe, "DIRECTORY_ENTRY_IMPORT"):
        for entry in pe.DIRECTORY_ENTRY_IMPORT:
            deps.append({
                "dll": entry.dll.decode("utf-8", "replace"),
                "funcs": len(entry.imports),
            })
    out["imports_dll"] = deps
    out["exports_count"] = (len(pe.DIRECTORY_ENTRY_EXPORT.symbols)
                            if hasattr(pe, "DIRECTORY_ENTRY_EXPORT") else 0)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("binary")
    ap.add_argument("--json", default=None)
    a = ap.parse_args()
    info = analyze(a.binary)
    text = json.dumps(info, ensure_ascii=False, indent=2)
    if a.json:
        with open(a.json, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"写出 {a.json}")
    else:
        print(text)


if __name__ == "__main__":
    sys.exit(main())