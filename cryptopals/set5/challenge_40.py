#!/usr/bin/env python3


from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
from sympy.ntheory.modular import crt
from sympy import root

import os


N = []
for _ in range(3):
    p = getPrime(1024)
    q = getPrime(1024)
    n = p*q
    N.append(n)

e = 3


m = os.urandom(32)
C = []
for i in range(3):
    C.append(pow(bytes_to_long(m), e, N[i]))

M, mod = crt(N, C)

assert(long_to_bytes(root(M, 3)) ==  m)


