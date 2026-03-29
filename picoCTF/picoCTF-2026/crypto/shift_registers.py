#!/usr/bin/env python3

def steplfsr(lfsr):
    b7 = (lfsr >> 7) & 1
    b5 = (lfsr >> 5) & 1
    b4 = (lfsr >> 4) & 1
    b3 = (lfsr >> 3) & 1

    feedback = b7 ^ b5 ^ b4 ^ b3
    lfsr = (feedback << 7) | (lfsr >> 1)
    return lfsr

ct = bytes.fromhex("21c1b705764e4bfdafd01e0bfdbc38d5eadf92991cdd347064e37444e517d661cea9")

k = next(b for b in range(256) if (ord('p') ^ steplfsr(b)) == ct[0])

pt = bytearray()
for c in ct:
    k = steplfsr(k)
    pt.append(c ^ k)

flag = pt.decode()
print(flag)
