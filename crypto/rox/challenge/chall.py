#!/bin/python

from flag import flag
from pwn import xor


BLOCK_SIZE = 8

flag = flag.ljust(100, b'\x41')

pt = [(flag[i:i + BLOCK_SIZE]) for i in range(0, len(flag), BLOCK_SIZE)]

ct = pt

for i in range(len(pt)):
    ct[i] = xor(ct[i],pt[i-1])

print(ct)
