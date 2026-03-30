#!/usr/bin/env python3

from sage.all import *
from Crypto.Util.number import long_to_bytes
from itertools import combinations
from pwn import *

e = 65537

host, port = sys.argv[1].split(":")
io = remote(host, port)
io.recvuntil(b'anger = ')
c = int(io.recvline().strip())
io.recvuntil(b'envy = ')
d = int(io.recvline().strip())

divisors = divisors(e*d-1)
primes = [int(d+1) for d in divisors if (d <= 2**128 - 1) and is_prime(d+1)]

for p, q in combinations(primes, 2):
    phi = (p-1)*(q-1)
    n = p*q
    if pow(e,-1,phi) == d:
        try:
            vainglory = long_to_bytes(pow(c,d,n)).decode()
            break
        except:
            pass

io.sendlineafter(b"> ", vainglory.encode())
io.recvuntil(b"Conquered!").decode()
flag = io.recv().decode()
print(flag)
