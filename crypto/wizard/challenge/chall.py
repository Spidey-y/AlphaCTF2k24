#!/usr/bin/env python3

from Crypto.Util.number import getPrime, bytes_to_long
from flag import FLAG

p = getPrime(490)

def encrypt(m, i):
    exp = 2 **((i%4)+4)
    enc = pow(m, exp, p)
    return enc

def chunks(string, chunk_size):
    chunks = []
    for i in range(0, len(string), chunk_size):
        chunks.append(string[i:i + chunk_size])
    return chunks

flag_chunks = chunks(FLAG, 60)

out = []

for i, c in enumerate(flag_chunks):
    tmp = encrypt(bytes_to_long(c.encode()), i)
    out.append(tmp)

with open('out.py', 'w') as f:
    f.write(f'{p=}\n')
    f.write(f'{out=}')



