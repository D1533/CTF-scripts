#!/usr/bin/env python3

from secrets import randbelow
import random
from Crypto.Util.number import *
from sympy.ntheory.modular import crt


def get_prime(n):
    p = 1
    r = random.Random()
    r.seed(randbelow(n))
    while not isPrime(p):
        p = r._randbelow(2**256) | 1
    return p 

with open("output.txt", "r") as f:
    data = f.read()
    n, c = map(lambda x: int(x, 16), data.split())

e = 0x10001
factors = []
c_i = []
for i in range(2,2**16): 
    p = get_prime(i)
    if n % p == 0:
        factors.append(p)
        n //= p

    if len(factors) == 10:
        break


for p_i in factors:
    d_i = pow(e, -1, p_i - 1)
    c_i.append(pow(c, d_i, p_i))

flag = long_to_bytes(crt(factors, c_i)[0]).decode()
print(flag)
