#!/usr/bin/env python3

from Crypto.Cipher import AES
import base64

def xor(s1, s2):
    return bytes([a ^ b for a, b in zip(s1, s2)])


def ctr_encrypt(key, nonce, pt):
    cipher = AES.new(key, AES.MODE_ECB)
    count = 0 
    ct = b""
    for i in range(0, len(pt), 16):
        c_i = cipher.encrypt(nonce + count.to_bytes(8, 'little'))
        ct += xor(pt[i:i+16], c_i)
        count += 1
    return ct


ct = base64.b64decode("L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==")
key = b"YELLOW SUBMARINE"
nonce = b"\x00"*8

print(ctr_encrypt(key, nonce, ct))






