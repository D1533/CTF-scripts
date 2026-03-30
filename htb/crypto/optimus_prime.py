#!/usr/bin/env python3

from pwn import *
from Crypto.Util.number import long_to_bytes
from math import gcd


host, port = sys.argv[1].split(":")
io = remote(host, port)

io.sendline(b"4")
io.recvuntil(b"PUBLIC KEY: ")
n1 = int(io.recvline().decode())
io.close()


io = remote(host, port)

io.sendline(b"4")
io.recvuntil(b"PUBLIC KEY: ")
n2 = int(io.recvline())

io.recvuntil(b"ENCRYPTED PASSWORD: ")
ct = int(io.recvline())

p = gcd(n1,n2)
q = n2 // p
e = 65537

phi = (p-1)*(q-1)
d = pow(e, -1, phi)

password = pow(ct, d, n2)

io.sendline(long_to_bytes(password))

io.recvuntil(b'ACCESS GRANTED: ')
flag = io.recvline().decode()

print(flag)
