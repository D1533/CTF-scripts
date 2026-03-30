#!/usr/bin/env python3

from pwn import *

# This was found in a paper
p = 29674495668685510550154174642905332730771991799853043350995075531276838753171770199594238596428121188033664754218345562493168782883
n = p*(313*(p-1)+1)*(353*(p-1)+1) 

host, port = sys.argv[1].split(":")
io = remote(host, port)
io.recvuntil(b"Give p: ")

io.sendline(str(n).encode())
flag = io.recvline().decode()
print(flag)
