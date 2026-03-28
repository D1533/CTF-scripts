#!/usr/bin/env python3

from pwn import *
from Crypto.Util.number import long_to_bytes

r = remote("wily-courier.picoctf.net", 62843)

r.recvuntil(b"flag!\n")
flag_ct = r.recvline().decode().strip()
flag_len = len(flag_ct)//2

payload1 = b"A"*(50000 - flag_len)
r.recvuntil(b"encrypt? ")
r.sendline(payload1)

r.recvuntil(b"encrypt? ")
r.sendline(b"\x00"*32)

r.recvuntil(b"Here ya go!\n")
key = r.recvline().decode().strip()

r.close()

flag = b"picoCTF{" + long_to_bytes(int(key,16) ^ int(flag_ct, 16)) + b"}"
print(flag.decode())
