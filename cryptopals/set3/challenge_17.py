#!/usr/bin/env python3

from Crypto.Cipher import AES
import os
import base64

def xor(s1, s2): 
    return bytes([a ^ b for a, b in zip(s1, s2)])

def pkcs7_pad(pt, block_size):
    pad_len = block_size - (len(pt) % block_size)
    return pt + bytes([pad_len]*pad_len)

def pkcs7_unpad(pt, block_size):
    if len(pt) % block_size != 0:
        raise ValueError("Input lenght is not multiple of block size")
    pad_len = pt[-1]
    if pad_len < 1 or pad_len > 16:
        raise ValueError("Invalid padding length")

    if pt[-pad_len:] != bytes([pad_len]*pad_len):
        raise ValueError("Invalid PKCS#7 padding")

    return pt[:-pad_len]

class Oracle:
    def __init__(self):
        self.key = os.urandom(16)
        self.iv = os.urandom(16)
        self.plaintexts = ["MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=",
                           "MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=",
                           "MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==",
                           "MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==",
                           "MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl",
                           "MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==",
                           "MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==",
                           "MDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=",
                           "MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=",
                           "MDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93"]
    
    def encrypt(self, pt):
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
        try:
            cipher = AES.new(self.key, AES.MODE_ECB)
            pt = b"" 
            ct_prev = ct[:16]
            ct = ct[16:]
            for i in range(0, len(ct), 16):
                pt += xor(cipher.decrypt(ct[i:i+16]), ct_prev)
                ct_prev = ct[i:i+16]

            pt = pkcs7_unpad(pt, 16)
            return True
        except:
            return False


def aes_cbc_padding_oracle_attack(oracle, ct):
    blocks = [ct[i:i+16] for i in range(0, len(ct), 16)]

    pt = b""
    prev_block = blocks[0]
    for i in range(1, len(blocks)):
        curr_block = blocks[i]
        mask = bytearray(16)

        for byte_idx in range(15, -1, -1):
            pad = 16 - byte_idx
            last_block = bytearray([pad] * 16)

            for k in range(byte_idx + 1, 16):
                last_block[k] ^= mask[k]

            for b in range(256):
                last_block[byte_idx] = b
                ct_b = bytes(last_block) + curr_block

                if oracle.decrypt(ct_b):
                    mask[byte_idx] = b ^ pad
                    break

        plaintext_block = xor(prev_block, mask)

        pt += plaintext_block
        prev_block = curr_block

    return pkcs7_unpad(pt, 16)


def main():
    oracle = Oracle()
    plaintexts = [base64.b64decode(pt) for pt in oracle.plaintexts]
    ciphertexts = [oracle.encrypt(pt) for pt in plaintexts] 
    plaintexts_recovered = []
    for ct in ciphertexts:
        plaintexts_recovered.append(aes_cbc_padding_oracle_attack(oracle, ct))

    assert(plaintexts == plaintexts_recovered)

if __name__ == '__main__':
    main()
