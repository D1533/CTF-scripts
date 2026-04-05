#!/usr/bin/env python3

from math import log, sqrt

def xor(s1, s2):
    return bytes([a ^ b for a, b in zip(s1, s2)])

def bhattacharyya_distance(p, q):
     d = sum(sqrt(p[x]*q[x]) for x in p.keys())
     return float('inf') if d == 0 else -log(d)

def get_frequencies(m):
    freq = {}
    n = len(m)
    m = m.lower()
    for k in freq_eng.keys():
        freq[k] = m.count(k.encode()) / n
    return freq

freq_eng = {
    'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253,
    'e': 0.12702, 'f': 0.02228, 'g': 0.02015, 'h': 0.06094,
    'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025,
    'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 'p': 0.01929,
    'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056,
    'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150,
    'y': 0.01974, 'z': 0.00074, ' ': 0.13
}

c = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
n = len(c)

min_dist = float('inf')
for b in range(256):
    m = xor(c, bytes([b]*n))
    freq_m = get_frequencies(m)
    dist = bhattacharyya_distance(freq_m, freq_eng)
    if dist < min_dist:
        min_dist = dist
        pt = m
print(pt.decode())

