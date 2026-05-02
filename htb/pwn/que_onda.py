#!/usr/bin/env python3

from pwn import *
import sys

def exploit(io):
    
    io.sendlineafter(b"$ ", b"flag")
    flag = io.recv().decode()
    print(flag)


def main():
    HOST, PORT = sys.argv[1].split(":")
    io = remote(HOST, PORT)
    exploit(io)


if __name__ == "__main__":
    main()
