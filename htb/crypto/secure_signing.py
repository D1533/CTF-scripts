#!/usr/bin/env python3

from pwn import *
from hashlib import sha256

def get_hash(io, m):
    io.sendlineafter(b">", b"1") 
    io.sendline(m)
    io.recvuntil(b"Hash: ")
    hsh = io.recvline().strip().decode()
    return hsh

host, port = sys.argv[1].split(":")
io = remote(host, port)

flag = b""
for i in range(64):
    m = b"\x00"*i
    hsh = get_hash(io, m)
    for b in range(256):
        hsh_test = sha256(flag + b.to_bytes(1)).digest().hex()
        if hsh_test == hsh:
            flag += b.to_bytes(1)
            break
print(flag.decode())
