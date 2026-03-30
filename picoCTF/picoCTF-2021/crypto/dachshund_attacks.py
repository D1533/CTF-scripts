#!/usr/bin/env python3

from pwn import *
from Crypto.Util.number import long_to_bytes
import owiener

host, port = sys.argv[1].split(":")
io = remote(host, port)

io.recvuntil(b"e: ")
e = int(io.recvline().strip().decode())
io.recvuntil(b"n: ")
n = int(io.recvline().strip().decode())
io.recvuntil(b"c: ")
c = int(io.recvline().strip().decode())

io.close()

d = owiener.attack(e, n)
m = pow(c, d, n)
flag = long_to_bytes(m).decode()
print(flag)

