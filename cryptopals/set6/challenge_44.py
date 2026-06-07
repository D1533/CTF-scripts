#!/usr/bin/env python3

from enum import verify
from hashlib import sha1
from Crypto.Util.number import getPrime, long_to_bytes
from random import randint
import os

p = int('800000000000000089e1855218a0e7dac38136ffafa72eda7'
                    '859f2171e25e65eac698c1702578b07dc2a1076da241c76c6'
                    '2d374d8389ea5aeffd3226a0530cc565f3bf6b50929139ebe'
                    'ac04f48c3c84afb796d61e5a4f9a8fda812ab59494232c7d2'
                    'b4deb50aa18ee9e132bfa85ac4374d7f9091abc3d015efc87'
                    '1a584471bb1', 16)

q = int('f4f47f05794b256174bba6e9b396a7707e563c5b', 16)
g = int('5958c9d3898b224b12672c0b98e06c60df923cb8bc999d119'
            '458fef538b8fa4046c8db53039db620c094c9fa077ef389b5'
            '322a559946a71903f990f1f7e0e025e2d7f7cf494aff1a047'
            '0f5b64c36b625a097f1651fe775323556fe00b3608c887892'
            '878480e99041be601a62166ca6894bdd41a7054ec89f756ba'
            '9fc95302291', 16)
        

data = []
current = {}
with open("44.txt", "r") as f: # https://cryptopals.com/static/challenge-data/44.txt
    for line in f:
        line = line.strip()
        if not line:
            continue

        if line.startswith("msg:"):
            if current:
                data.append(current)
                current = {}
            current["msg"] = line.split("msg:", 1)[1].strip()

        elif line.startswith("s:"):
            current["s"] = int(line.split("s:", 1)[1].strip())

        elif line.startswith("r:"):
            current["r"] = int(line.split("r:", 1)[1].strip())

        elif line.startswith("m:"):
            current["m"] = line.split("m:", 1)[1].strip()
if current:
    data.append(current)

found = False
for i in range(len(data) - 1):
    for j in range(i+1, len(data)):
        if data[i]["r"] == data[j]["r"]:
            h1 = int(data[i]["m"], 16)
            h2 = int(data[j]["m"], 16)
            s1 = data[i]["s"]
            s2 = data[j]["s"]
            k = ((h1 - h2)*pow(s1 - s2, -1 , q)) % q
            x = ((s1*k - h1)*pow(data[i]["r"], -1, q)) % q
            print("private key x:", x)
            assert(sha1(hex(x)[2:].encode()).hexdigest() == "ca8f6f7c66fa362d40760d135b763eb8527d3d52")
            found = True
            break
    if found:
        break


