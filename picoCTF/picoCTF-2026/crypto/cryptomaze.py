#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

state = [0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1]
taps = [63, 61, 60, 58]
ct = bytes.fromhex("8f0e6d0f5b0dc1db201948b9e0cebd8f4e0f7cb6a86d4243f62f1438e07a632c38338e7e04fbddef0c6260a4eb758417")


key_int = 0
for _ in range(128):
    key_int = (key_int << 1) + state[0]  
    feedback = state[63] ^ state[61] ^ state[60] ^ state[58]
    state = state[1:] + [feedback]

key = key_int.to_bytes(16, "big")
cipher = AES.new(key, AES.MODE_ECB)
flag = unpad(cipher.decrypt(ct), 16).decode()

print(flag)

