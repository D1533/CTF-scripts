#!/usr/bin/env python3

from Crypto.Cipher import AES
import os
import base64
from random import randint

def xor(s1, s2):
    return bytes([a ^ b for a, b in zip(s1, s2)])

def pkcs7_pad(pt, block_size):
    pad_len = block_size - (len(pt) % block_size)
    return pt + bytes([pad_len]*pad_len)


class Oracle():
    def __init__(self):
        self.key = os.urandom(16)
        self.prefix = os.urandom(randint(1,100))
        self.secret = base64.b64decode("""Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
                                          aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
                                          dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
                                          YnkK""")

    def encrypt(self, pt):
        pt = self.prefix + pt + self.secret
        pt = pkcs7_pad(pt, 16)    
        cipher = AES.new(self.key, AES.MODE_ECB)
        ct = cipher.encrypt(pt)

        return ct

def get_prefix_size(oracle):
    for pad_len in range(32):
        pt = b"A"*pad_len + b"B"*32
        ct = oracle.encrypt(pt)

        blocks = [ct[i:i+16] for i in range(0, len(ct), 16)]

        for i in range(len(blocks) - 1):
            if blocks[i] == blocks[i+1]:
                return i*16 - pad_len

def ecb_byte_at_a_time(oracle):
    prefix_size = get_prefix_size(oracle)
    pad_len = (16 - (prefix_size % 16)) % 16

    len_0 = len(oracle.encrypt(b""))
    for i in range(16):
        if len(oracle.encrypt(b"A"*(i+1))) > len_0:
            secret_len = len_0 - (i+1) - prefix_size
            break

    secret = b""
    for i in range(secret_len):
        padding = b"A" * (pad_len + (16 - 1 - (i % 16)))
        ct = oracle.encrypt(padding)

        block_idx = (prefix_size + pad_len + i) // 16
        for b in range(256):
            pt_b = padding + secret + bytes([b])
            ct_b = oracle.encrypt(pt_b)
            if ct_b[block_idx*16:(block_idx+1)*16] == ct[block_idx*16:(block_idx+1)*16]:
                secret += bytes([b])
                break

    return secret

def main():
    oracle = Oracle()
    secret = ecb_byte_at_a_time(oracle)
    print(secret.decode())


if __name__ == "__main__":
    main()
