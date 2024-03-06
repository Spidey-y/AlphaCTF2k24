#!/usr/bin/env python3
from Crypto.Cipher import AES
from flag import FLAG
import random

KEY = random.randbytes(16)

def decrypt_ecb(ciphertext):
    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return str(e)
    return decrypted
def decrypt_ctr(ciphertext):
    cipher = AES.new(KEY, AES.MODE_CTR)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return str(e)
    return decrypted
def decrypt_cfb(ciphertext):
    cipher = AES.new(KEY, AES.MODE_CFB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return str(e)
    return decrypted
def decrypt_ofb(ciphertext):
    cipher = AES.new(KEY, AES.MODE_CFB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return str(e)
    return decrypted
def encrypt(plaintext, iv):
    plaintext = plaintext.ljust(BLOCK_SIZE, '\x00')
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    try:
        encrypted = cipher.encrypt(plaintext.encode())
    except ValueError as e:
        return str(e)
    return encrypted

print("welcome hacker, today's lesson is about AES")
print("1 - encrypt flag with cbc")
print("2 - decrypt flag with ctr")
print("3 - decrypt flag with ecb")
print("4 - decrypt flag with cfb")
print("5 - decrypt flag with 0fb")

while True:
    iv=b'\x00'*16
    option = input("choose an option: ")  
    if option == '1':
        BLOCK_SIZE = 16
        flag_chunks = [(FLAG[i:i + BLOCK_SIZE]) for i in range(0, len(FLAG), BLOCK_SIZE)]
        enc = []
        for i in range(len(flag_chunks)):
            enc.append(encrypt(''.join(flag_chunks[i]), iv))
            iv = flag_chunks[i].encode()
        print(b''.join(enc).hex())
    elif option == '2':
        ct = input('enter you ciphertext: ')
        print(decrypt_ctr(bytes.fromhex(ct)).hex())
    elif option == '3':
        ct = input('enter you ciphertext: ')
        print(decrypt_ecb(bytes.fromhex(ct)).hex())
    elif option == '4':
        ct = input('enter you ciphertext: ')
        print(decrypt_cfb(bytes.fromhex(ct)).hex())  
    elif option == '5':
        ct = input('enter you ciphertext: ')
        print(decrypt_ofb(bytes.fromhex(ct)).hex())  
    else:
        print('INVALID INPUT !!')