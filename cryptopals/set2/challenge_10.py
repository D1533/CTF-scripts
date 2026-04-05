#!/usr/bin/env python3

from Crypto.Cipher import AES
import base64

def xor(s1, s2):
    return bytes([a ^ b for a, b in zip(s1, s2)])

def aes_cbc_decrypt(iv, key, ct):
    cipher = AES.new(key, AES.MODE_ECB)

    pt = b"" 
    ct_prev = iv
    for i in range(len(ct) // 16):
        pt += xor(cipher.decrypt(ct[i*16:(i+1)*16]), ct_prev)
        ct_prev = ct[i*16:(i+1)*16]

    return pt


iv = b"\x00"*16
key = b"YELLOW SUBMARINE"

with open("10.txt", "r") as f: # https://cryptopals.com/static/challenge-data/10.txt
    data = f.read()

ct = base64.b64decode(data)
pt = aes_cbc_decrypt(iv, key, ct)
print(pt.decode())

