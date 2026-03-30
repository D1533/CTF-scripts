#!/usr/bin/env python3

from pwn import *
from Crypto.Util.number import long_to_bytes

host, port = sys.argv[1].split(":")
io = remote(host, port)

io.recvuntil(b"flag!\n")
flag_ct = io.recvline().decode().strip()
flag_len = len(flag_ct)//2

payload1 = b"A"*(50000 - flag_len)
io.recvuntil(b"encrypt? ")
io.sendline(payload1)

io.recvuntil(b"encrypt? ")
io.sendline(b"\x00"*32)

io.recvuntil(b"Here ya go!\n")
key = io.recvline().decode().strip()

io.close()

flag = b"picoCTF{" + long_to_bytes(int(key,16) ^ int(flag_ct, 16)) + b"}"
print(flag.decode())
