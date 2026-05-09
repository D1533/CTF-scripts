#!/usr/bin/env python3

from sage.all import *
from pwn import *
from hashlib import md5
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def fermat_factor(n):
    a = isqrt(n)
    if a * a < n:
        a += 1
    while True:
        b2 = a*a - n
        b = isqrt(b2)

        if b*b == b2:
            p = a - b
            q = a + b
            return p, q
        a += 1

def next_prime(num):
    if num % 2 == 0:
        num += 1
    else:
        num += 2
    while not is_prime(num):
        num += 2
    return num

def get_parameters(io):
    io.recvuntil(b"flag: ")
    ct = io.recvline().strip().decode()
    io.recvuntil(b"IV: ")
    iv = io.recvline().strip().decode()
    io.recvuntil(b"N: ")
    n = int(io.recvline().strip().decode())
    io.recvuntil(b"x=")
    x = int(io.recvuntil(b",")[:-1].decode())
    io.recvuntil(b"y=")
    y = int(io.recvuntil(b")")[:-1])
    
    io.sendlineafter(b"> ", b"y")
    io.recvuntil(b"x=")
    Gx = int(io.recvuntil(b",")[:-1].decode())
    io.recvuntil(b"y=")
    Gy = int(io.recvuntil(b")")[:-1])
     
    return ct, iv, n, x, y, Gx, Gy

def exploit(io):
    ct, iv, n, Ax, Ay, Gx, Gy = get_parameters(io)
    a = ((Ay**2 - Gy**2-Ax**3+Gx**3)*pow(Ax-Gx, -1, n) ) % n
    b = (Ay**2 - Ax**3 - a*Ax) % n
    p, q = fermat_factor(n)
    e = next_prime(p >> (512 // 4))
    
    Ep = EllipticCurve(GF(p), [a,b])
    Eq = EllipticCurve(GF(q), [a,b])
    dp = pow(e, -1, Ep.order())
    dq = pow(e, -1, Eq.order())
    Gp = int(dp) * Ep((Ax, Ay))
    Gq = int(dq) * Eq((Ax, Ay))

    gx = crt([int(Gp[0]), int(Gq[0])], [p,q])
    key = md5(str(gx).encode()).digest()   

    cipher = AES.new(key, AES.MODE_CBC, bytes.fromhex(iv))
    flag = unpad(cipher.decrypt(bytes.fromhex(ct)), 16).decode()
    print(flag)

def main():
    HOST, PORT = sys.argv[1].split(":")
    io = remote(HOST, PORT)
    exploit(io)


if __name__ == "__main__":
    main()
