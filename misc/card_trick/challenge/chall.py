#!/usr/bin/env python3
import random
from flag import FLAG
dec = []
F = ['Jack','Queen', 'King', 'Ace']
S = ['Clubs','Hearts','Spades', 'Diamonds']
for i in F:
    for j in S:
        dec.append(f'{i}_{j}')

MAX_DIGITS = (2 ** 16)
def card_trick() -> bool:

    pin = [random.choice(dec) for _ in range(4)]
    digits = ["*", "*", "*", "*"]
    counter = 0

    print("What are the 4 cards that i choosed")

    while True:
        attempt = input(f"Attempt>")
        attempt = attempt.split(' ')
        for _ in range(len(attempt)):
            digits.insert(0, attempt.pop())
            digits.pop()
            if " ".join(digits) == " ".join(pin):
                return True
            counter += 1
            if counter > MAX_DIGITS:
                return False


for n in range(20):

    print(f"You've made it to level #{n+1}.\n")

    if not card_trick():
        print("You lost ")
        exit()

print(f"GG you won here is your flag: {FLAG}")


