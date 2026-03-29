#!/usr/bin/env python3

ct = "xqkwKBN{z0bib1wv_l3kzgxb3l_4k71n5j0}"

for key in range(26):
    flag = ""
    for c in ct:
        if c.islower():
            base = ord('a')
            flag += chr( (ord(c) - base + key) % 26 + base)
        elif c.isupper():
            base = ord('A')
            flag += chr( (ord(c) - base + key) % 26 + base)

        else:
            flag += c

    if "picoCTF{" in flag:
        print(flag)


