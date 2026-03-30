#!/usr/bin/env python3


from pwn import *
import time
import random

host, port = sys.argv[1].split(":")
io = remote(host, port)

seed = int(time.time())
random.seed(seed)

extraction_1 = []
solution_1 = ""
while len(extraction_1) < 5:
    r1 = random.randint(1, 90)
    if(r1 not in extraction_1):
        extraction_1.append(r1)
        solution_1 += str(r1) + " "

extraction_2 = []
solution_2 = ""
while len(extraction_2) < 5:
    r2 = random.randint(1, 90)
    if(r2 not in extraction_2):
        extraction_2.append(r2)
        solution_2 += str(r2) + " "

io.sendline(solution_2)
io.interactive()
