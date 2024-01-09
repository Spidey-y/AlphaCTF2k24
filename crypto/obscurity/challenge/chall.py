#!/usr/bin/env python3

from Crypto.Util.number import bytes_to_long, isPrime


FLAG=b'AlphaCTF{WHO_C4R3$_4B0U7_N_1F_1_H4V3_7h3_f4c7or$}'

n = 1
e = 65537
for i in range(10000):
    if isPrime(i):
        n *= i

m = bytes_to_long(FLAG)

c = pow(m, e, n)

print(f'{e=}')
print(f'{c=}')
print(f'{n=}')
