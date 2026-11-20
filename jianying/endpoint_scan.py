#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""从多个二进制里抽 HTTP 端点与 SDK 标识，产出端点清单。

剪映的云端 AI 能力分散在不同模块：语音在 speechsdk.dll，变声/克隆在 grow-voice-api.dll，
AIGC 在 GeckoSDK.dll，云素材在 ever_cloud_sdk.dll。单看 videoeditor.dll 会漏掉一大半。

用法:
    python endpoint_scan.py --dir "<剪映安装根>" --out reports/jy_endpoints.txt
    python endpoint_scan.py --dir "<根>" --out x.txt --only speechsdk.dll grow-voice-api.dll
"""
import argparse
import os
import re
from collections import OrderedDict

URL_RE = re.compile(rb"https?://[ -~]{6,160}")
PATH_RE = re.compile(rb"/(?:lv|api|v1|v2)/[a-z0-9_/{}.\-]{3,80}")
HOST_RE = re.compile(rb"\b(?:[a-z0-9-]+\.)+(?:com|cn|net|io|ai)\b")

DEFAULT_TARGETS = [
    "videoeditor.dll", "JianyingPro.exe", "DeepAgentsService.dll", "deepagents_capi.dll",
    "speechsdk.dll", "grow-voice-api.dll", "GeckoSDK.dll", "GeckoCppSDK.dll",
    "ever_cloud_sdk.dll", "sscronet.dll", "pc_push.dll", "uploader.dll",
    "AICreator.dll", "EffectPlatform.dll", "Tracking.dll", "resourcecli.dll",
    "agent_runtime_addon.node", "videoeditor_addon.node",
]


def scan_file(path):
    data = open(path, "rb").read()
    urls = [m.group(0).decode("latin-1") for m in URL_RE.finditer(data)]
    paths = [m.group(0).decode("latin-1") for m in PATH_RE.finditer(data)]
    hosts = [m.group(0).decode("latin-1") for m in HOST_RE.finditer(data)]
    return urls, paths, hosts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--only", nargs="*")
    a = ap.parse_args()

    targets = a.only or DEFAULT_TARGETS
    urls, paths, hosts = OrderedDict(), OrderedDict(), OrderedDict()
    scanned = []
    for name in targets:
        p = os.path.join(a.dir, name)
        if not os.path.isfile(p):
            continue
        scanned.append((name, round(os.path.getsize(p) / 1024 / 1024, 1)))
        u, pa, h = scan_file(p)
        for x in u:
            urls.setdefault(x, name)
        for x in pa:
            paths.setdefault(x, name)
        for x in h:
            hosts.setdefault(x, name)

    lines = ["# 端点 / 主机 / 路径（来源文件标注在第二列）", "", "## URL"]
    lines += [f"{u}\t{src}" for u, src in urls.items()]
    lines += ["", "## HOST"]
    lines += [f"{h}\t{src}" for h, src in hosts.items()]
    lines += ["", "## PATH"]
    lines += [f"{p}\t{src}" for p, src in paths.items()]
    open(a.out, "w", encoding="utf-8").write("\n".join(lines))

    print(f"扫描 {len(scanned)} 个模块，URL {len(urls)} / 主机 {len(hosts)} / 路径 {len(paths)} -> {a.out}")
    print("  模块：" + ", ".join(f"{n}({s}MB)" for n, s in scanned))
    print("  主机样本：" + ", ".join(list(hosts)[:12]))
    print("  路径样本：" + ", ".join(list(paths)[:10]))


if __name__ == "__main__":
    main()