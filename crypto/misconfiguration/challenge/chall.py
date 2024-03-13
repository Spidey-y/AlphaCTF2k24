from Crypto.Util.number import bytes_to_long, getPrime
from flag import FLAG
from Crypto.Util.number import long_to_bytes
from gmpy2 import iroot, gcdext, gcd
from sympy.residue_ntheory import is_primitive_root, is_quad_residue

n = getPrime(1024)
phi = n-1

for i in range(40, 100):
    if gcd(phi, i) == 2 and not iroot(i, 2)[1]:
        e = i
        break

print(e)
print(gcd(phi, e))

m = bytes_to_long(FLAG)
c = pow(m, e, n)
print(f'{m=}')
print(f'{c=}')
print(f'{n=}')
print(f'{e=}')

d = gcdext(e, phi)
print(d)
print(is_quad_residue(c))
flag_2 = pow(c, d[1], n)

flag, is_root = iroot(flag_2, gcd(phi, e))

print(long_to_bytes(flag))