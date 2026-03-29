#!/usr/bin/env python3

import base64

def caesar_decipher(ct, k):
    pt = ""
    for c in ct:
        if c.islower():
            base = ord('a')
            pt += chr((ord(c) - base - k ) % 26 + base)
        elif c.isupper():
            base = ord('A')
            pt += chr((ord(c) - base - k ) % 26 + base)
        else:
            pt += c
    return pt


ct = "YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgya3lNRFJvYTJvMmZRPT0nCg=="

ct = eval(base64.b64decode(ct).decode())
ct = base64.b64decode(ct).decode()

for k in range(26):
    flag = caesar_decipher(ct, k)
    if "picoCTF{" in flag:
        print(flag)
        break

