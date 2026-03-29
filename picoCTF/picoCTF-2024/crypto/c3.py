#!/usr/bin/env python3

lookup1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
lookup2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"


ct = "DLSeGAGDgBNJDQJDCFSFnRBIDjgHoDFCFtHDgJpiHtGDmMAQFnRBJKkBAsTMrsPSDDnEFCFtIbEDtDCIbFCFtHTJDKerFldbFObFCFtLBFkBAAAPFnRBJGEkerFlcPgKkImHnIlATJDKbTbFOkdNnsgbnJRMFnRBNAFkBAAAbrcbTKAkOgFpOgFpOpkBAAAAAAAiClFGIPFnRBaKliCgClFGtIBAAAAAAAOgGEkImHnIl"

code2 = ""
prev = 0
for c in ct:
    idx = lookup2.index(c)
    cur = (idx + prev) % 40
    code2 += lookup1[cur]
    prev = cur

flag = ""
b = 1
for i in range(len(code2)):
    if i == b * b * b:
        flag += code2[i]
        b += 1

flag = "picoCTF{" + flag + "}"
print(flag)


