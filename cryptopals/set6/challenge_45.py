#!/usr/bin/env python3

from enum import verify
from hashlib import sha1
from Crypto.Util.number import getPrime
from random import randint
import os

class DSA:
    def __init__(self):
        self.H = sha1
        self.p = int('800000000000000089e1855218a0e7dac38136ffafa72eda7'
                    '859f2171e25e65eac698c1702578b07dc2a1076da241c76c6'
                    '2d374d8389ea5aeffd3226a0530cc565f3bf6b50929139ebe'
                    'ac04f48c3c84afb796d61e5a4f9a8fda812ab59494232c7d2'
                    'b4deb50aa18ee9e132bfa85ac4374d7f9091abc3d015efc87'
                    '1a584471bb1', 16)

        self.q = int('f4f47f05794b256174bba6e9b396a7707e563c5b', 16)
        self.g = int('5958c9d3898b224b12672c0b98e06c60df923cb8bc999d119'
            '458fef538b8fa4046c8db53039db620c094c9fa077ef389b5'
            '322a559946a71903f990f1f7e0e025e2d7f7cf494aff1a047'
            '0f5b64c36b625a097f1651fe775323556fe00b3608c887892'
            '878480e99041be601a62166ca6894bdd41a7054ec89f756ba'
            '9fc95302291', 16)
        
        self.x = None
        self.y = None

    def gen_pubkey(self):
        self.x = randint(1, self.q - 1)
        y = pow(self.g, self.x, self.p)
        return y

    def sign(self, m):
        while True:
            k = randint(1, self.q - 1)
            r = (pow(self.g, k, self.p)) % self.q
            h = int(self.H(m).hexdigest(), 16)
            s = (pow(k, -1, self.q)*(h + self.x*r)) % self.q
            if s != 0:
                return r, s

    def verify(self,y, m, r, s):
        h = int(self.H(m).hexdigest(), 16)
        w = pow(s, -1, self.q)
        u1 = (h*w) % self.q 
        u2 = (r*w) % self.q
        v = ((pow(self.g, u1, self.p)*pow(y, u2, self.p) ) % self.p ) % self.q
        print(v)
        return v == r

# g = 0 => r = 0  = v for any msg 
m = os.urandom(32)
dsa = DSA()
dsa.g = 0 # Attack
y = dsa.gen_pubkey()
r, s = dsa.sign(m) 
assert(dsa.verify(y, m, r, s) == True)
assert(dsa.verify(y, os.urandom(32), r, s) == True) # Can validate every msg

# g = p+1 => r = 1 
m = os.urandom(32)
dsa = DSA()
dsa.g = dsa.p + 1 # Attack
y = dsa.gen_pubkey()
r, s = dsa.sign(m) 
assert(dsa.verify(y, m, r, s) == True)

z = randint(1, dsa.p)
r = pow(y, z, dsa.p) % dsa.q
s = (r*pow(z, -1, dsa.q)) % dsa.q
assert(dsa.verify(y, os.urandom(32), r, s) == True) # Can validate every msg


