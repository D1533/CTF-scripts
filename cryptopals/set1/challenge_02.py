#!/usr/bin/env python3

def xor(s1, s2):
    return bytes([a ^ b for a, b in zip(s1, s2)])

s1 = bytes.fromhex("1c0111001f010100061a024b53535009181c")
s2 = bytes.fromhex("686974207468652062756c6c277320657965")

s = xor(s1, s2).hex()
print(s)
