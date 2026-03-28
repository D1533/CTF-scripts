#!/usr/bin/env python3

from pwn import *
from Crypto.Util.number import long_to_bytes

r = remote("fickle-tempest.picoctf.net", 53925)

r.recvuntil(b"q : ")
q = int(r.recvline().strip().decode())
r.recvuntil(b"p : ")
p = int(r.recvline().strip().decode())
r.sendlineafter(b":", b"Y")
r.sendlineafter(b"n: ", str(p*q).encode())

r.recvuntil(b"p : ")
p = int(r.recvline().strip().decode())
r.recvuntil(b"n : ")
n = int(r.recvline().strip().decode())
r.sendlineafter(b":", b"Y")
r.sendlineafter(b"q: ", str(n//p).encode())

r.sendlineafter(b"(Y/N):", b"N")

r.recvuntil(b"q : ")
q = int(r.recvline().strip().decode())
r.recvuntil(b"p : ")
p = int(r.recvline().strip().decode())
r.sendlineafter(b":", b"Y")
r.sendlineafter(b"totient(n):", str((p-1)*(q-1)).encode())

r.recvuntil(b"plaintext : ")
m = int(r.recvline().strip().decode())
r.recvuntil(b"e : ")
e = int(r.recvline().strip().decode())
r.recvuntil(b"n : ")
n = int(r.recvline().strip().decode())
r.sendlineafter(b":", b"Y")
r.sendlineafter(b"ciphertext:", str(pow(m,e,n)).encode())

r.sendlineafter(b"(Y/N):", b"N")

r.recvuntil(b"q : ")
q = int(r.recvline().strip().decode())
r.recvuntil(b"p : ")
p = int(r.recvline().strip().decode())
r.recvuntil(b"e : ")
e = int(r.recvline().strip().decode())
r.sendlineafter(b":", b"Y")
r.sendlineafter(b"d:", str(pow(e,-1,(p-1)*(q-1))).encode())

r.recvuntil(b"p : ")
p = int(r.recvline().strip().decode())
r.recvuntil(b"ciphertext : ")
c = int(r.recvline().strip().decode())
r.recvuntil(b"e : ")
e = int(r.recvline().strip().decode())
r.recvuntil(b"n : ")
n = int(r.recvline().strip().decode())

q = n // p
d = pow(e,-1,(p-1)*(q-1))
m = pow(c,d,n)
flag = long_to_bytes(m).decode()
print(flag)



