#!/usr/bin/env python3

from pwn import *
import json

user1 = "TEXTCOLLBYfGiJUETHQ4hAcKSMd5zYpgqf1YRDhkmxHkhPWptrkoyz28wnI9V0aHeAuaKnak"
user2 = "TEXTCOLLBYfGiJUETHQ4hEcKSMd5zYpgqf1YRDhkmxHkhPWptrkoyz28wnI9V0aHeAuaKnak"

host, port = sys.argv[1].split(":")
io = remote(host, port)
io.recv()
io.sendline(json.dumps({"option":"register"}).encode())
io.sendline(json.dumps({"username":user1,"password":"password"}).encode())

io.recv()
io.sendline(json.dumps({"option":"login"}).encode())
io.sendline(json.dumps({"username":user2,"password":"password"}).encode())

io.recvuntil(b"shutting down the system :: ")
flag = io.recvline().decode()
print(flag)


