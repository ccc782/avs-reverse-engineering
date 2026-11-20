#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""加密特征扫描：算法常量 + 加密库指纹。

不实现任何解密，只回答「这个二进制里有哪些密码学实现」。
判据全部是可复核的字节常量或库特征串。

用法:
    python find_crypto.py <binary> [--json out.json]
"""
import argparse
import hashlib
import json
import re
import sys

# 已知常量：命中即说明该算法实现被编译进二进制
CONSTANTS = {
    "AES_SBOX_FIPS197": bytes.fromhex(
        "637c777bf26b6fc53001672bfed7ab76ca82c97dfa5947f0add4a2af9ca472c0"),
    "AES_INV_SBOX": bytes.fromhex(
        "52096ad53036a538bf40a39e81f3d7fb7ce339829b2fff87348e4344c4dee9cb"),
    "AES_RCON": bytes.fromhex("01020408102040801b366cd8ab4d9a2f"),
    "SHA256_K": bytes.fromhex(
        "428a2f9871374491b5c0fbcfe9b5dba53956c25b59f111f1923f82a4ab1c5ed5"),
    "SHA512_K": bytes.fromhex(
        "428a2f98d728ae227137449123ef65cdb5c0fbcfec4d3b2fe9b5dba58189dbbc"),
    "MD5_IV": bytes.fromhex("0123456789abcdeffedcba9876543210"),
    "SHA1_IV": bytes.fromhex("67452301efcdab8998badcfe10325476c3d2e1f0"),
    "CRC32_POLY": bytes.fromhex("edb88320"),
}

# 库指纹：源码里出现的符号/类名/异常文本
FINGERPRINTS = {
    "Crypto++": [b"CryptoPP", b"Rijndael_Info", b"CTR_ModePolicy", b"CBC_ModePolicy",
                 b"GCM_Base", b"PKCS7_Padding", b"SHA256_Base"],
    "OpenSSL": [b"OPENSSL_", b"SSL_CTX", b"EVP_DecryptInit_ex", b"EVP_CipherInit"],
    "mbedTLS": [b"mbedtls_", b"MBEDTLS_"],
    "libsodium": [b"libsodium", b"crypto_aead_xchacha20poly1305", b"crypto_secretbox"],
    "WindowsCNG": [b"BCryptDecrypt", b"BCryptEncrypt", b"BCryptGenerateSymmetricKey",
                   b"BCryptOpenAlgorithmProvider"],
    "WindowsCryptoAPI": [b"CryptDecrypt", b"CryptEncrypt", b"CryptAcquireContextW",
                         b"CryptDeriveKey"],
    "AES-NI指令": [],  # 通过反汇编统计，见下
}

AESNI_OPCODES = [
    bytes.fromhex("660f38dcaesbox"[:0] + "660f38dc"),  # AESENC
    bytes.fromhex("660f38dd"),  # AESENCLAST
    bytes.fromhex("660f38de"),  # AESDEC
    bytes.fromhex("660f38df"),  # AESDECLAST
]


def scan(path):
    data = open(path, "rb").read()
    out = {
        "file": path.split("\\")[-1],
        "size": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "constants": {},
        "libraries": {},
        "instruction_hints": {},
        "interesting_strings": [],
    }
    for name, sig in CONSTANTS.items():
        idx = data.find(sig)
        out["constants"][name] = idx  # -1 表示未命中

    for lib, sigs in FINGERPRINTS.items():
        hit = [s.decode("latin-1") for s in sigs if s in data]
        if hit:
            out["libraries"][lib] = hit

    ctr = 0
    for op in AESNI_OPCODES:
        c = data.count(op)
        if c:
            ctr += c
    if ctr:
        out["instruction_hints"]["AESENC簇出现次数"] = ctr

    # 与工程加密/许可相关的高信号词
    pat = re.compile(rb"[ -~]{6,120}")
    keys = [b"cipher", b"encrypt", b"decrypt", b"key_store", b"keystore",
            b"aes", b"license", b"activation", b"signature", b"verify",
            b"jypack", b"draft_entryption", b"trial", b"expire", b"serial"]
    seen = set()
    for m in pat.finditer(data):
        s = m.group(0)
        low = s.lower()
        if any(k in low for k in keys):
            if s not in seen:
                seen.add(s)
                out["interesting_strings"].append(s.decode("latin-1"))
                if len(out["interesting_strings"]) >= 400:
                    break
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("binary")
    ap.add_argument("--json")
    a = ap.parse_args()
    r = scan(a.binary)
    text = json.dumps(r, ensure_ascii=False, indent=2)
    if a.json:
        open(a.json, "w", encoding="utf-8").write(text)
        print(f"{r['file']}: 常量命中 {sum(1 for v in r['constants'].values() if v>=0)} 个，"
              f"库指纹 {list(r['libraries'])}，信号串 {len(r['interesting_strings'])} 条")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())