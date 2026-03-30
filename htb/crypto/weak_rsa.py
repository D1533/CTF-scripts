#!/usr/bin/env python3

from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes
import owiener

with open("key.pub", "rb") as f:
    key = RSA.import_key(f.read())

with open("flag.enc", "rb") as f:
    c = bytes_to_long(f.read())

n = key.n
e = key.e

d = owiener.attack(e, n)
m = pow(c, d, n)
flag = long_to_bytes(m)

print(flag)

