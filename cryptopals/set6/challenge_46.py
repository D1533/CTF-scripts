#!/usr/bin/env python3

from Crypto.Util.number import getPrime, GCD, bytes_to_long, long_to_bytes
import base64
from fractions import Fraction

class Oracle:
    def __init__(self):
        self.e = 65537
        self.p, self.q = self.get_primes()
        self.N = self.p * self.q
        self.d = pow(self.e, -1, (self.p -1)*(self.q-1))

    def get_primes(self):
        while True:
            p = getPrime(1024)
            q = getPrime(1024)
            if GCD(self.e, (p-1)*(q-1)) == 1:
                return p, q
    def encrypt(self, pt):
        return pow(pt, self.e, self.N)

    def is_even(self, ct):
        pt = pow(ct, self.d, self.N)
        return pt % 2 == 0



oracle = Oracle()
pt = base64.b64decode(b"VGhhdCdzIHdoeSBJIGZvdW5kIHlvdSBkb24ndCBwbGF5IGFyb3VuZCB3aXRoIHRoZSBGdW5reSBDb2xkIE1lZGluYQ==")
ct = oracle.encrypt(bytes_to_long(pt))

l = Fraction(0)
h = Fraction(oracle.N)

for _ in range(oracle.N.bit_length()):
    ct = ct * pow(2, oracle.e, oracle.N)
    m = (l + h) / 2
    if oracle.is_even(ct):
        h = m
    else:
        l = m

pt_recovered = long_to_bytes(int(h))
print(pt_recovered)
assert(pt_recovered == pt)
