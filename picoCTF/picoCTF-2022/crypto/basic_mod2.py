#!/usr/bin/env python3


numbers = [104, 372, 110, 436, 262, 173, 354, 393, 351, 297, 241, 86, 262, 359, 256, 441, 124, 154, 165, 165, 219, 288, 42]
flag = ""

for n in numbers:
    c = pow(n, -1, 41)
    if c <= 26:
        flag += chr(c - 1 + ord('A'))
    elif c <= 36:
        flag += str(c - 27)
    else:
        flag += "_"

flag = "picoCTF{" + flag + "}"
print(flag)
