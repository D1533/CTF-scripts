#!/usr/bin/env python3

from pwn import *
from Crypto.Util.number import long_to_bytes
import owiener

r = remote("wily-courier.picoctf.net", 51488)

r.recvuntil(b"e: ")
e = int(r.recvline().strip().decode())
r.recvuntil(b"n: ")
n = int(r.recvline().strip().decode())
r.recvuntil(b"c: ")
c = int(r.recvline().strip().decode())

r.close()

d = owiener.attack(e, n)
m = pow(c, d, n)
flag = long_to_bytes(m).decode()
print(flag)

