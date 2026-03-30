#!/usr/bin/env python3

from pwn import *
from sage.all import *
from Crypto.PublicKey import RSA

host, port = sys.argv[1].split(":")
io = remote(host, port)

for _ in range(5):
    io.recvuntil(b"-----BEGIN PUBLIC KEY-----")
    pem = b"-----BEGIN PUBLIC KEY-----\n"
    pem += io.recvuntil(b"-----END PUBLIC KEY-----")
    
    key = RSA.import_key(pem)

    n = key.n
    print(n)
    factors = factor(n)
    p = factors[0][0]
    q = factors[1][0]

    io.sendline(str(p).encode())
    io.sendline(str(q).encode())

io.interactive()
