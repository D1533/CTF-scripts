#!/usr/bin/env python3

from Crypto.Cipher import AES
import os

def xor(s1, s2): 
    return bytes([a ^ b for a, b in zip(s1, s2)])

def pkcs7_pad(pt, block_size):
    pad_len = block_size - (len(pt) % block_size)
    return pt + bytes([pad_len]*pad_len)


class Oracle():
    def __init__(self):
        self.key = os.urandom(16)
        self.iv = os.urandom(16)
        self.prefix = b"comment1=cooking%20MCs;userdata="
        self.sufix = b";comment2=%20like%20a%20pound%20of%20bacon"

    def encrypt(self, pt):
        pt = self.prefix + pt + self.sufix 
        pt = pkcs7_pad(pt, 16)
        cipher = AES.new(self.key, AES.MODE_ECB)
        ct = b""
        ct_prev = self.iv
        for i in range(0, len(pt), 16):
            ct_curr = cipher.encrypt(xor(pt[i:i+16], ct_prev))
            ct += ct_curr
            ct_prev = ct_curr
        return self.iv + ct

    def decrypt(self, ct):
        cipher = AES.new(self.key, AES.MODE_ECB)
        pt = b"" 
        ct_prev = ct[:16]
        ct = ct[16:]
        for i in range(0, len(ct), 16):
            pt += xor(cipher.decrypt(ct[i:i+16]), ct_prev)
            ct_prev = ct[i:i+16]
        print(pt) 
        if b";admin=true;" in pt:
            return True
        return False

def cbc_bit_flipping_attack(oracle, target):
    ct = oracle.encrypt(b"A"*len(target))
    original = b"A" * len(target)
    ct = ct[16:]
    ct = bytearray(ct)
    prefix_len = len(b"comment1=cooking%20MCs;userdata=")
    
    block_index = prefix_len // 16
    for i in range(len(target)):
        ct[(block_index-1)*16 + i] ^= (original[i] ^ target[i])

    return bytes(ct)

def main():
    oracle = Oracle()
    ct = cbc_bit_flipping_attack(oracle, b";admin=true;")
    print(oracle.decrypt(ct))

if __name__ == "__main__":
    main()
