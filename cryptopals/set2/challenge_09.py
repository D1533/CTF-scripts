#!/usr/bin/env python3

def pkcs7_pad(pt, block_size):
    pad_len = block_size - (len(pt) % block_size)
    return pt + bytes([pad_len]*pad_len)

pt = b"YELLOW SUBMARINE"

print(pkcs7_pad(pt, 20))
