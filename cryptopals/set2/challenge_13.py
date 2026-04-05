#!/usr/bin/env python3

import os
from Crypto.Cipher import AES

def xor(s1, s2):
    return bytes([a ^ b for a, b in zip(s1, s2)])

def pkcs7_pad(pt, block_size):
    pad_len = block_size - (len(pt) % block_size)
    return pt + bytes([pad_len]*pad_len)

def parse_kv(s):
    return dict(pair.split("=") for pair in s.split("&"))

def profile_for(email):
    email = email.replace("&", "").replace("=", "")
    return f"email={email}&uid=10&role=user".encode()

key = os.urandom(16)
def encryption_oracle(pt):
    pt = profile_for(pt)
    cipher = AES.new(key, AES.MODE_ECB)
    ct = cipher.encrypt(pkcs7_pad(pt, 16))

    return ct

def cut_and_paste_attack():
    pad_len = 16 - len("admin")
    payload1 = "A"*(16 - len("email=")) + "admin" + chr(pad_len)*pad_len
    ct1 = encryption_oracle(payload1)
    payload2 = "A"*(16 - len("email=&uid=10&role=") % 16)
    ct2 = encryption_oracle(payload2)

    ct = ct2[:32] + ct1[16:32]
    return ct

ct = cut_and_paste_attack()
cipher = AES.new(key, AES.MODE_ECB)
pt = cipher.decrypt(ct)
assert(b"role=admin" in pt)

