#!/usr/bin/env python3

from pwn import *
from Crypto.Util.number import long_to_bytes


host, port = sys.argv[1].split(":")
io = remote(host, port)
io.recvuntil(b'n: ')
n = int(io.recvline().strip().decode())
io.recvuntil(b'e: ')
e = int(io.recvline().decode())
io.recvuntil(b'ciphertext: ')
ciphertext = int(io.recvline().strip().decode())


payload = (pow(2,e,n)*ciphertext) % n

io.sendlineafter(b'Give me ciphertext to decrypt: ', str(payload).encode())

io.recvuntil(b'Here you go: ')
m = int(io.recvline().strip().decode())
flag = (pow(2,-1,n)*m) % n
print(long_to_bytes(flag).decode())


