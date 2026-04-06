#!/usr/bin/env python3

from Crypto.Cipher import AES
import os
import base64

def xor(s1, s2):
    return bytes([a ^ b for a, b in zip(s1, s2)])

def pkcs7_pad(pt, block_size):
    pad_len = block_size - (len(pt) % block_size)
    return pt + bytes([pad_len]*pad_len)


class Oracle():
    def __init__(self):
        self.key = os.urandom(16)

    def encrypt(self, pt):
        secret = base64.b64decode("""Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
                                     aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
                                     dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
                                     YnkK""")
        pt += secret
        pt = pkcs7_pad(pt, 16)    
        
        cipher = AES.new(self.key, AES.MODE_ECB)
        ct = cipher.encrypt(pt)

        return ct

def detect_aes_mode(ct):
    blocks = [ct[i:i+16] for i in range(0, len(ct), 16)]
    if len(set(blocks)) == len(blocks):
        return 'CBC'
    return 'ECB'

def ecb_byte_at_a_time(oracle):
    len_0 = len(oracle.encrypt(b""))
    for i in range(16):
        len_i = len(oracle.encrypt(b"A" * (i+1)))
        if len_i > len_0:
            secret_len = len_0 - (i+1)
            break

    secret = b""
    for i in range(secret_len):  
        block_idx = i // 16

        payload = b"A" * (15 - (i % 16))
        ct = oracle.encrypt(payload)

        for b in range(256):
            pt_b = payload + secret + bytes([b])
            ct_b = oracle.encrypt(pt_b)

            if ct_b[16*(block_idx):16*(block_idx + 1)] == ct[16*(block_idx):16*(block_idx + 1)]:
                secret += bytes([b])
                break
    return secret

def main():
    oracle = Oracle()
    secret = ecb_byte_at_a_time(oracle)
    print(secret.decode())

if __name__ == "__main__":
    main()
