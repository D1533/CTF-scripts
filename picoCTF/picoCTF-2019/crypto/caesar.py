#!/usr/bin/env python3


def caesar_cipher(ct, k):
    pt = ""
    for c in ct:
        pt += chr( (ord(c) - ord('a') + k) % 26 + ord('a'))
    return pt
   
ct = "rgdhhxcviwtgjqxrdcbxpotman"

for k in range(26):
    flag = "picoCTF{" + caesar_cipher(ct, k) + "}"
    print(flag)
