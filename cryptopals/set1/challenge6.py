#!/usr/bin/env python3

import base64
from math import log, sqrt

def xor(s1, s2):
    return bytes([a ^ b for a, b in zip(s1, s2)])

def repeating_key_xor(pt, key):
    return bytes([pt[i] ^ key[i % len(key)] for i in range(len(pt))])

def bhattacharyya_distance(p, q):
    d = sum(sqrt(p[x]*q[x]) for x in p.keys())
    return float('inf') if d == 0 else -log(d)

def hamming_distance(s1, s2):
    return sum( (a ^ b).bit_count() for a, b in zip(s1, s2))

def get_frequencies(m):
    freq = {}
    n = len(m)
    m = m.lower()
    for k in freq_eng.keys():
        freq[k] = m.count(k.encode()) / n
    return freq

def get_key_size(ct, n_blocks, max_size):
    min_dist_k = float('inf')
    for k in range(2, 40):
        blocks = [ct[i*k:(i+1)*k] for i in range(n_blocks)]
        dist = 0
        for i in range(len(blocks)-1):
            for j in range(i, len(blocks)):
                dist += hamming_distance(blocks[i], blocks[j]) / k
        dist /= n_blocks
        if dist < min_dist_k:
            min_dist_k = dist
            key_len = k
    return key_len

def solve_single_byte_xor(block):
    min_dist = float('inf')
    n = len(block)
    key = 0
    for b in range(256):
        pt_i = xor(block, bytes([b]*n))
        freq_pt = get_frequencies(pt_i)
        dist = bhattacharyya_distance(freq_pt, freq_eng)
        if dist < min_dist:
            min_dist = dist
            key = b
    return bytes([key])

freq_eng = {
    'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253,
    'e': 0.12702, 'f': 0.02228, 'g': 0.02015, 'h': 0.06094,
    'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025,
    'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 'p': 0.01929,
    'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056,
    'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150,
    'y': 0.01974, 'z': 0.00074, ' ': 0.13
}

with open("6.txt", "r") as f: # https://cryptopals.com/static/challenge-data/6.txt
    data = f.read()

ct = base64.b64decode(data.encode())
key_len = get_key_size(ct, 4, 40)
key = b""
for i in range(key_len):
    block = bytes([ct[j] for j in range(i, len(ct), key_len)])
    key += solve_single_byte_xor(block)

pt = repeating_key_xor(ct, key)
print(pt.decode())





