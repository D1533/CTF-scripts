#!/usr/bin/env python3

from sage.all import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from hashlib import sha1

def pohlig_hellman(G, Q, max_prod):
    n = G.order()
    factors = factor(n)

    residues = []
    moduli = []
    prod = 1
    for p, e in factors:
        if prod >= max_prod:
            break
        prod *= int(p**e)
        
        G_pe = (n // p**e)*G
        Q_pe = (n // p**e)*Q
        d = G_pe.discrete_log(Q_pe)
        
        residues.append(d)
        moduli.append(p**e)
    
    dlog = crt(residues, moduli)
    return dlog


p = 101177610013690114367644862496650410682060315507552683976670417670408764432851 
Gx, Gy = [14374457579818477622328740718059855487576640954098578940171165283141210916477, 97329024367170116249091206808639646539802948165666798870051500045258465236698]
Gn = 32293793010624418281951109498609822259728115103695057808533313831446479788050
ct = bytes.fromhex("df572f57ac514eeee9075bc0ff4d946a80cb16a6e8cd3e1bb686fabe543698dd8f62184060aecff758b29d92ed0e5a315579b47f6963260d5d52b7ba00ac47fd")
IV = bytes.fromhex("baf9137b5bb8fa896ca84ce1a98b34e5")

# Lambda parameters
k1 = 417826948860567519876089769167830531934
k2 = 177776968102066079765540960971192211603
k3 = 3045783791

# dy/dx = (3x**2 + k1x + k2)/(2y + k3) => y**2 + k3y + c1 = x**3 + k1/2x**2 + k2*x + c2
a1 = 0
a2 = (k1 * pow(2, -1, p)) % p
a3 = k3
a4 = k2
a5 = (Gy**2 + a3*Gy - Gx**3 - a2*Gx**2 - a4*Gx ) % p

E = EllipticCurve(GF(p), [a1,a2,a3,a4,a5])
G = E(Gx, Gy)
Q = E.lift_x(Integer(Gn))

factors = factor(G.order())
prod = prod([p**e for p, e in factors[:-2]]) # the last two factors are too large for discrete log
n = pohlig_hellman(G, Q, prod )

while True:
    if n*G == Q:
        break
    n += prod

key = sha1(str(n).encode('ascii')).digest()[0:16]
cipher = AES.new(key, AES.MODE_CBC, IV)
flag = unpad(cipher.decrypt(ct),16).decode()
print(flag)

