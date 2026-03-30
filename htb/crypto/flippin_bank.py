#!/usr/bin/env python3

from pwn import *


host, port = sys.argv[1].split(":")
io = remote(host, port)

io.sendlineafter(b"username: ", b"admin")
io.sendlineafter(b"password: ", b"\x000ld3n_b0y")
io.recvuntil(b"ciphertext: ")
ct = io.recvline()[:-1].decode()

ct = bytearray(bytes.fromhex(ct))

ct[15] ^= ord('g')

io.sendlineafter(b"ciphertext: ", ct.hex().encode())
io.recvuntil(b"Your flag is: ")

flag = io.recv().decode()
print(flag)


