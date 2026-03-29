#!/usr/bin/env python3


key = "CYLAB"
ct = "rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_2951c89f}"
flag = ""

for i, c in enumerate(ct):
    shift = ord(key[i % len(key)]) - ord('A')
    if c.islower():
        base = ord('a')
        flag += chr( (ord(c) - base - shift) % 26 + base)
    elif c.isupper():
        base = ord('A')
        flag += chr( (ord(c) - base - shift) % 26 + base)
    else:
        flag += c

print(flag)
    








