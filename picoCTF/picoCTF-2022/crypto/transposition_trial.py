#!/usr/bin/env python3

ct = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V091B0AE}2"

pt = ""
for i in range(0,len(ct),3):
    pt += ct[i+2] + ct[i] + ct[i+1]

print(pt)
