import string
from pwn import remote, process, args

if args.REMOTE:
    io = remote('0.0.0.0', 1337)
else:
    io = process('../challenge/chall.py')


def encrypt_flag():
    io.sendlineafter('option:', '1')
    io.recvlines(2)
    res = io.recvline().decode().strip()
    return res
def encrypt(inp):
    io.sendlineafter('option:', '2')
    io.sendlineafter('you:', inp)
    io.recvline()
    res = io.recvline().decode().strip()
    return res

enc = encrypt_flag()

flag = ''
blockSize = 32
found = False
while not found:
    found = True
    for c in string.ascii_letters+'{0123456789_}':
        tmp = encrypt(flag+c)
        if tmp == enc[:len(flag+c)*blockSize]:
            flag += c
            print(flag)
            found = False