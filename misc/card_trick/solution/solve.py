import itertools
from pwn import *

def de_bruijn_sequence(n, characters):
    k = len(characters)
    a = [0] * k * n
    sequence = []

    def db(t, p):
        if t > n:
            if n % p == 0:
                for j in range(1, p + 1):
                    sequence.append(characters[a[j]])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                db(t + 1, t)
    
    db(1, 1)
    
    return ' '.join(sequence + sequence[:n - 1])

n = 4
dec = []
faces = ['Jack','Queen', 'King', 'Ace']
suits = ['Clubs','Hearts','Spades', 'Diamonds']
for i in faces:
    for j in suits:
        dec.append(f'{i}_{j}')

MAX_DIGITS = (2 ** 16) 
de_bruijn_seq = de_bruijn_sequence(n, dec).split(' ')[:MAX_DIGITS]
de_bruijn_seq = ' '.join(de_bruijn_seq)
io = process('./chall.py')
for i in range(20):
    print(f'{i=}')
    io.recvuntil('Attempt>')
    io.sendline(de_bruijn_seq)

io.interactive()
