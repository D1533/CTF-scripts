#!/usr/bin/env python3

from pwn import *

host, port = sys.argv[1].split(":")
io = remote(host, port)

io.sendlineafter(b">", b"4")
io.recvuntil(b"p = ")
p = int(io.recvline().strip().decode())
io.recvuntil(b"q = ")
q = int(io.recvline().strip().decode())
io.recvuntil(b"g = ")
g = int(io.recvline().strip().decode())

io.sendlineafter(b"Test user log (y/n): ", b"y")
io.sendlineafter(b"Enter your password : ", b"5up3r_53cur3_P45sw0r6")


io.recvline()
data = eval(io.recvline().strip().decode())
(r, s), H = data[5]

k = 65500
while True:
    if r == pow(g, k, p) % q:
        break
    k += 1
 

x = ((s*k - int(H,16)) * pow(r,-1,q)) % q

io.sendlineafter(b">", b"3")
io.sendlineafter(b": ", b"ElGamalSux")
io.sendlineafter(b": ", b"3")
io.sendlineafter(b": ", str(k).encode())
io.sendlineafter(b": ", str(x).encode())

io.recvuntil(b": ")
flag = io.recvline().decode()

print(flag)
