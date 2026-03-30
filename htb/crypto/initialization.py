#!/usr/bin/env python3

from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Util.Padding import unpad

msg = [
    b'This is some public information that can be read out loud.',
    b'No one can crack our encryption algorithm.',
    b'HTB{?????????????????????????????????????????????}',
    b'Secret information is encrypted with Advanced Encryption Standards.',
]

ct0 = bytes.fromhex("2ac199d1395745812e3e5d3c4dc995cd2f2a076426b70fd5209cdd5ddc0a0c372feb3909956a791702180f591a63af184c27a6ba2fd61c1741ea0818142d0b92")
ct1 = bytes.fromhex("30c6d0cd775b16c23c3f103a1fd883c4632c11366fbc07d92088cc5ddc0a0c373aef3f12c7606c114f546c7f6e00c87a")
ct2 = bytes.fromhex("36fdb2d97d0a5bcf0225586a1e8abfc62d3057273aab5ae5309d8c4ade060a236aed070d817b2c14110e590b1b27ef5d4d35ddc001b47d6c2bca00101c25039a")
ct3 = bytes.fromhex("2dcc93d07c4a16c833375f2b00d894c62c2d442d3cf90cd43183c559c10006372cea2c1595487c0f4314091c0c268b120f3aaabe7bd31c0c05977a7f7c4f6ce6f59392e0e522e66500e153f7a6f914c7")



encrypted_nonces = []

for i in range(len(ct3) // 16):
    encrypted_nonces.append(bytes_to_long(ct3[16*i:16*(i+1)]) ^ bytes_to_long(msg[3][16*i:16*(i+1)]))

flag = b""
for i in range(len(ct2) // 16):
    flag += long_to_bytes(encrypted_nonces[i] ^ bytes_to_long(ct2[16*i:16*(i+1)]))

print(unpad(flag,16).decode())

