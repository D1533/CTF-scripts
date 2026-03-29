#!/usr/bin/env python3


from sage.all import *
import hashlib

VERIF_KEY = "96cc5f3b460732b442814fd33cf8537c"
ENCRYPTED_FLAG = bytes.fromhex("42cbbce1487b443de1acf4834baed794f4bbd0dfb5885e6c7ed9a3c62b")

def decrypt_flag(sol):
    sol = sol % (10**10000)
    sol = str(sol)
    sol_md5 = hashlib.md5(sol.encode()).hexdigest()

    if sol_md5 != VERIF_KEY:
        print("Incorrect solution")
        sys.exit(1)

    key = hashlib.sha256(sol.encode()).digest()
    flag = bytearray([char ^ key[i] for i, char in enumerate(ENCRYPTED_FLAG)]).decode()

    print(flag)

a1 = 21
a2 = 301
a3 = -9549
a4 = 55692

A = Matrix([[a1, a2, a3, a4],
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0]])

f3 = vector([4,3,2,1])
sol = (A**(int(2e7)-3)*f3)[0]

decrypt_flag(sol)
