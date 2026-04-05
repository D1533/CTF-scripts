#!/usr/bin/env python3

from Crypto.Cipher import AES
import os

def xor(s1, s2): 
    return bytes([a ^ b for a, b in zip(s1, s2)])

def pkcs7_pad(pt, block_size):
    pad_len = block_size - (len(pt) % block_size)
    return pt + bytes([pad_len]*pad_len)

key = os.urandom(16)
iv = os.urandom(16)
def aes_cbc_encrypt_oracle(pt):
    pt = b"comment1=cooking%20MCs;userdata=" + pt + b";comment2=%20like%20a%20pound%20of%20bacon"
    pt = pkcs7_pad(pt, 16)
    cipher = AES.new(key, AES.MODE_ECB)
    ct = b""
    ct_prev = iv
    for i in range(len(pt) // 16):
        ct_curr = cipher.encrypt(xor(pt[i*16:(i+1)*16], ct_prev))
        ct += ct_curr
        ct_prev = ct_curr
    return ct

def aes_cbc_decrypt_oracle(ct):
    cipher = AES.new(key, AES.MODE_ECB)
    pt = b"" 
    ct_prev = iv
    for i in range(len(ct) // 16):
        pt += xor(cipher.decrypt(ct[i*16:(i+1)*16]), ct_prev)
        ct_prev = ct[i*16:(i+1)*16]
    
    if b";admin=true;" in pt:
        return True
    return False

def cbc_bit_flipping_attack():
    payload = b"A" * 16
    ct = aes_cbc_encrypt_oracle(payload)

    target = b";admin=true;"
    original = b"A" * len(target)

    ct = bytearray(ct)
    prefix_len = len(b"comment1=cooking%20MCs;userdata=")

    block_index = prefix_len // 16

    for i in range(len(target)):
        ct[(block_index-1)*16 + i] ^= (original[i] ^ target[i])

    return bytes(ct)

ct = cbc_bit_flipping_attack()
print(aes_cbc_decrypt_oracle(ct))
