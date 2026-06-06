#!/usr/bin/env python3


from Crypto.Util.number import getPrime, long_to_bytes
from Crypto.Cipher import AES
import hashlib
import random
import os

class Alice:
    def __init__(self):
        self.p = getPrime(1024)
        self.a = random.randint(1, self.p)
        self.g = 2
        self.A = pow(self.g, self.a, self.p)
        self.B = None
        self.s = None
        self.msg = os.urandom(32) 
        self.ct = None
        self.iv = os.urandom(16)
        
    def send_parameters(self, Bob):
        Bob.p = self.p
        Bob.g = self.g
        Bob.A = self.A

    def receive_pubkey(self, Bob):
        self.B = Bob.B

    def compute_secret(self):
        self.s = hashlib.sha1(long_to_bytes(pow(self.B, self.a, self.p))).digest()[:16]

    def encrypt_msg(self):
        cipher = AES.new(self.s, AES.MODE_CBC, self.iv)
        self.ct = cipher.encrypt(self.msg)

class Bob:
    def __init__(self):
        self.p = None
        self.b = None
        self.g = None
        self.A = None
        self.B = None
        self.s = None
        self.msg = os.urandom(32)
        self.ct = None
        self.iv = os.urandom(16)

    def recieve_parameters(self, Alice):
        self.p = Alice.p
        self.g = Alice.g
        self.A = Alice.A

    def compute_pubkey(self):
        self.b = random.randint(1, self.p)
        self.B = pow(self.g, self.b, self.p)
     
    def send_B(self, Alice):
        Alice.B = self.B

    def compute_secret(self):
        self.s = hashlib.sha1(long_to_bytes(pow(self.A, self.b, self.p))).digest()[:16]
    
    def encrypt_msg(self):
        cipher = AES.new(self.s, AES.MODE_CBC, self.iv)
        self.ct = cipher.encrypt(self.msg)

class Mallory:
    def __init__(self):
        self.p = None
        self.g = None
        self.A = None
        self.B = None
        self.s = None
        self.ct_A = None
        self.ct_B = None
        self.msg_A = None
        self.msg_B = None

    def receive_parameters(self, Alice):
        self.p = Alice.p
        self.g = Alice.g

    def send_parameters(self, Bob):
        Bob.p = self.p
        Bob.g = self.g
        Bob.A = self.p

    def compute_payload(self):
        self.A = self.p
        self.B = self.p

    def compute_secret(self):
        self.s = hashlib.sha1(long_to_bytes(0)).digest()[:16]

    def receive_ct(self, Alice, Bob):
        self.ct_A = Alice.ct
        self.iv_A = Alice.iv
        self.ct_B = Bob.ct
        self.iv_B = Bob.iv
    
    def decrypt_ct(self):
        cipher_A = AES.new(self.s, AES.MODE_CBC, self.iv_A)
        self.msg_A = cipher_A.decrypt(self.ct_A)
        
        cipher_B = AES.new(self.s, AES.MODE_CBC, self.iv_B)
        self.msg_B = cipher_B.decrypt(self.ct_B)



# Protocol test
A = Alice()
B = Bob()
A.send_parameters(B)
B.compute_pubkey()
A.receive_pubkey(B)
A.compute_secret()
B.compute_secret()
assert(A.s == B.s)

# MITM
A = Alice()
B = Bob()
M = Mallory()

A.send_parameters(M)
M.send_parameters(B)
B.compute_pubkey()

M.compute_payload()
A.receive_pubkey(M)

A.compute_secret()
B.compute_secret()
M.compute_secret()

A.encrypt_msg()
B.encrypt_msg()

M.receive_ct(A, B)
M.decrypt_ct()

assert( (M.msg_A == A.msg) & (M.msg_B == B.msg))


