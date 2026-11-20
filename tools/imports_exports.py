#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""导入/导出表 + 可疑能力归类。

不评价「好/坏」，只把每个 PE 依赖的 API 按能力面归类，用于判断：
网络栈、加密栈、文件系统、进程与调试、GPU、反调试痕迹。

用法:
    python imports_exports.py <binary> [--json out.json] [--exports]
"""
import argparse
import json
import sys

import pefile

CATEGORY = {
    "网络": ["ws2_32", "winhttp", "wininet", "wsock32", "mswsock", "httpapi", "dnsapi",
             "secur32", "crypt32", "ncrypt", "schannel"],
    "进程与调试": ["kernel32", "ntdll", "psapi", "tlhelp32", "dbghelp", "powrprof"],
    "加密": ["bcrypt", "bcryptprimitives", "advapi32", "ncrypt", "crypt32", "cryptsp"],
    "图形": ["d3d11", "d3d12", "dxgi", "opengl32", "vulkan-1", "d3dcompiler_47",
             "dxcompiler", "dxil", "nvapi", "amfrt", "libmfx", "opencl"],
    "音频": ["winmm", "dsound", "xaudio2", "mfplat", "mfreadwrite", "portaudio",
             "libsndfile", "coreaudio"],
    "运行时": ["msvcp", "vcruntime", "ucrtbase", "concrt", "vcomp", "api-ms-win"],
    "COM/UI": ["ole32", "oleaut32", "comctl32", "uxtheme", "dwmapi", "shell32", "shlwapi"],
}

SUSPICIOUS = {
    "反调试/反虚拟机": [
        "IsDebuggerPresent", "CheckRemoteDebuggerPresent", "NtQueryInformationProcess",
        "OutputDebugStringA", "OutputDebugStringW", "QueryPerformanceCounter",
        "GetTickCount64", "NtSetInformationThread", "DebugActiveProcess",
        "CreateToolhelp32Snapshot", "Process32FirstW", "Process32NextW",
        "NtQuerySystemInformation", "GetSystemFirmwareTable",
    ],
    "注入/内存": [
        "VirtualAllocEx", "WriteProcessMemory", "CreateRemoteThread", "QueueUserAPC",
        "SetWindowsHookExW", "NtMapViewOfSection", "VirtualProtect", "LoadLibraryExW",
        "GetProcAddress", "LdrLoadDll", "RtlAddVectoredExceptionHandler",
    ],
    "凭据/令牌": [
        "LogonUserW", "CredReadW", "CryptUnprotectData", "LsaEnumerateLogonSessions",
        "OpenProcessToken", "DuplicateTokenEx", "ImpersonateLoggedOnUser",
    ],
    "文件外发": [
        "InternetOpenUrlW", "HttpSendRequestW", "WinHttpSendRequest",
        "WinHttpOpenRequest", "URLDownloadToFileW", "ShellExecuteExW",
    ],
    "隐私数据": [
        "GetComputerNameW", "GetVolumeInformationW", "GetAdaptersInfo",
        "GetAdaptersAddresses", "WTSEnumerateSessionsW", "EnumWindows",
        "GetForegroundWindow", "GetKeyState", "SetWindowsHookExA",
    ],
}


def classify(dll_name):
    n = dll_name.lower().replace(".dll", "")
    for cat, keys in CATEGORY.items():
        if any(k in n for k in keys):
            return cat
    return "其它"


def analyze(path, want_exports=False):
    pe = pefile.PE(path, fast_load=True)
    pe.parse_data_directories(directories=[
        pefile.DIRECTORY_ENTRY["IMAGE_DIRECTORY_ENTRY_IMPORT"],
        pefile.DIRECTORY_ENTRY["IMAGE_DIRECTORY_ENTRY_EXPORT"],
    ])
    imports = {}
    api_hits = {k: [] for k in SUSPICIOUS}
    for entry in getattr(pe, "DIRECTORY_ENTRY_IMPORT", []):
        dll = entry.dll.decode("utf-8", "replace")
        names = []
        for imp in entry.imports:
            if imp.name:
                names.append(imp.name.decode("utf-8", "replace"))
        imports[dll] = sorted(names)
        for cat, keys in SUSPICIOUS.items():
            for k in keys:
                if k in names:
                    api_hits[cat].append(f"{dll}!{k}")

    out = {
        "file": path.split("\\")[-1],
        "dll_count": len(imports),
        "by_category": {},
        "suspicious": {k: sorted(set(v)) for k, v in api_hits.items() if v},
        "imports": imports,
    }
    for dll in imports:
        out["by_category"].setdefault(classify(dll), []).append(dll)

    if want_exports and hasattr(pe, "DIRECTORY_ENTRY_EXPORT"):
        out["exports"] = [s.name.decode("utf-8", "replace") if s.name else f"ord{s.ordinal}"
                          for s in pe.DIRECTORY_ENTRY_EXPORT.symbols]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("binary")
    ap.add_argument("--json")
    ap.add_argument("--exports", action="store_true")
    a = ap.parse_args()
    r = analyze(a.binary, a.exports)
    if a.json:
        json.dump(r, open(a.json, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print(f"{r['file']}: {r['dll_count']} 个依赖，可疑面 {list(r['suspicious'])}")
    else:
        print(json.dumps(r, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())