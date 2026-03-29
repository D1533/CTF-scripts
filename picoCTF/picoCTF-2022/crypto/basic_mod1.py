#!/usr/bin/env python3

numbers = [128, 322, 353, 235, 336, 73, 198, 332, 202, 285, 57, 87, 262, 221, 218, 405, 335, 101, 256, 227, 112, 140]

flag = ""
for n in numbers:
    c = n % 37
    if c <= 25:
        flag += chr(c + ord('A'))
    elif c <= 35:
        flag += str(c - 26)
    else:
        flag += "_"

flag = "picoCTF{" + flag + "}"
print(flag)
