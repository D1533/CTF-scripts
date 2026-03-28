#!/usr/bin/env python3

numbers = [16,9,3,15,3,20,6, '{',20,8,5,14,21,13,2,5,18,19,13,1,19,15,14, '}']

flag = "".join(chr(ord('A')+n-1) if isinstance(n,int) else n for n in numbers)
print(flag)
