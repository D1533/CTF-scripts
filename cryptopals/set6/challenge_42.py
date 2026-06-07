#!/usr/bin/env python3

from Crypto.Util.number import GCD, getPrime, bytes_to_long, long_to_bytes
import os
from hashlib import sha256
import gmpy2


asn1 = bytes.fromhex("3031300d060960864801650304020105000420") 
BLOCK_SIZE = 256

class Signer():
    def __init__(self):
        self.e = 3
        self.p, self.q = self.get_primes()
        self.N = self.p * self.q
        self.d = pow(self.e, -1 , (self.p - 1)*(self.q - 1))
        self.msg = os.urandom(32)
        self.signature = None

    def get_primes(self):
        while True:
            p = getPrime(1024)
            q = getPrime(1024)
            if GCD(self.e, (p-1)*(q-1)) == 1:
                return p, q

    def sign(self):
        h = sha256(self.msg).digest()
        m = b"\x00\x01" + b"\xff" * (BLOCK_SIZE - len(asn1 + h) - 3) + b"\x00" + asn1 + h
        self.signature = pow(bytes_to_long(m), self.d , self.N)


class Verifier():
    def __init__(self, N, e):
        self.N = N
        self.e = e

    def verify(self, s, msg):
        m = long_to_bytes(pow(s, self.e, self.N), BLOCK_SIZE)
        h = sha256(msg).digest()
        # Vulnerability
        if b"\x00\x01" not in m:
            return False
        
        if b"\x00" not in m:
            return False

        if asn1 + h not in m:
            return False

        return True


# Test
signer = Signer()
verifier = Verifier(signer.N, signer.e)
signer.sign()
assert(verifier.verify(signer.signature, signer.msg) == True)

# Attack: forge a valid signature without d
h = sha256(b"hi mom").digest()
m = b"\x00\x01\xff\xff\x00" + asn1 + h
m = bytes_to_long(m + b"\x01" * (BLOCK_SIZE - len(m)))
s = gmpy2.iroot(m, 3)[0]

assert(verifier.verify(s, b"hi mom") == True)











