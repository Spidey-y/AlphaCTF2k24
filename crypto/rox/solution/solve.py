#!/bin/python

from pwn import xor


ct = [b'\x06\x06a) "*$', b't&\x18FU\x02AJ', b'\x1bQ8.:ua2', b't#\x18YU\x07\nA', b"TK}+0'c2", b't2\x12^B\x07\x05^', b'\x15U2\x1f.wm?', b'V\x01tdI\x102G', b'fs+UmOT2', b'\x08\x0e\x0b?\x18< \x12', b'i.{^|XI|', b'\x0eo:\x1f=\x19\x08=', b'O.{^|XI|']

pt = ct

for i in range(len(pt)-1, 0, -1):
    pt[i] = xor(ct[i-1], ct[i])

pt[0] = xor(pt[len(pt)-1], ct[0])

flag = b''.join(pt)
print(flag)