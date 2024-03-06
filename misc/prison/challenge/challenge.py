#!/usr/bin/env python3

from whitelist import whitelist

inp = input("Enter your inp:\n>>> ").lower()


if len(inp) > 137:
    print("No no!, Long input")
    exit()

if any([i not in whitelist for i in inp]):
    print("No no!, Invalid Input")
    exit()

try:
    exec(eval(inp))
except:
    print("ERROR Try again !!")

