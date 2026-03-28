#!/usr/bin/env python3

def rot13(ct):
    pt = ""
    for c in ct:
        if 'a' <= c <= 'z':
            pt += chr( (ord(c) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= c <= 'Z':
            pt += chr( (ord(c) - ord('A') + 13) % 26 + ord('A'))
        else:
            pt += c
    return pt

ct = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"
flag = rot13(ct)
print(flag)
