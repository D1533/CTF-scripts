#!/usr/bin/env python3

from pwn import *
from Crypto.Util.number import long_to_bytes

r = remote("wily-courier.picoctf.net", 54701)
r.recvuntil(b'n: ')
n = int(r.recvline().strip().decode())
r.recvuntil(b'e: ')
e = int(r.recvline().decode())
r.recvuntil(b'ciphertext: ')
ciphertext = int(r.recvline().strip().decode())


payload = (pow(2,e,n)*ciphertext) % n

r.sendlineafter(b'Give me ciphertext to decrypt: ', str(payload).encode())

r.recvuntil(b'Here you go: ')
m = int(r.recvline().strip().decode())
flag = (pow(2,-1,n)*m) % n
print(long_to_bytes(flag).decode())


