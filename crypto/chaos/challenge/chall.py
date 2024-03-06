#!/usr/bin/env python3

from Crypto.Util.number import bytes_to_long
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from flag import FLAG
from random import getrandbits 


def getRandom(bits, rounds):
    for _ in range(rounds):
        a = getrandbits(bits)
        print(f'{a}')
    a = getrandbits(bits)
    return a.to_bytes(32, 'little')


key = getRandom(256, 100)
iv = b"alpha_gift_for_u"

cipher = AES.new(key, AES.MODE_CBC, iv)
enc = cipher.encrypt(pad(FLAG,AES.block_size))
print(f'enc={bytes_to_long(enc)}')
