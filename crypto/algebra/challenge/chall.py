from Crypto.Util.number import bytes_to_long, getPrime
from flag import FLAG

p = getPrime(512)
q = getPrime(512)
s = getPrime(2048)
n = p*q
e = 65537
m = bytes_to_long(FLAG)
c = pow(m, e, n)

gift = pow(p, s+2, s)
print(f'{c=}')
print(f'{n=}')
print(f'{e=}')
print(f'{gift=}')
