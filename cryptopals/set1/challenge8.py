#!/usr/bin/env python3

def ecb_score(ct):
    blocks = []
    for i in range(len(ct)//16):
        blocks.append(ct[i*16:(i+1)*16])

    return len(set(blocks)) / len(blocks)

with open('8.txt', 'r') as f: # https://cryptopals.com/static/challenge-data/8.txt
    lines = f.readlines()
    ct = list(map(bytes.fromhex, lines))

min_score = float('inf')
best_cipher = 0
for i in range(len(ct)):
    score = ecb_score(ct[i])
    if score < min_score:
        min_score = score
        ciphertext = ct[i]
        ciphertext_idx = i

print(ciphertext_idx, ciphertext.hex())



