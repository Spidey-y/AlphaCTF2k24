#!/usr/bin/env python3
from os import environ
from sys import exit


flag = environ.get("FLAG", "flag{FAKE_FLAG}")
blacklist = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?*^\t\n\r\x0b\x0c "
input = str(input("Prove me you're a real wizard: \n>>> ")
            ).encode('ascii', 'ignore').decode('ascii')


if any((c in blacklist) for c in input):
    print("Nope, you're a muggle.")
    exit()

if eval(input) == 101:
    print(f"Congratz! wizzard, Here's your flag: {flag}")
    exit()
else:
    print("Nope, you're a muggle.")
    exit()
