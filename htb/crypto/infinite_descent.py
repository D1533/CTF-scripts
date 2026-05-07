#!/usr/bin/env python3

from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes
from math import isqrt
import base64

class mersenne(object):
    def __init__(self, seed):
        # Initialize the index to 0
        self.index = 624
        self.mt = [0] * 624
        self.mt[0] = seed  # Initialize the initial state to the seed
        for i in range(1, 624):
            initval = int(0xFFFFFFFF & (1812433253 * (self.mt[i - 1] ^ self.mt[i - 1] >> 30) + i))
            # print(initval)
            self.mt[i] = initval

    def extract_number(self):
        if self.index >= 624:
            self.twist()

        y = self.mt[self.index]

        # Right shift by 11 bits
        y = y ^ y >> 11
        # Shift y left by 7 and take the bitwise and of 2636928640
        y = y ^ y << 7 & 2636928640
        # Shift y left by 15 and take the bitwise and of y and 4022730752
        y = y ^ y << 15 & 4022730752
        # Right shift by 18 bits
        y = y ^ y >> 18

        self.index = self.index + 1

        return int(0xFFFFFFFF & y)

    def twist(self):
        for i in range(624):
            # Get the most significant bit and add it to the less significant
            # bits of the next number
            y = int(0xFFFFFFFF & ((self.mt[i] & 0x80000000) + (self.mt[(i + 1) % 624] & 0x7fffffff)))
            self.mt[i] = self.mt[(i + 397) % 624] ^ y >> 1

            if y % 2 != 0:
                self.mt[i] = self.mt[i] ^ 0x9908b0df
        self.index = 0
        #test

def gen_and_check(genseed):
    x = mersenne(genseed)
    y = (x.extract_number() & 0xFF) 
    return y 


def fermat_factor(n):
    a = isqrt(n)
    if a*a < n:
        a += 1
    while True:
        b2 = a*a - n
        b = isqrt(b2)

        if b*b == b2:
            p = a - b
            q = a + b
            return p, q
        a += 1

pem = b"""-----BEGIN PUBLIC KEY-----
MIGeMA0GCSqGSIb3DQEBAQUAA4GMADCBiAKBgFbDk+zYy1tbjwPpsTWbYjIfBtZk
walARbJxLg6QhyalsGnBx064VFIH9XIKzPK/Dt1RzMO68gy7zLOiyipPtYb2n0M6
WcdDGgw9J9+xx4HjXZCHx4h4zQhfQeOYymeSPewXJOe+GT31ymz6/Q1Ulyq/jWnD
XZogxfbXi6bIwuN7AgMBAAE=
-----END PUBLIC KEY-----
"""
c = 41296290787170212566581926747559000694979534392034439796933335542554551981322424774631715454669002723657175134418412556653226439790475349107756702973735895193117931356004359775501074138668004417061809481535231402802835349794859992556874148430578703014721700812262863679987426564893631600671862958451813895661


key = RSA.import_key(pem)
n = key.n
e = key.e

p, q = fermat_factor(n)
phi = (p-1)*(q-1)
d = pow(e, -1, phi)
seed = str(pow(c, d, n))

flag = ''
for i in range(0, len(seed), 3):
    seedval = int(seed[i:i+3])
    bin_char = str(bin(gen_and_check(seedval)))[2::].zfill(8)
    flag += chr(int(bin_char, 2))

flag = b"HTB{" + base64.b64decode(flag).split(b'=')[-1] + b"}"
print(flag)



