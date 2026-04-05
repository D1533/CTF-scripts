#!/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

with open("7.txt", "r") as f: # https://cryptopals.com/static/challenge-data/7.txt
    data = f.read()

ct = base64.b64decode(data.encode())

key = b"YELLOW SUBMARINE"
cipher = AES.new(key, AES.MODE_ECB)
pt = unpad(cipher.decrypt(ct), 16)

print(pt.decode())
