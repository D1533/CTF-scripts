#!/usr/bin/env python3

def exploit(chars, flags):
    flag = b""
    for char, f in zip(chars, flags):
        if f & (1 << 4):
            char ^= 0x3e
        if f & (1 << 3):
            char ^= 0x6b
        if f & (1 << 1):
            char = 255 - char
        if f & (1 << 6):
            b = char ^ 0xbd 
            this_msb = (b >> 4) 
            this_lsb = b & 0xf
            char = (this_lsb << 4) | this_msb
        flag += bytes([char])
    
    print(flag.decode())

def main():
    with open("output.txt") as f:
        values = f.readline().split(" ")

    chars = []
    flags = []
    for i in range(0, len(values), 2):
        chars.append(int(values[i]))
        flags.append(int(values[i+1]) ^ 0x4a)

    exploit(chars, flags)

if __name__ == "__main__":
    main()

