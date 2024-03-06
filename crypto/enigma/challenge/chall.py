#!/usr/bin/env python3
import random
import time
from flag import FLAG

def generate_padding():
    length = random.randint(30, 70)
    a = [chr(random.randint(ord('a'), ord('z'))) for i in range(length)]
    return "".join(a)

def encrypt(plain, key):
    if plain.isalpha():  
        if plain.isupper():
            return chr((ord(plain) + key - ord('A')) % 26 + ord('A'))
        else:
            return chr((ord(plain) + key - ord('a')) % 26 + ord('a'))
    else:
        return plain  
    
def initialize():
    seed = int(time.time())
    random.seed(seed)

initialize()

pad1 = generate_padding()
pad2 = generate_padding()
pad3 = generate_padding()

index1 = random.randint(len(FLAG)//3, len(FLAG))
index2 = random.randint(len(FLAG)//3, len(FLAG))
index3 = random.randint(len(FLAG)//3, len(FLAG))

FLAG = FLAG[:index1]+pad1+FLAG[index1:]
FLAG = FLAG[:index2]+pad2+FLAG[index2:]
FLAG = FLAG[:index3]+pad3+FLAG[index3:]

enc = ''

for i in range(len(FLAG)):
    key = random.randint(0, 100)
    enc+=encrypt(FLAG[i], key) 
enc = list(enc)
random.shuffle(enc)

print(''.join(enc))
