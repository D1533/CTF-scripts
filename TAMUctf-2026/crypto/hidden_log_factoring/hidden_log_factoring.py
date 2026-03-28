#!/usr/bin/env python3

from sage.all import *
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from Crypto.Util.number import long_to_bytes, bytes_to_long
import random

n = 71016310005824589926747341243598522145452505235842335510488353587223142066921470760443852767377534776713566052988373656012584808377496091765373981120165220471527586994259252074709653090148780742972203779666231432769553199154214563039426087870098774883375566546770723222752131892953195949848583409407713489831
e = 65537

p = 200167626629249973590210748210664315551571227173732968065685194568612605520816305417784745648399324178485097581867501503778073506528170960879344249321872139638179291829086442429009723480288604047975360660822750743411854623254328369265079475034447044479229192540942687284442586906047953374527204596869578972378578818243592790149118451253249
g = 11
A = 44209577951808382329528773174800640982676772266062718570752782238450958062000992024007390942331777802579750741643234627722057238001117859851305258592175283446986950906322475842276682130684406699583969531658154117541036033175624316123630171940523312498410797292015306505441358652764718889371372744612329404629522344917215516711582956706994

D = 9478993126102369804166465392238441359765254122557022102787395039760473484373917895152043164556897759129379257347258713397227019255397523784552330568551257950882564054224108445256766524125007082113207841784651721510041313068567959041923601780557243220011462176445589034556139643023098611601440872439110251624
c = 1479919887254219636530919475050983663848182436330538045427636138917562865693442211774911655964940989306960131568709021476461747472930022641984797332621318327273825157712858569934666380955735263664889604798016194035704361047493027641699022507373990773216443687431071760958198437503246519811635672063448591496


def hkdf_mask(secret: bytes, length: int) -> bytes:
  hkdf = HKDF(
    algorithm=hashes.SHA256(),
    length=length,
    salt=None,
    info=b"rsa-d-mask",
    backend=default_backend()
  )
  return hkdf.derive(secret)

def pohlig_hellman(h, g, p, max_bit_size):
    factors = factor(p-1)

    residues = []
    moduli = []
    prod = 1
    for p_i, e_i in factors:
        if int(prod).bit_length() > max_bit_size:
            break
        
        prod *= p_i**e_i
        g_i = pow(g, (p-1)//(p_i**e_i), p)
        h_i = pow(A, (p-1)//(p_i**e_i), p)
        x_i = discrete_log(h_i, g_i)
        residues.append(x_i)
        moduli.append(p_i**e_i)

    x = crt(residues, moduli)
    
    return x


def RSA_factor_with_private_key(N, e, d):
    t = e*d - 1
    s = 0
    while t % 2 == 0:
        t //= 2
        s += 1

    a = 2
    while True:
        b = pow(a, t, N)

        if b == 1:
            a = next_prime(a)
            continue

        i = s
        while i != 0:
            c = pow(b, 2, N)

            if c != 1:
                b = c
                i -= 1
                continue
            else:
                break

        if b == N - 1:
            a = next_prime(a)
            continue

        p = gcd(b - 1, N)
        if p != 1 and p != N:
            q = N // p
            return p, q

        a = next_prime(a)



F = GF(p)
A = F(A)
g = F(g)

s = pohlig_hellman(A, g, p, 100)
assert(pow(g,s,p) == A)
print("s:", s)


d = D ^ bytes_to_long(hkdf_mask(long_to_bytes(int(s)), n.bit_length() // 8))
assert all(pow(r, e*d, n) == r for r in (random.randint(2, n-1) for _ in range(100)))
print("d:", d)    

q1, q2 = RSA_factor_with_private_key(n, e, d)

M1 = Zmod(q1)(c).sqrt(all=True)
M2 = Zmod(q2)(c).sqrt(all=True)

for m1 in M1:
    for m2 in M2:
        m = crt([int(m1), int(m2)], [q1, q2])
        try:
            flag = long_to_bytes(m).decode()
            print(flag)
        except:
            pass

