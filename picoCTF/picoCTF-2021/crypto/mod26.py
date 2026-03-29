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


ct = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_45559noq}"
flag = rot13(ct)
print(flag)

