#!/usr/bin/env python3

from pwn import *


host, port = sys.argv[1].split(":")
r = remote(host, port)

r.sendlineafter(b"username: ", b"admin")
r.sendlineafter(b"password: ", b"\x000ld3n_b0y")
r.recvuntil(b"ciphertext: ")
ct = r.recvline()[:-1].decode()

ct = bytearray(bytes.fromhex(ct))

ct[15] ^= ord('g')

r.sendlineafter(b"ciphertext: ", ct.hex().encode())
r.recvuntil(b"Your flag is: ")

flag = r.recv().decode()
print(flag)


