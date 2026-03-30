#!/usr/bin/env python3

from pwn import *
from hashlib import sha256

def get_hash(r, m):
    r.sendlineafter(b">", b"1") 
    r.sendline(m)
    r.recvuntil(b"Hash: ")
    hsh = r.recvline().strip().decode()
    return hsh

host, port = sys.argv[1].split(":")
r = remote(host, port)

flag = b""
for i in range(64):
    m = b"\x00"*i
    hsh = get_hash(r, m)
    for b in range(256):
        hsh_test = sha256(flag + b.to_bytes(1)).digest().hex()
        if hsh_test == hsh:
            flag += b.to_bytes(1)
            break
print(flag.decode())
