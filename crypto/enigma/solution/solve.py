#!/usr/bin/env python3
import random
import time
from pwn import *

def generate_padding():
    length = random.randint(30, 70)
    a = [chr(random.randint(ord('a'), ord('z'))) for i in range(length)]
    return "".join(a)

def decrypt(plain, key):
    if plain.isalpha():  
        if plain.isupper():
            return chr((ord(plain) + key - ord('A')) % 26 + ord('A'))
        else:
            return chr((ord(plain) + key - ord('a')) % 26 + ord('a'))
    else:
        return plain  
    
def unshuffle(shuffled):
    shuffled_list = list(shuffled)
    indices = list(range(len(shuffled_list)))
    random.shuffle(indices)
    unshuffled_list = [None] * len(shuffled_list)
    for i, j in zip(indices, range(len(shuffled_list))):
        unshuffled_list[i] = (shuffled_list[j])
    unshuffled = ''.join(unshuffled_list)
    return unshuffled

def initialize(seed):
    random.seed(seed)

if args.REMOTE:
    io = remote('0.0.0.0', 1337)
else:
    io = process('../challenge/chall.py')
    
cipher = io.recvline().decode().strip()

init_time = int(time.time())

for i in range(0, 10):
    initialize(init_time-i)
    pad1 = generate_padding()
    pad2 = generate_padding()
    pad3 = generate_padding()
    flag_length  = len(cipher) - len(pad1)- len(pad2)- len(pad3)
    index1 = random.randint(flag_length//3, flag_length)
    index2 = random.randint(flag_length//3, flag_length)
    index3 = random.randint(flag_length//3, flag_length)
    flag = ''
    key = [None]*len(cipher)
    for i in range(len(cipher)):
        key[i] = random.randint(0, 100)
    f = unshuffle(cipher)
    for i in range(len(cipher)):
        flag+=decrypt(f[i], -key[i]) 
    flag = flag[:index3]+flag[index3+len(pad3):]
    flag = flag[:index2]+flag[index2+len(pad2):]
    flag = flag[:index1]+flag[index1+len(pad1):]
    if 'Alpha' in flag:
        print(flag)
        exit()
