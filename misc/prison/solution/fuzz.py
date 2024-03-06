from pwn import * 
import string

chars = ''
for i in string.printable:
    io = process('../challenge/challenge.py')
    io.recvuntil('>>>')
    io.sendline(i)
    res = io.recvline()
    if b'No no!, Invalid Input' not in res:
        chars += i

print(chars)