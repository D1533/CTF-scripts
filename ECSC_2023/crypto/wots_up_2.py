#!/usr/bin/env python3

import json
from hashlib import sha256
from Crypto.Cipher import AES

def exploit(pub_key, msg, sig, iv, enc_flag):
    message = f"{pub_key[0]} sent 999999 WOTScoins to me".encode()
    message_hsh = sha256(message).digest()
    
    signature = []
    for i in range(32):
        for m, s in zip(msg, sig):
            h = sha256(m.encode()).digest()
            if h[i] >= message_hsh[i]:
                sig_item = bytes.fromhex(s[i])
                for _ in range(h[i] - message_hsh[i]):
                    sig_item = sha256(sig_item).digest()
                signature.append(sig_item)
                break
    
    key = bytes([s[0] for s in signature])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    flag = cipher.decrypt(enc_flag).decode()
    print(flag)


def main():
    with open("data.json") as f:
        data = json.loads(f.read())
    msg = [] 
    sig = []
    for j in data["signatures"]:
        msg.append(j["message"])
        sig.append(j["signature"])
    
    pub_key = data["public_key"]
    iv = bytes.fromhex(data["iv"])
    enc_flag = bytes.fromhex(data["enc"])

    exploit(pub_key, msg, sig, iv, enc_flag)


if __name__ == "__main__":
    main()
