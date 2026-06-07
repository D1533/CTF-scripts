#!/usr/bin/env python3

import os
from hashlib import sha256
import hmac
from random import randint
from Crypto.Util.number import long_to_bytes


class Server:
    def __init__(self):
        self.N = int("ffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd1"
                    "29024e088a67cc74020bbea63b139b22514a08798e3404dd"
                    "ef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245"
                    "e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7ed"
                    "ee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3d"
                    "c2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f"
                    "83655d23dca3ad961c62f356208552bb9ed529077096966d"
                    "670c354e4abc9804f1746c08ca237327ffffffffffffffff", 16)
        self.g = 2
        self.k = 3
        self.salt = os.urandom(8)
        self.v = None
        self.u = None

        self.A = None
        self.b = randint(1, self.N)
        self.B = None
        self.S = None
        self.K = None
        self.HMAC_proof = None

    def send_parameters(self, Client):
        Client.N = self.N
        Client.g = self.g
        Client.k = self.k
    
    def send_pubkeys(self, Client):
        self.B = (self.k * self.v + pow(self.g, self.b, self.N)) % self.N
        Client.salt = self.salt
        Client.B = self.B
    
    def receive_password(self, Client):
        xH = sha256(self.salt + Client.password).hexdigest()
        x = int(xH, 16)
        self.v = pow(self.g, x, self.N)
    
    def compute(self):
        uH = sha256(long_to_bytes(self.A) + long_to_bytes(self.B)).hexdigest()
        self.u = int(uH, 16)
        self.S = pow(self.A*pow(self.v, self.u, self.N), self.b, self.N) 
        self.K = sha256(long_to_bytes(self.S)).digest()

    def validate_HMAC(self, Client):
        return "OK" if (Client.HMAC_proof == hmac.new(self.K, self.salt, sha256).digest()) else "Wrong"

class Client:
    def __init__(self):
        self.N = None
        self.g = None
        self.k = None
        self.salt = None
        self.a = None
        self.A = None
        self.B = None
        self.u = None 
        self.S = None
        self.K = None
        self.HMAC_proof = None
        self.password = os.urandom(32)
    
    def compute_pubkey(self):
        self.a = randint(1, self.N)
        self.A = pow(self.g, self.a, self.N)

    def send_pubkey(self, Server):
        Server.A = self.A
    
    def compute(self):
        uH = sha256(long_to_bytes(self.A) + long_to_bytes(self.B)).hexdigest()
        self.u = int(uH, 16)
        xH = sha256(self.salt + self.password).hexdigest()
        x = int(xH, 16)
        self.S = pow(self.B - self.k * pow(self.g, x, self.N), self.a + self.u*x, self.N)
        self.K = sha256(long_to_bytes(self.S)).digest()
    
    def compute_HMAC(self):
        self.HMAC_proof = hmac.new(self.K, self.salt, sha256).digest()


# Client logs in
S = Server()
C = Client()

S.send_parameters(C)
S.receive_password(C)

C.compute_pubkey()
C.send_pubkey(S)
S.send_pubkeys(C)

C.compute()
S.compute()

C.compute_HMAC()
print(S.validate_HMAC(C))


# Attacker, A = 0 ==> S = 0
Attacker = Client()
Attacker.password = b"Unknown"

Attacker.a = randint(1, S.N)
Attacker.A = 0
Attacker.send_pubkey(S)
S.send_pubkeys(Attacker)

S.compute()
Attacker.K = sha256(long_to_bytes(0)).digest()
Attacker.compute_HMAC()
print(S.validate_HMAC(Attacker))



