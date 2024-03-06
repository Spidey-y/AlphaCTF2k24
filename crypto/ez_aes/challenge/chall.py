#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from flag import FLAG
import random

KEY = random.randbytes(16)

def encrypt(plaintext):
    p = ''
    for i in plaintext:
        p += i*16
    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        encrypted = cipher.encrypt(p.encode())
    except ValueError as e:
        return str(e)

    return encrypted.hex()

print('welcome to my encryptor')
print('you have two options')
print('1 - encrypt the flag')
print('2 - encrypt your input')
while True:
    choice = input('choose an option: ')
    if choice == '1':
        print('here is the flag encrypted in a weird way\n')
        enc = encrypt((FLAG))
        print(enc)
        print()
    if choice == '2':
        inp = input('enter your plaintext and i will encrypt it for you: ')
        enc = encrypt((inp))
        print()
        print(enc)
        print()
