#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""剪映 AI 深度测绘：接口面、任务模型、提示词结构、模型规格、云 API 清单。

四路深挖（比 ai_surface.py 更深一层）：
  A. RTTI → AI 相关的 Req/Resp 配对 → 内部 AI RPC 全表
  B. 源码树 → AI 流水线的模块与节点名
  C. 安装目录 → 每个模型包的 config/manifest 输入输出规格
  D. 端点清单 → 按 /lv/v1/<service>/<action> 聚合成云 API 目录

用法:
    python ai_deep.py --install "<剪映安装根>" --rtti reports/rtti_jy_veditor.json \
        --src reports/src_jy_veditor.json --endpoints reports/jy_endpoints.txt \
        --out reports/jianying_ai_deep
"""
import argparse
import json
import os
import re
from collections import Counter, defaultdict

# AI 域关键词 → 归类
AI_DOMAINS = {
    "抠像/分割": ["matting", "segmentation", "humans", "portrait", "chroma", "keying",
                  "green_screen", "salient"],
    "美颜/塑形": ["beauty", "makeup", "figure", "facefitting", "retouch", "slim", "eye"],
    "人脸": ["face", "freid", "gender", "petface"],
    "跟踪/锁定": ["track", "objectlock", "lockon", "stabiliz", "motion"],
    "画质": ["denoise", "deblur", "super", "scale", "interpolat", "umvfi", "deflicker",
             "relight", "enhance", "hdr", "defog", "quality"],
    "音频 AI": ["vocal", "voice", "tts", "tone", "pitch", "beat", "loudness", "denoise",
                "separat", "speech", "asr", "recogni", "lyric"],
    "字幕/文本": ["subtitle", "text_template", "recognize_text", "caption", "keyword"],
    "AIGC 生成": ["aigc", "aic", "ai_", "idream", "generate", "diffusion", "creator",
                  "writer", "story", "reel", "article"],
    "数字人": ["digital_human", "avatar", "vtuber", "talking"],
    "智能剪辑决策": ["smart", "clipflow", "decision", "highlight", "scene", "shot",
                     "auto_", "recommend", "rank"],
    "AI 任务调度": ["ai_queue", "aitask", "ai_task", "aigc_task", "async", "progress"],
}

MODEL_SPEC_FILES = ("config.json", "config_prev.json", "extra.json", "content.json",
                    "js-meta.json", "lua-meta.json", "model.json", "manifest.json")


def load_json(p):
    try:
        return json.load(open(p, encoding="utf-8", errors="replace"))
    except Exception:
        return None


def domain_of(name):
    low = name.lower()
    for dom, keys in AI_DOMAINS.items():
        if any(k in low for k in keys):
            return dom
    return None


def part_a_rpc(rtti_names):
    """A: AI 相关 Req/Resp 配对。"""
    ai = [n for n in rtti_names if domain_of(n)]
    methods = defaultdict(lambda: {"req": None, "resp": None, "ns": None})
    for n in ai:
        m = re.match(r"(?:(\w+)::)?(\w+?)(ReqStruct|RespStruct|Req|Resp)$", n)
        if not m:
            continue
        ns, base, kind = m.group(1) or "", m.group(2), m.group(3)
        key = f"{ns}::{base}" if ns else base
        methods[key]["ns"] = ns
        methods[key]["req" if kind.endswith(("ReqStruct", "Req")) else "resp"] = n
    rows = []
    for k, v in methods.items():
        rows.append({"method": k.split("::")[-1], "ns": v["ns"],
                     "req": v["req"], "resp": v["resp"],
                     "domain": domain_of(k) or "其它"})
    return sorted(rows, key=lambda r: (r["domain"], r["method"]))


def part_b_pipeline(src_paths):
    """B: 从源文件路径还原 AI 流水线节点。"""
    buckets = defaultdict(set)
    for p in src_paths:
        low = p.lower().replace("\\", "/")
        if not any(k in low for k in ("ai", "aigc", "matting", "clipflow", "task", "recognize",
                                     "speech", "voice", "tts", "face", "beauty", "track",
                                     "digitalhuman", "smart", "algorithm")):
            continue
        parts = low.split("/")
        # 取 videoeditor 之后的相对目录
        try:
            i = parts.index("videoeditor")
            rel = "/".join(parts[i + 1:])
        except ValueError:
            rel = "/".join(parts[-4:])
        buckets["/".join(rel.split("/")[:-1]) or "(根)"].add(rel.split("/")[-1])
    out = []
    for d, files in sorted(buckets.items(), key=lambda x: -len(x[1])):
        out.append({"dir": d, "count": len(files), "files": sorted(files)[:12]})
    return out[:40]


def part_c_models(install):
    """C: 每个模型包的规格文件与体积。"""
    base = os.path.join(install, "Resources", "models")
    rows = []
    if not os.path.isdir(base):
        return rows
    for name in sorted(os.listdir(base)):
        d = os.path.join(base, name)
        if not os.path.isdir(d):
            continue
        files, total = [], 0
        for b, _, fs in os.walk(d):
            for f in fs:
                fp = os.path.join(b, f)
                if os.path.isfile(fp):
                    total += os.path.getsize(fp)
                    files.append((f, os.path.getsize(fp)))
        specs = {}
        for f, _ in files:
            if f in MODEL_SPEC_FILES:
                j = load_json(os.path.join(d, f))
                if j is not None:
                    specs[f] = j if not isinstance(j, (list, dict)) or len(str(j)) < 4000 else str(j)[:4000]
        big = sorted(files, key=lambda x: -x[1])[:4]
        rows.append({
            "dir": name,
            "mb": round(total / 1024 / 1024, 2),
            "file_count": len(files),
            "weights": [{"name": f, "mb": round(s / 1024 / 1024, 2)} for f, s in big],
            "specs": specs,
            "domain": domain_of(name) or "其它",
        })
    return rows


def part_d_endpoints(path):
    """D: /lv/v1/<service>/<action> 聚合。"""
    svc = defaultdict(set)
    hosts = Counter()
    if not os.path.exists(path):
        return {"services": {}, "hosts": {}}
    section = None
    for line in open(path, encoding="utf-8", errors="replace"):
        line = line.rstrip("\n")
        if line.startswith("## "):
            section = line[3:].strip()
            continue
        if not line or line.startswith("#"):
            continue
        val = line.split("\t")[0]
        if section == "HOST":
            hosts[val] += 1
            continue
        m = re.search(r"/lv/v\d+/([a-z0-9_]+)/([a-z0-9_]+)", val)
        if m:
            svc[f"{m.group(1)}/{m.group(2)}"].add(line.split("\t")[1] if "\t" in line else "")
        m2 = re.search(r"/lv/v\d+/([a-z0-9_]+)\b", val)
        if m2 and not m:
            svc[m2.group(1)].add(line.split("\t")[1] if "\t" in line else "")
    return {"services": {k: sorted(v) for k, v in sorted(svc.items())},
            "hosts": dict(hosts.most_common(20))}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--install", required=True)
    ap.add_argument("--rtti", required=True)
    ap.add_argument("--src", required=True)
    ap.add_argument("--endpoints", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    rtti = [r["name"] for r in json.load(open(a.rtti, encoding="utf-8"))]
    src = list(json.load(open(a.src, encoding="utf-8"))["paths"].keys())

    rpc = part_a_rpc(rtti)
    pipe = part_b_pipeline(src)
    models = part_c_models(a.install)
    eps = part_d_endpoints(a.endpoints)

    dom_rpc = Counter(r["domain"] for r in rpc)
    dom_model = Counter(m["domain"] for m in models)

    md = ["# 剪映 AI 深挖：接口 / 流水线 / 模型规格 / 云 API", "",
          f"- AI 命中的 RTTI 类名：**{len([n for n in rtti if domain_of(n)])}**",
          f"- 反推出的 AI RPC：**{len(rpc)}**（按域分布：" +
          "，".join(f"{k} {v}" for k, v in dom_rpc.most_common()) + "）",
          f"- AI 流水线目录：**{len(pipe)}**",
          f"- 端侧模型包：**{len(models)}**（合计 {sum(m['mb'] for m in models):.0f} MB）",
          f"- 云 API 服务：**{len(eps['services'])}**", ""]

    md += ["## 一、AI RPC 全表（从 Req/Resp 结构体反推）", "",
           "| 域 | 命名空间 | 方法 | 请求结构 | 响应结构 |", "| --- | --- | --- | --- | --- |"]
    for r in rpc:
        md.append(f"| {r['domain']} | `{r['ns']}` | `{r['method']}` | "
                  f"{('`'+r['req']+'`') if r['req'] else '—'} | "
                  f"{('`'+r['resp']+'`') if r['resp'] else '—'} |")

    md += ["", "## 二、AI 流水线目录（源码树还原）", "",
           "| 文件数 | 目录 | 样本文件 |", "| ---: | --- | --- |"]
    for p in pipe:
        md.append(f"| {p['count']} | `{p['dir']}` | " +
                  "<br>".join(f"`{f}`" for f in p["files"][:5]) + " |")

    md += ["", "## 三、端侧模型包规格", "",
           "| 目录 | 域 | MB | 文件数 | 权重文件 | 规格文件 |", "| --- | --- | ---: | ---: | --- | --- |"]
    for m in sorted(models, key=lambda x: -x["mb"]):
        w = "<br>".join(f"`{x['name']}` {x['mb']}MB" for x in m["weights"])
        sp = "<br>".join(f"`{k}`" for k in m["specs"]) or "—"
        md.append(f"| `{m['dir']}` | {m['domain']} | {m['mb']} | {m['file_count']} | {w} | {sp} |")

    md += ["", "## 四、云 API 服务目录", "", "| 服务/动作 | 出现模块 |", "| --- | --- |"]
    for k, v in eps["services"].items():
        md.append(f"| `{k}` | {', '.join(sorted(set(v)))[:120]} |")
    md += ["", "### 主机", "", "```"] + [f"{h}  x{c}" for h, c in eps["hosts"].items()] + ["```"]

    open(a.out + ".md", "w", encoding="utf-8").write("\n".join(md))
    json.dump({"rpc": rpc, "pipeline": pipe, "models": models, "cloud": eps},
              open(a.out + ".json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"AI RPC {len(rpc)} / 流水线目录 {len(pipe)} / 模型 {len(models)} / 云服务 {len(eps['services'])} -> {a.out}.md")
    print("域分布：" + "，".join(f"{k} {v}" for k, v in dom_rpc.most_common()))


if __name__ == "__main__":
    main()