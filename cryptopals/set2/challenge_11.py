#!/usr/bin/env python3

from Crypto.Cipher import AES
import os
from random import randint

def xor(s1, s2):
    return bytes([a ^ b for a, b in zip(s1, s2)])

def pkcs7_pad(pt, block_size):
    pad_len = block_size - (len(pt) % block_size)
    return pt + bytes([pad_len]*pad_len)

def aes_cbc_encrypt(key, iv, pt):
    cipher = AES.new(key, AES.MODE_ECB)
    ct = b""
    ct_prev = iv
    for i in range(len(pt) // 16):
        ct_curr = cipher.encrypt(xor(pt[i*16:(i+1)*16], ct_prev))
        ct += ct_curr
        ct_prev = ct_curr
    return ct

def encryption_oracle(pt):
    key = os.urandom(16)
    pt = os.urandom(randint(5, 10)) + pt + os.urandom(randint(5,10))
    pt = pkcs7_pad(pt, 16)    
    if randint(0,1):
        cipher = AES.new(key, AES.MODE_ECB)
        ct = cipher.encrypt(pt)
        mode = "ECB"
    else:
        iv = os.urandom(16)
        ct = aes_cbc_encrypt(key, iv, pt)
        mode = "CBC"

    return ct, mode

def detect_aes_mode(ct):
    blocks = [ct[i*16:(i+1)*16] for i in range(len(ct)//16)]
    if len(set(blocks)) == len(blocks):
        return 'CBC'
    return 'ECB'

for _ in range(100):
    pt = b"A"*48
    ct, mode = encryption_oracle(pt)
    assert(mode == detect_aes_mode(ct))


