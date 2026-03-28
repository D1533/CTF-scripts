#!/usr/bin/env python3

from sage.all import *
from pwn import *
from Crypto.Util.number import long_to_bytes

r = remote("fickle-tempest.picoctf.net", 60059)

r.recvuntil(b"c: ")
c = int(r.recvline().strip().decode())
r.recvuntil(b"n: ")
n = int(r.recvline().strip().decode())
r.recvuntil(b"e: ")
e = int(r.recvline().strip().decode())


factors = factor(n)
assert(all(e_i == 1 for p, e_i in factors))
phi = 1
for p, _ in factors:
    phi *= (p-1)

d = int(pow(e,-1, int(phi)))
flag = long_to_bytes(pow(c,d,n)).decode()
print(flag)

