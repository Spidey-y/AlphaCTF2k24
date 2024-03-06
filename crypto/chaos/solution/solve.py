from Crypto.Cipher import AES
from randcrack import RandCrack
from pwn import *
from Crypto.Util.number import long_to_bytes

def chunk(s, n):
    # split the given string to chunks of size n
    return [s[i:i + n] for i in range(0, len(s), n)]

def crack(numbers, bits):
    rc = RandCrack()
    split_numbers = []
    for n in numbers:
        #convert integer to hex number padded with zeros to the right to be of size bits//4 
        v = hex(n).replace("0x", "").rjust(bits // 4, "0")
        for c in chunk(v, 8)[::-1]:
            split_numbers.append(int(c, 16))
    for n in split_numbers[-624:]:
    # the random cracker needs 624 last generated number to update the local state
        rc.submit(n)
    return rc

if args.REMOTE:
    io = remote('0.0.0.0', 1337)
else:
    io = process('../challenge/chall.py')



numbers = []
for i in range(100):
    tmp = int(io.recvline().strip())
    numbers.append(tmp)
enc = long_to_bytes(int(io.recvline()[4:].strip()))

rc = crack(numbers, 256)

key = rc.predict_getrandbits(256).to_bytes(32, 'little')

iv = b'alpha_gift_for_u'


cipher = AES.new(key, AES.MODE_CBC, iv)
dec = cipher.decrypt(enc)
print(dec)