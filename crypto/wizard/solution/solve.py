#!/usr/bin/env python3

from Crypto.Util.number import long_to_bytes
from sympy.ntheory.residue_ntheory import sqrt_mod, is_quad_residue
from out import p, out

def get_sq(sq):
    for i in sq:
        if is_quad_residue(i, p):
            res = sqrt_mod(i, p, all_roots=True)
    return res

def get_all_sq(x, i):
    sq0 = [x]
    sq1 = []
    for _ in range(i):
        sq1 = get_sq(sq0)
        sq0 = sq1
    return sq1

def get_sqrts(x, exp):
    match exp:
        case 16:
            return get_all_sq(x, 4)
        case 32:
            return get_all_sq(x, 5)
        case 64:
            return get_all_sq(x, 6)

flag = ''
for i, o in enumerate(out):
    sqrt = get_sqrts(o, 2**((i%4)+4))
    for i in sqrt:
        try:
            tmp = long_to_bytes(i).decode()
            flag += tmp
        except:
            pass
print(flag)


