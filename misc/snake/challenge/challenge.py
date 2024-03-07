#!/usr/bin/env python2

from flag import FLAG

inp = input("Enter your input:\n>>> ")

if len(str(inp)) > 3:
    print(len(str(inp)))
    print("No no!, Long input")
    exit()

print(len(str(inp)))


if inp > 10e99:
    print(FLAG)


