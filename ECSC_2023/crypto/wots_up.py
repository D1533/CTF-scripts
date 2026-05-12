#!/usr/bin/env python3

import json
from hashlib import sha256
from Crypto.Cipher import AES

def exploit(pub_key, message, signature, enc_flag, iv):
    
    message_hash = sha256(message.encode()).digest()
    idx = message_hash.index(0xff)
    
    priv_key = []
    priv = bytes.fromhex(signature[idx])
    for _ in range(32):
        priv_key.append(priv)
        priv = sha256(priv).digest()
    
    message = b"Sign for flag"
    msg_hash = sha256(message).digest()
    
    sig = []
    for i in range(32):
        sig_item = priv_key[i]
        for _ in range(255 - msg_hash[i]):
            sig_item = sha256(sig_item).digest()
        sig.append(sig_item)
    
    key = bytes([s[0] for s in sig])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    flag = cipher.decrypt(enc_flag).decode()

    print(flag)

    
def main():
    with open("data.json") as f:
        data = json.load(f)
    pub_key = data["public_key"]
    message = data["message"]
    signature = data["signature"]
    enc_flag = bytes.fromhex(data["enc"])
    iv = bytes.fromhex(data["iv"])

    exploit(pub_key, message, signature, enc_flag, iv)

if __name__ == "__main__":
    main()
