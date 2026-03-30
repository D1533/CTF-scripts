#!/usr/bin/env python3

from pwn import *
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes

msg = b"Initialization Sequence - Code 0"


def encrypt(msg, shared_secret):
    key = hashlib.md5(long_to_bytes(shared_secret)).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(msg)


host, port = sys.argv[1].split(":")
io = remote(host, port)

io.sendlineafter(b"Enter The Public Key of The Memory: ", b"1")
enc_msg = encrypt(msg, 1)
io.sendlineafter(b"Enter The Encrypted Initialization Sequence: ", enc_msg.hex().encode())
io.recvuntil(b"DEBUG MSG - ")
io.recvuntil(b"DEBUG MSG - ")
flag = io.recvline().decode()
print(flag)



