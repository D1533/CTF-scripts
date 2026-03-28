#!/usr/bin/env python3

from sage.all import *
from math import gcd
from Crypto.Util.number import long_to_bytes

n = 0x98a3425eee4016a2592706867127e6c52ab2cf8077806f5626095e3afadc73cb4d0e747c5b9bf6234242e9578b12aba5e391e04a5cd2730f6e45d9f0758fb69eb32e0070b9efd3470f6571a8443bae63cd16efcb3e945dc3da1ce46993be4c8b4467ffb4e0525428bb8673ba144b0d36d1c34fe87307d68439070da27a8809551aa6cdf55c39c79bb7b6b7b9c26b45ef79f6c1ebf68033e4beab2d24df66f69dfb7f54d70d3b477fc7b67592cb029dfe6341c591c34a127f84b33626cd117707b69d1ed55f1773e3ba8d26b76f2db95e85de14a6aa1ff3de7fa23ce9f7ebd0e6c18c2fef4bbff47b6bd632d2d767aab7d35bf4d8577e50556626096704f0c425
c = 0x8788542cefd7490c9282c06b8d24280d56c6706b996bdf580290cdf2cb90e45efd2ce185fc07d2b916c24b0512d38ca14de0ee608a9d6003f258859bbbed97dad15c1d07410a34fd55cd8305eb43418d38f1ca6e024725b97fd9da701a39c23fe55a13d43b4bf9a3d9ebb44d7fe67bd60beffc29ec27bb4baf05ec5b250bfa68360df0d1379c066297a7878e59d27e68cf6a0da90755450827623e54e4f3d9f280fef53c7620d58decfbd10dd64e9d1d5507b5460603c58f5be70c82e2a8e613d730a950caea4c4389c5fc0521f8207ead5fb26c04eb6d0486fd6fe8d015fdabbda00139b42163acc86ffb30c12988058c6247344c42b8f3cdc984c06f4276f8


def pollard_factor(n):
    a = 2
    j = 2
    while True: 
        a = pow(a,j,n)
        g = gcd(a-1,n)
        if 1 < g and g < n:
            return g
        j += 1

def pohlig_hellman(g, h, p, factors):
    remainders = []
    moduli = []
    
    for q, e in factors:
        g_q = pow(g,(p-1)//q**e, p)
        h_q = pow(h, (p-1)//q**e, p)

        x_q = discrete_log(h_q, g_q, ord=q**e)

        remainders.append(x_q)
        moduli.append(q**e)

    x = crt(remainders, moduli)
    return x


p = pollard_factor(n)
q = n//p

x_p = pohlig_hellman(3,c,p,list(factor(p-1))[1:])
x_q = pohlig_hellman(3,c,q,list(factor(q-1)))

x = crt([x_p,x_q],[(p-1)//2,q-1])

x -= (p-1)*(q-1)//4
flag = long_to_bytes(x).decode()
print(flag)
