#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""剪映 AI 能力面测绘：把散在模型包、类名、命令表、网络端点里的证据汇总成矩阵。

四路证据：
  1. 端侧模型包  <install>\Resources\models\*             → 目录名 + 体积 = 能力存在
  2. RTTI 类名   reports/rtti_jy_veditor.json             → 类级实现线索
  3. 命令表      reports/commands_jy.json                 → 可从外部触发的动作
  4. 字符串端点  reports/str_jy_veditor.txt (可选)        → 云端接口与 SDK

输出：Markdown 矩阵 + JSON。

用法:
    python ai_surface.py --install "<剪映安装根>" --rtti reports/rtti_jy_veditor.json \
        --commands reports/commands_jy.json --strings reports/str_jy_veditor.txt \
        --out reports/jianying_ai_matrix
"""
import argparse
import json
import os
import re
from collections import defaultdict

# 能力分类：关键词命中哪一路就归到哪个能力
CAPABILITIES = {
    "人像抠像/视频分割": {
        "models": ["mattingmodel", "tt_interactive_matting", "tt_mobilevos", "headsegmodel",
                   "humanparsingmodel", "hairparser", "saliency_seg_model", "tt_salient_human",
                   "skin_seg", "mattingBlend", "mattingBlendV2", "mattingBlendCloud", "matting_config"],
        "classes": ["Matting", "Portrait", "HumanSeg", "PersonSeg", "Vos"],
        "commands": ["setMatting", "clearMatting", "addCustomMatting", "applyAllChroma"],
        "endpoints": ["matting", "portrait_matting"],
    },
    "绿幕/色度键": {
        "models": ["Chroma", "Chroma2"],
        "classes": ["Chroma", "GreenScreen"],
        "commands": ["setChromaColor", "setChromaIntensity", "setChromaShadow",
                     "setChromaEdgeSmooth", "setChromaSpill", "resetChroma"],
        "endpoints": [],
    },
    "美颜/美妆/塑形": {
        "models": ["facebeautifymodel", "bingo_facegan_model", "tt_gendergan",
                   "facefitting", "tt_facefitting_3d", "tt_eyefitting", "petfacemodel"],
        "classes": ["Beauty", "Makeup", "Figure", "FaceFitting", "Retouch"],
        "commands": ["setFigure", "setMakeupRoot", "clearFigure", "setFigureFaceId"],
        "endpoints": ["beauty", "retouch"],
    },
    "人脸识别/聚类/验证": {
        "models": ["faceclustingmodel", "faceverifymodel", "freidmodel"],
        "classes": ["FaceCluster", "FaceVerify", "FaceId", "Freid"],
        "commands": [],
        "endpoints": ["face_cluster", "face_verify"],
    },
    "手部/骨骼/动作": {
        "models": ["handmodel", "skeleton_model", "avatar3d", "avatar_drive"],
        "classes": ["Hand", "Skeleton", "Pose", "Avatar"],
        "commands": ["addDigitalHuman", "updateDigitalHuman"],
        "endpoints": ["digital_human", "avatar"],
    },
    "深度/显著性/场景": {
        "models": ["depthmodel", "alg_scene_normal", "scene_normal_model", "colorcard"],
        "classes": ["Depth", "Saliency", "SceneNormal"],
        "commands": [],
        "endpoints": [],
    },
    "插帧/超分/去闪烁": {
        "models": ["interpolation", "umvfi", "deflicker"],
        "classes": ["Interpolat", "SuperResol", "Deflicker", "SuperScale"],
        "commands": ["setVideoAlgorithm", "setStable"],
        "endpoints": ["interpolation", "super_resolution"],
    },
    "防抖/稳定": {
        "models": [],
        "classes": ["Stabiliz", "Stable", "Gyro"],
        "commands": ["setStable"],
        "endpoints": ["stab"],
    },
    "降噪（画/音）": {
        "models": ["noise_reduction", "rnnoise", "audiomodel", "audiosami"],
        "classes": ["Denoise", "NoiseReduction", "Rnnoise"],
        "commands": ["denoiseOn", "denoiseOff"],
        "endpoints": ["denoise"],
    },
    "人声分离/修音/变声": {
        "models": ["audiomodel", "audiosami", "vocal_beautifys", "vocal_separations"],
        "classes": ["VocalSepar", "VocalBeautify", "VoiceEffect", "PitchShift", "Tone"],
        "commands": ["setVocalSeparation", "setVocalBeautify", "setVoiceEffect",
                     "setVoiceEffectParams", "modifiedToneOn", "pitchOn", "pitchOff"],
        "endpoints": ["vocal_separ", "voice_conversion", "grow-voice"],
    },
    "语音识别/字幕/歌词": {
        "models": ["audio_metrics", "audiomodel", "espresso", "sentence_score", "aed"],
        "classes": ["Recognize", "Transcri", "Speech", "Subtitle", "Lyric", "Asr"],
        "commands": ["addSubtitles", "updateSubtitleTemplate", "setSubtitleKeywords",
                     "clearSubtitleKeywords", "deleteTextToAudioIds"],
        "endpoints": ["audio_subtitle", "asr", "speechsdk", "lyric"],
    },
    "TTS/配音/音色克隆": {
        "models": ["tts", "aigc_text"],
        "classes": ["Tts", "VoiceClone", "SpeechSynthesis", "VoiceOver"],
        "commands": ["deleteTextToAudioIds"],
        "endpoints": ["text_to_audio", "tts", "voice_clone"],
    },
    "视觉跟踪/物体锁定": {
        "models": ["object_tracking"],
        "classes": ["Tracking", "Tracker", "ObjectLock", "VideoTrack"],
        "commands": ["addVideoTracker", "updateVideoTracker", "removeVideoTracker",
                     "addObjectLocked", "updateObjectLocked", "removeObjectLocked"],
        "endpoints": ["track"],
    },
    "智能裁剪/运镜/构图": {
        "models": ["saliency_seg_model"],
        "classes": ["SmartCrop", "SmartReframe", "AutoReframe", "SmartColor"],
        "commands": ["addSmartCrop", "removeSmartCrop", "setSmartColorAdjust"],
        "endpoints": ["smart_crop", "smart_reframe"],
    },
    "智能打光/眼神/画质修复": {
        "models": ["idream", "bingo_facegan_model"],
        "classes": ["Relight", "EyeCorrect", "Enhance", "Restore"],
        "commands": ["setVideoAlgorithm"],
        "endpoints": ["relight", "enhance"],
    },
    "素材语义检索": {
        "models": ["media_search", "SegmentJS"],
        "classes": ["MediaSearch", "SemanticSearch", "Embedding"],
        "commands": [],
        "endpoints": ["search", "embedding"],
    },
    "AIGC 生成（文/图/视频）": {
        "models": ["idream", "mangamodel", "jianying_aigc_charge"],
        "classes": ["Aigc", "AIGC", "AiCreation", "AiWriter", "AiReel", "AiStory",
                    "AiArticle", "ArticleVideo", "Prompt"],
        "commands": ["setAiCreatorContent", "updateAiCreation", "updateAiReelAgent"],
        "endpoints": ["aigc", "text_to_image", "text_to_video", "create"],
    },
    "数字人": {
        "models": ["avatar3d", "avatar_drive", "digital_human"],
        "classes": ["DigitalHuman", "Avatar"],
        "commands": ["addDigitalHuman", "updateDigitalHuman", "updateDigitalHumanRendered"],
        "endpoints": ["digital_human"],
    },
    "场景检测/镜头切分": {
        "models": ["SceneEditDetection"],
        "classes": ["SceneDetect", "SceneEdit", "ShotDetect", "Highlight"],
        "commands": [],
        "endpoints": ["scene", "highlight", "smart_highlight"],
    },
    "隐形水印/AI 标识": {
        "models": ["invisible_watermark", "VideoWaterMark"],
        "classes": ["Watermark", "Forensic"],
        "commands": ["updateDraftAIGCWatermark", "addPreviewWatermark"],
        "endpoints": ["watermark"],
    },
}

MODE_HINT = {
    "端侧": "模型包在本地 + 类级实现存在",
    "云侧": "只有网络端点与 SDK，本地无模型包",
    "双路": "本地有模型包，同时有云端端点",
}


def list_models(install):
    """返回 {目录名: (MB, 文件数)}"""
    base = os.path.join(install, "Resources", "models")
    out = {}
    if not os.path.isdir(base):
        return out
    for name in os.listdir(base):
        p = os.path.join(base, name)
        if not os.path.isdir(p):
            continue
        total, files = 0, 0
        for b, _, fs in os.walk(p):
            for f in fs:
                fp = os.path.join(b, f)
                if os.path.isfile(fp):
                    total += os.path.getsize(fp)
                    files += 1
        out[name] = (round(total / 1024 / 1024, 1), files)
    return out


def list_res_dirs(install):
    base = os.path.join(install, "Resources")
    if not os.path.isdir(base):
        return {}
    out = {}
    for name in os.listdir(base):
        p = os.path.join(base, name)
        if os.path.isdir(p):
            n = sum(len(fs) for _, _, fs in os.walk(p))
            out[name] = n
    return out


def load_strings(path):
    if not path or not os.path.exists(path):
        return []
    with open(path, encoding="utf-8", errors="replace") as f:
        return [l.rstrip("\n") for l in f]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--install", required=True)
    ap.add_argument("--rtti")
    ap.add_argument("--commands")
    ap.add_argument("--strings")
    ap.add_argument("--endpoints", help="endpoint_scan.py 产出的端点清单")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    models = list_models(a.install)
    resdirs = list_res_dirs(a.install)
    rtti = [r["name"] for r in json.load(open(a.rtti, encoding="utf-8"))] if a.rtti else []
    cmds = json.load(open(a.commands, encoding="utf-8")) if a.commands else {"domains": {}, "safe_subset": []}
    strs = load_strings(a.strings)

    if a.endpoints and os.path.exists(a.endpoints):
        for line in open(a.endpoints, encoding="utf-8", errors="replace"):
            if line.strip() and not line.startswith("#"):
                strs.append(line.split(chr(9))[0])

    endpoint_hits = defaultdict(list)
    for s in strs:
        low = s.lower()
        if "ulikecam.com" in low or "/lv/v1/" in low:
            endpoint_hits["__all__"].append(s)
    all_endpoints = sorted(set(endpoint_hits["__all__"]))

    matrix = []
    for cap, spec in CAPABILITIES.items():
        m_hit = [m for m in spec["models"] if any(m.lower() in d.lower() for d in models)
                 or any(m.lower() in d.lower() for d in resdirs)]
        m_detail = {m: models[m] for m in models if any(k.lower() in m.lower() for k in spec["models"])}

        c_hit = [n for n in rtti if any(k.lower() in n.lower() for k in spec["classes"])][:12]

        cmd_hit = []
        for dom, items in cmds.get("domains", {}).items():
            for it in items:
                if it in spec["commands"]:
                    cmd_hit.append(f"{dom}.{it}")

        e_hit = [e for e in all_endpoints
                 if any(k and k.lower() in e.lower() for k in spec["endpoints"])][:8]

        if m_detail and e_hit:
            mode = "双路"
        elif m_detail:
            mode = "端侧"
        elif e_hit:
            mode = "云侧"
        elif c_hit or cmd_hit:
            mode = "端侧" if c_hit else "未知"
        else:
            mode = "未命中"
        if mode == "未命中":
            continue

        matrix.append({
            "capability": cap,
            "mode": mode,
            "models": m_detail,
            "classes": c_hit,
            "class_total": sum(1 for n in rtti if any(k.lower() in n.lower() for k in spec["classes"])),
            "commands": cmd_hit,
            "endpoints": e_hit,
        })

    # 输出
    md = [f"# 剪映 AI 能力矩阵（证据化）", "",
          f"- 扫描对象：`{os.path.basename(a.install)}` 的 `Resources\\models` 与 `Resources\\*`",
          f"- 端侧模型包：**{len(models)}** 个，合计 **{sum(v[0] for v in models.values()):.0f} MB**",
          f"- RTTI 类名：**{len(rtti)}**（全量在 `rtti_jy_veditor.md`）",
          f"- 可从外部触发的 AI 命令：{sum(len(x['commands']) for x in matrix)} 条",
          f"- 云端端点样本：{len(all_endpoints)} 条", "",
          "| 能力 | 落点 | 端侧模型包（MB / 文件） | 类级线索 | 可触发命令 | 云端端点 |",
          "| --- | --- | --- | ---: | --- | --- |"]

    for row in matrix:
        m = "<br>".join(f"`{k}` {v[0]}MB/{v[1]}f" for k, v in list(row["models"].items())[:4]) or "—"
        c = f"{row['class_total']} 个" + (
            "<br>" + "<br>".join(f"`{x}`" for x in row["classes"][:3]) if row["classes"] else "")
        cmd = "<br>".join(f"`{x}`" for x in row["commands"][:4]) or "—"
        ep = "<br>".join(f"`{x[:60]}`" for x in row["endpoints"][:3]) or "—"
        md.append(f"| {row['capability']} | {row['mode']} | {m} | {c} | {cmd} | {ep} |")

    md += ["", "## 端侧模型包全表", "",
           f"共 {len(models)} 个目录，合计 {sum(v[0] for v in models.values()):.0f} MB。", "",
           "| 目录 | MB | 文件数 |", "| --- | ---: | ---: |"]
    for k, v in sorted(models.items(), key=lambda x: -x[1][0]):
        md.append(f"| `{k}` | {v[0]} | {v[1]} |")

    md += ["", "## 云端端点（去重样本）", "", "```"]
    md += all_endpoints[:120]
    md += ["```"]

    open(a.out + ".md", "w", encoding="utf-8").write("\n".join(md))
    json.dump({"matrix": matrix, "models": {k: {"mb": v[0], "files": v[1]} for k, v in models.items()},
               "endpoints": all_endpoints}, open(a.out + ".json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)

    print(f"能力 {len(matrix)} 项 / 模型包 {len(models)} 个 / 端点 {len(all_endpoints)} 条 -> {a.out}.md")
    for row in matrix:
        print(f"  {row['mode']:3s} {row['capability']:22s} 模型 {len(row['models'])}  类 {row['class_total']:4d}  命令 {len(row['commands'])}  端点 {len(row['endpoints'])}")


if __name__ == "__main__":
    main()