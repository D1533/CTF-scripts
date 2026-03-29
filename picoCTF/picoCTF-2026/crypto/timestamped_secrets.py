#!/usr/bin/env python3

import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from hashlib import sha256

ct = bytes.fromhex("6d8330b05a68848fdf4b7ab057cd6eb070810e3febd76872b4a5e7627221a396")
timestamp = 1770242633

key = sha256(str(timestamp).encode()).digest()[:16]
cipher = AES.new(key, AES.MODE_ECB)
flag = unpad(cipher.decrypt(ct), 16).decode()

print(flag)

