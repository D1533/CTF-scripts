#!/usr/bin/env python3

import string
from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64

ALPHABET = string.ascii_letters + string.digits + '~!@#$%^&*'

password = "t*!zGnf#LKO~drVQc@n%oFFZyvhvGZq8zbfXKvE1#*R%uh*$M6c$zrxWedrAENFJB7xz0ps4zh94EwZOnVT9&h"
flag_enc = base64.b64decode("GKLlVVw9uz/QzqKiBPAvdLA+QyRqyctsPJ/tx8Ac2hIUl8/kJaEvHthHUuwFDRCs")

MASTER_KEY = 0

for i,c in enumerate(password):
    if ALPHABET.index(c) < len(ALPHABET)//2:
        MASTER_KEY |= (1 << i)


key_bytes = MASTER_KEY.to_bytes( (MASTER_KEY.bit_length() + 7) // 8, "little")
k = sha256(key_bytes).digest()

cipher = AES.new(k, AES.MODE_ECB)
flag = unpad(cipher.decrypt(flag_enc),16).decode()

print(flag)

