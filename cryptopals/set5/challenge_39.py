#!/usr/bin/env python3


from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
import os



p = getPrime(1024)
q = getPrime(1024)
N = p*q
e = 3

d = pow(e, -1 , (p-1)*(q-1))

m = os.urandom(32)
c = pow(bytes_to_long(m), e, N)

assert( long_to_bytes(pow(c, d, N)) == m)



