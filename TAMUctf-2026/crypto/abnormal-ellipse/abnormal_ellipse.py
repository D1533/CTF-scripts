#!/usr/bin/env python3

from sage.all import *
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import hashlib

def Hensel_lift(E, P, F):
    x, y = map(ZZ, P.xy())
    for p in E.lift_x(x, all=True):
        xx, yy = map(F, p.xy())
        if y == yy:
            return p


def Smart_Attack(E, G, P):
    F_p = GF(p)
    Eqq = E.change_ring(QQ)
    Eqp = Eqq.change_ring(Qp(p))
    G = p*Hensel_lift(Eqp, G, F_p)
    P = p*Hensel_lift(Eqp, P, F_p)
    G_x, G_y = G.xy()
    P_x, P_y = P.xy()

    return int(F_p( (P_x / P_y) / (G_x / G_y)))


p = 57896044618658103051097247842201434560310253892815534401457040244646854264811
a = 57896044618658103051097247842201434560310253892815534336455328262589759096811
b = 6378745995050415640528904257536000
E = EllipticCurve(GF(p), [a, b])

G = E(46876917648549268272641716936114495226812126512396931121066067980475334056759, 29018161638760518123770904309639572979634020954930188106398864033161780615057)
PA = E(41794565872898552028378254333448511042514164360566217446125286680794907163222, 28501067479064047326107608780246105661757692260405498327414296914217192089882)
PB = E(832923623940209904267388169663314834051489004894067103155141367420578675552, 7382962163953851721569729505742450736497607615866914193411926051803583826592)

ct = bytes.fromhex("e31e0e638110d1e5c39764af90ac6194c1f9eaabd396703371dc2e6bb2932a18d824d86175ab071943cba7c093ccc6c6")
iv = bytes.fromhex("478876e42be078dceb3aee3a6a8f260f")


assert(p == E.order())
dB = Smart_Attack(E, G, PB)

S = dB * PA
S_x, S_y = S.xy()

key = hashlib.sha256(int(S_x).to_bytes((int(S_x).bit_length() + 7) // 8, 'big')).digest()


cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
decryptor = cipher.decryptor()

padded_plaintext = decryptor.update(ct) + decryptor.finalize()
unpadder = padding.PKCS7(128).unpadder()
flag = unpadder.update(padded_plaintext) + unpadder.finalize()

print(flag.decode())


