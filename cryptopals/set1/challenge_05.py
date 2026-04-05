#!/usr/bin/env python3

def repeating_key_xor(pt, key):
    return bytes([pt[i] ^ key[i % len(key)] for i in range(len(pt))])

pt = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

ct = repeating_key_xor(pt, b"ICE")

print(ct.hex())
