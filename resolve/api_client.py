#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""达芬奇脚本 API 客户端：连活实例、读工程、导时间轴、提交渲染。

前置：Resolve 正在运行；Studio 版在 偏好设置 > 系统 > 常规 里把
External scripting 设为 Local（或 Network 用于局域网）。

用官方自带解释器最省事：
    "C:\Program Files\Blackmagic Design\DaVinci Resolve\ResolvePython\ResolvePython.exe" api_client.py probe
用自备 Python 时先设环境变量：
    RESOLVE_SCRIPT_API=%PROGRAMDATA%\Blackmagic Design\DaVinci Resolve\Support\Developer\Scripting
    RESOLVE_SCRIPT_LIB=C:\Program Files\Blackmagic Design\DaVinci Resolve\fusionscript.dll
    PYTHONPATH=%RESOLVE_SCRIPT_API%\Modules\

用法:
    python api_client.py probe                      # 版本/工程/显卡/是否 Studio
    python api_client.py tree                       # 工程与时间轴树
    python api_client.py timeline                   # 当前时间轴的轨道与片段
    python api_client.py export <out.otio>          # 导出当前时间轴为 OTIO
    python api_client.py render <dir>               # 给当前时间轴加一个渲染任务并开跑
"""
import json
import os
import sys


def connect():
    try:
        import DaVinciResolveScript as dvr
    except ImportError:
        api = os.environ.get("RESOLVE_SCRIPT_API")
        if api and os.path.join(api, "Modules") not in sys.path:
            sys.path.append(os.path.join(api, "Modules"))
        import DaVinciResolveScript as dvr
    resolve = dvr.scriptapp("Resolve")
    if resolve is None:
        raise SystemExit("连不上 Resolve：实例没起，或 External scripting 未开")
    return resolve


def probe(resolve):
    pm = resolve.GetProjectManager()
    proj = pm.GetCurrentProject()
    return {
        "product": resolve.GetProductName(),
        "version": resolve.GetVersionString(),
        "is_studio": bool(resolve.IsStudio()),
        "page": resolve.GetCurrentPage(),
        "project": proj.GetName() if proj else None,
        "timeline": (proj.GetCurrentTimeline().GetName()
                     if proj and proj.GetCurrentTimeline() else None),
        "gpu": resolve.GetCurrentPage(),
        "databases": pm.GetDatabaseList(),
        "extras": resolve.GetExtrasPackages() if resolve.IsStudio() else [],
    }


def tree(resolve):
    pm = resolve.GetProjectManager()
    proj = pm.GetCurrentProject()
    if not proj:
        return {"projects": pm.GetProjectListInCurrentFolder(), "current": None}
    timelines = []
    for i in range(1, proj.GetTimelineCount() + 1):
        t = proj.GetTimelineByIndex(i)
        if t:
            timelines.append({
                "index": i,
                "name": t.GetName(),
                "start_frame": t.GetStartFrame(),
                "end_frame": t.GetEndFrame(),
                "video_tracks": t.GetTrackCount("video"),
                "audio_tracks": t.GetTrackCount("audio"),
                "subtitle_tracks": t.GetTrackCount("subtitle"),
            })
    return {"project": proj.GetName(), "timelines": timelines,
            "settings": proj.GetSettings()}


def timeline(resolve):
    proj = resolve.GetProjectManager().GetCurrentProject()
    tl = proj.GetCurrentTimeline() if proj else None
    if not tl:
        return {"error": "没有打开的时间轴"}
    out = {"name": tl.GetName(), "start_timecode": tl.GetStartTimecode(),
           "fps": proj.GetSetting("timelineFrameRate"), "tracks": []}
    for kind in ("video", "audio", "subtitle"):
        for i in range(1, tl.GetTrackCount(kind) + 1):
            items = []
            for it in tl.GetItemListInTrack(kind, i) or []:
                items.append({
                    "name": it.GetName(),
                    "start": it.GetStart(),
                    "end": it.GetEnd(),
                    "duration": it.GetDuration(),
                    "source_start": it.GetSourceStartFrame(),
                    "type": it.GetType(),
                    "fusion_comps": it.GetFusionCompCount(),
                })
            out["tracks"].append({"kind": kind, "index": i, "items": items})
    return out


def export_otio(resolve, out_path):
    proj = resolve.GetProjectManager().GetCurrentProject()
    tl = proj.GetCurrentTimeline()
    ok = tl.Export(out_path, resolve.EXPORT_OTIO)
    return {"exported": bool(ok), "path": out_path}


def render(resolve, out_dir):
    proj = resolve.GetProjectManager().GetCurrentProject()
    tl = proj.GetCurrentTimeline()
    proj.SetCurrentRenderFormatAndCodec("mp4", "H264")
    job = proj.AddRenderJob()
    if not job:
        return {"error": "AddRenderJob 失败（先确认时间轴已选中）"}
    proj.SetRenderSettings({
        "SelectAllFrames": 1,
        "TargetDir": out_dir,
        "CustomName": tl.GetName(),
    })
    started = proj.StartRendering([job])
    return {"job_id": job, "started": bool(started)}


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "probe"
    resolve = connect()
    if cmd == "probe":
        r = probe(resolve)
    elif cmd == "tree":
        r = tree(resolve)
    elif cmd == "timeline":
        r = timeline(resolve)
    elif cmd == "export":
        r = export_otio(resolve, sys.argv[2])
    elif cmd == "render":
        r = render(resolve, sys.argv[2])
    else:
        raise SystemExit(__doc__)
    print(json.dumps(r, ensure_ascii=False, indent=2, default=str))


if __name__ == "__main__":
    main()