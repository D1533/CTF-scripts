#!/usr/bin/env python3

def pkcs7_unpad(pt, block_size):
    if len(pt) % block_size != 0:
        raise ValueError("Input lenght is not multiple of block size")
    pad_len = pt[-1]
    if pad_len < 1 or pad_len > 16:
        raise ValueError("Invalid padding length")

    if pt[-pad_len:] != bytes([pad_len]*pad_len):
        raise ValueError("Invalid PKCS#7 padding")

    return pt[:-pad_len]


tests = [
    b"ICE ICE BABY\x04\x04\x04\x04",
    b"ICE ICE BABY\x05\x05\x05\x05",
    b"ICE ICE BABY\x01\x02\x03\x04"
]

for test in tests:
    try:
        print(pkcs7_unpad(test, 16))
    except ValueError as e:
        print(f"Error: {e}")
