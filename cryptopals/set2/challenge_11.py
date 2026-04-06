#!/usr/bin/env python3

from Crypto.Cipher import AES
import os
from random import randint

def xor(s1, s2):
    return bytes([a ^ b for a, b in zip(s1, s2)])

def pkcs7_pad(pt, block_size):
    pad_len = block_size - (len(pt) % block_size)
    return pt + bytes([pad_len]*pad_len)

class Oracle:
    def __init__(self):
        self.key = os.urandom(16)
        self.iv = os.urandom(16)
    
    def ecb_encrypt(self, pt):
        self.key = os.urandom(16)
        cipher = AES.new(self.key, AES.MODE_ECB)
        ct = cipher.encrypt(pt)
        return ct

    def cbc_encrypt(self, pt):
        self.key = os.urandom(16)
        self.iv = os.urandom(16)
        cipher = AES.new(self.key, AES.MODE_ECB)
        ct = b""
        ct_prev = self.iv
        for i in range(0, len(pt), 16):
            ct_curr = cipher.encrypt(xor(pt[i:i+16], ct_prev))
            ct += ct_curr
            ct_prev = ct_curr
        return ct

    def encrypt(self, pt):
        pt = os.urandom(randint(5, 10)) + pt + os.urandom(randint(5,10))
        pt = pkcs7_pad(pt, 16)    
        if randint(0,1):
            ct = self.ecb_encrypt(pt)
            mode = "ECB"
        else:
            ct = self.cbc_encrypt(pt)
            mode = "CBC"

        return ct, mode

def detect_aes_mode(ct):
    blocks = [ct[i:i+16] for i in range(0, len(ct), 16)]
    if len(set(blocks)) == len(blocks):
        return 'CBC'
    return 'ECB'

def main():
    oracle = Oracle()
    for _ in range(100):
        pt = b"A"*64
        ct, mode = oracle.encrypt(pt)
        assert(mode == detect_aes_mode(ct))

if __name__ == "__main__":
    main()
