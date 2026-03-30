#!/usr/bin/env python3

from pwn import *
from Crypto.Util.number import long_to_bytes

host, port = sys.argv[1].split(":")
io = remote(host, port)

io.recvuntil(b"q : ")
q = int(io.recvline().strip().decode())
io.recvuntil(b"p : ")
p = int(io.recvline().strip().decode())
io.sendlineafter(b":", b"Y")
io.sendlineafter(b"n: ", str(p*q).encode())

io.recvuntil(b"p : ")
p = int(io.recvline().strip().decode())
io.recvuntil(b"n : ")
n = int(io.recvline().strip().decode())
io.sendlineafter(b":", b"Y")
io.sendlineafter(b"q: ", str(n//p).encode())

io.sendlineafter(b"(Y/N):", b"N")

io.recvuntil(b"q : ")
q = int(io.recvline().strip().decode())
io.recvuntil(b"p : ")
p = int(io.recvline().strip().decode())
io.sendlineafter(b":", b"Y")
io.sendlineafter(b"totient(n):", str((p-1)*(q-1)).encode())

io.recvuntil(b"plaintext : ")
m = int(io.recvline().strip().decode())
io.recvuntil(b"e : ")
e = int(io.recvline().strip().decode())
io.recvuntil(b"n : ")
n = int(io.recvline().strip().decode())
io.sendlineafter(b":", b"Y")
io.sendlineafter(b"ciphertext:", str(pow(m,e,n)).encode())

io.sendlineafter(b"(Y/N):", b"N")

io.recvuntil(b"q : ")
q = int(io.recvline().strip().decode())
io.recvuntil(b"p : ")
p = int(io.recvline().strip().decode())
io.recvuntil(b"e : ")
e = int(io.recvline().strip().decode())
io.sendlineafter(b":", b"Y")
io.sendlineafter(b"d:", str(pow(e,-1,(p-1)*(q-1))).encode())

io.recvuntil(b"p : ")
p = int(io.recvline().strip().decode())
io.recvuntil(b"ciphertext : ")
c = int(io.recvline().strip().decode())
io.recvuntil(b"e : ")
e = int(io.recvline().strip().decode())
io.recvuntil(b"n : ")
n = int(io.recvline().strip().decode())

q = n // p
d = pow(e,-1,(p-1)*(q-1))
m = pow(c,d,n)
flag = long_to_bytes(m).decode()
print(flag)



