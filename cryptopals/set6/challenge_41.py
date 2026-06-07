#!/usr/bin/env python3


from Crypto.Util.number import getPrime, long_to_bytes, bytes_to_long
from hashlib import sha256
from random import randint
import os

class Oracle:
    def __init__(self):
        self.p = getPrime(1024)
        self.q = getPrime(1024)
        self.N = self.p*self.q
        self.e = 65537
        self.d = pow(self.e, -1, (self.p - 1)*(self.q - 1))
        self.hashes = []
    
    def decrypt(self, ct):
        h = sha256(long_to_bytes(ct)).digest()
        if h in self.hashes:
            return None

        self.hashes.append(h)
        return long_to_bytes(pow(ct, self.d, self.N))
    
    def encrypt(self, pt):
        return pow(bytes_to_long(pt), self.e, self.N)


oracle = Oracle()
priv_msg = os.urandom(32)
ct = oracle.encrypt(priv_msg)
pt = oracle.decrypt(ct)
assert(pt == priv_msg)

assert(oracle.decrypt(ct) == None) # Attacker cannot decrypt it

C = randint(2, oracle.N)
ct_payload = (ct * pow(C, oracle.e, oracle.N) ) % oracle.N
pt_ = oracle.decrypt(ct_payload)
pt_recovered = (bytes_to_long(pt_) * pow(C, -1, oracle.N)) % oracle.N
assert(long_to_bytes(pt_recovered) == pt)






