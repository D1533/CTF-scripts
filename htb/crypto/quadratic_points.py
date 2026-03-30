#!/usr/bin/env python3

from sage.all import *
from pwn import *
from itertools import product
from Crypto.Util.number import long_to_bytes

def find_coeff(r1):
    for a, b, c in product(range(-60, 60), repeat = 3):
        if a == 0 or b == 0 or c == 0:
            continue

        if abs(a*r1**2 + b*r1 + c) < 1e-13:
            return a, b, c

host, port = sys.argv[1].split(":")
remainders = []
moduli = []
while True:
    io = remote(host, port)

    for _ in range(7):
        io.recvuntil(b"x = ")
        r1 = float(io.recvline().strip().decode())

        a, b, c = find_coeff(r1)     
        
        io.sendlineafter(b"a: ", str(a).encode())
        io.sendlineafter(b"b: ", str(b).encode())
        io.sendlineafter(b"c: ", str(c).encode())

    io.recvuntil(b"G = ")
    G = eval(io.recvline().strip())
    io.recvuntil(b"Gn = ")
    Q = eval(io.recvline().strip())
    io.recvuntil(b"p = ")
    p = int(io.recvline().strip())

    io.close()
    
    E = EllipticCurve(GF(p), [b, c])
    G = E(G)
    Q = E(Q)
    n = G.discrete_log(Q)
    
    remainders.append(n)
    moduli.append(G.order())
    n = crt(remainders, moduli)
    flag = long_to_bytes(n)
    if b"HTB{" in flag:
        print(flag.decode())
        break
   







