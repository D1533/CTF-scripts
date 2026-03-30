#!/usr/bin/env python3

from sage.all import *
from Crypto.Util.number import long_to_bytes

p = 307163712384204009961137975465657319439
g = 1337

with open("output.txt", "r") as f:
    data = eval(f.read())


flag = ""
for h in data:
    l = legendre_symbol(h, p)

    if l == 1:
        flag += "0"
    else:
        flag += "1"


flag = long_to_bytes(int(flag, 2)).decode()
print(flag)


