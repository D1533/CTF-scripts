#!/usr/bin/env python3

from Crypto.PublicKey import RSA
from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64
from sage.all import *

def polynomial_gcd(g1, g2):
    while g2:
        g1, g2 = g2, g1 % g2
    return g1.monic()

with open("key1.pem", "rb") as f:
    key1 = RSA.import_key(f.read())

with open("key2.pem", "rb") as f:
    key2 = RSA.import_key(f.read())

message1 = b"RBVdQw7Pllwb42GDYyRa6ByVOfzRrZHmxBkUPD393zxOcrNRZgfub1mqcrAgX4PAsvAOWptJSHbrHctFm6rJLzhBi/rAsKGboWqPAWYIu49Rt7Sc/5+LE2dvy5zriAKclchv9d+uUJ4/kU/vcpg2qlfTnyor6naBsZQvRze0VCMkPvqWPuE6iL6YEAjZmLWmb+bqO+unTLF4YtM1MkKTtiOEy+Bbd4LxlXIO1KSFVOoGjyLW2pVIgKzotB1/9BwJMKJV14/+MUEiP40ehH0U2zr8BeueeXp6NIZwS/9svmvmVi06Np74EbL+aeB4meaXH22fJU0eyL2FppeyvbVaYQ=="
message2 = b"TSHSOfFBkK/sSE4vWxy00EAnZXrIsBI/Y6mGv466baOsST+qyYXHdPsI33Kr6ovucDjgDw/VvQtsAuGhthLbLVdldt9OWDhK5lbM6e0CuhKSoJntnvCz7GtZvjgPM7JDHQkAU7Pcyall9UEqL+W6ZCkiSQnK+j6QB7ynwCsW1wAmnCM68fY2HaBvd8RP2+rPgWv9grcEBkXf7ewA+sxSw7hahMaW0LYhsMYUggrcKqhofGgl+4UR5pdSiFg4YKUSgdSw1Ic/tug9vfHuLSiiuhrtP38yVzazqOZPXGxG4tQ6btc1helH0cLfw1SCdua1ejyan9l1GLXsAyGOKSFdKw=="

c1 = bytes_to_long(base64.b64decode(message1))
c2 = bytes_to_long(base64.b64decode(message2))

n = key1.n
e1 = key1.e
e2 = key2.e

R = PolynomialRing(Zmod(n), 'x')
x = R.gen()

f = x**e1 - c1
g = x**e2 - c2

m = int(-polynomial_gcd(f, g)[0] % n)
flag = long_to_bytes(m).decode()
print(flag)












