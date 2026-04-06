#!/usr/bin/env python3

import os
from Crypto.Cipher import AES

def xor(s1, s2):
    return bytes([a ^ b for a, b in zip(s1, s2)])

def pkcs7_pad(pt, block_size):
    pad_len = block_size - (len(pt) % block_size)
    return pt + bytes([pad_len]*pad_len)

class Oracle():
    def __init__(self):
        self.key = os.urandom(16)

    def parse_kv(self, s):
        return dict(pair.split("=") for pair in s.split("&"))

    def profile_for(self, email):
        email = email.replace("&", "").replace("=", "")
        return f"email={email}&uid=10&role=user".encode()

    def encrypt(self, pt):
        pt = self.profile_for(pt)
        cipher = AES.new(self.key, AES.MODE_ECB)
        ct = cipher.encrypt(pkcs7_pad(pt, 16))
        return ct
    
    def decrypt(self, ct):
        cipher = AES.new(self.key, AES.MODE_ECB)
        pt = cipher.decrypt(ct)
        return pt

def cut_and_paste_attack(oracle):
    pad_len = 16 - len("admin")
    payload1 = "A"*(16 - len("email=")) + "admin" + chr(pad_len)*pad_len
    ct1 = oracle.encrypt(payload1)
    payload2 = "A"*(16 - len("email=&uid=10&role=") % 16)
    ct2 = oracle.encrypt(payload2)

    ct = ct2[:32] + ct1[16:32]
    return ct

def main():
    oracle = Oracle()
    ct = cut_and_paste_attack(oracle)
    assert(b"role=admin" in oracle.decrypt(ct))

if __name__ == "__main__":
    main()
