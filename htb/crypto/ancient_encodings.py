#!/usr/bin/env python3

from Crypto.Util.number import long_to_bytes
import base64

ct = 0x53465243657a51784d56383361444e664d32356a4d475178626a6c664e44497a5832677a4d6a4e664e7a42664e5463306558303d

flag = base64.b64decode(long_to_bytes(ct).decode()).decode()

print(flag)


