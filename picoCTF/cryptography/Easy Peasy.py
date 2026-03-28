#!/usr/bin/env python3

from pwn import *

context.log_level = 'error'


p = remote("mercury.picoctf.net", 11188)


p.recvuntil(b"flag!\n")
flag_ct = p.recvline().decode().strip()
flag_len = len(flag_ct)//2

payload1 = b"A"*(50000 - flag_len)
p.recvuntil(b"encrypt? ")
p.sendline(payload1)

p.recvuntil(b"encrypt? ")
p.sendline(b"\x00"*32)

p.recvuntil(b"Here ya go!\n")
key = p.recvline().decode().strip()

p.close()

flag = ""
for i in range(32):
    flag += chr(int(key[i*2:i*2+2],16) ^ int(flag_ct[i*2:i*2+2],16))

print("picoCTF{" + flag + "}")
