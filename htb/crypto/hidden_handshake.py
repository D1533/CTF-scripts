#!/usr/bin/env python3

from pwn import *
from Crypto.Util.number import long_to_bytes, bytes_to_long

host, port = sys.argv[1].split(":")
io = remote(host, port)

s2 = b"A"*8
user1 = "B"*1336
io.sendlineafter(b"Enter your secure access key: ", s2)
io.sendlineafter(b"Enter your Agent Codename: ", user1.encode())
io.recvuntil(b"Encrypted transmission: ")
ct1 = bytes.fromhex(io.recvline().strip().decode())


io.sendlineafter(b"Enter your secure access key: ", s2)
io.sendlineafter(b"Enter your Agent Codename: ", b"B"*1)
io.recvuntil(b"Encrypted transmission: ")
ct2 = bytes.fromhex(io.recvline().strip().decode())


pt = f"Agent {user1}, your clearance for Operation Blackout is: ".encode()
pt2 = b""
for i in range(13):
    pt2 += long_to_bytes(bytes_to_long(ct2[8*i:8*(i+1)]) ^ bytes_to_long(pt[8*i:8*(i+1)]) ^ bytes_to_long(ct1[8*i:8*(i+1)]))

print(pt2.decode())


