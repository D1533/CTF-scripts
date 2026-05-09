#!/usr/bin/env python3


from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes
from gmpy2 import iroot

def exploit(pubkey, enc_key, ct):
    n = pubkey.n
    e = pubkey.e
    
    p = iroot(n, 3)[0]
    phi = p**3 - p**2
    d = pow(e, -1, phi)
    aes_key = long_to_bytes(pow(enc_key, d, n))

    cipher = AES.new(aes_key, AES.MODE_ECB)
    flag = cipher.decrypt(ct).decode()
    print(flag)



def main():
    with open("flag.txt.aes", "rb") as f:
        ct = f.read().strip()

    with open("pubkey.pem", "rb") as f:
        pubkey = RSA.importKey(f.read())

    with open("key") as f:
        enc_key = int(f.read(), 16)

    exploit(pubkey, enc_key, ct)

if __name__ == "__main__":
    main()
