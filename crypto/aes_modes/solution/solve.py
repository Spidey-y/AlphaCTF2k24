from pwn import remote, process, args, xor

if args.REMOTE:
    io = remote('0.0.0.0', 1337)
else:
    io = process('./chall.py')


def send_payload(choice, payload):
    io.sendlineafter('choose an option: ', choice)
    if choice != '1':
        io.sendline(payload)
    res = io.recvline().split(b': ')[-1].strip()
    return res

BLOCK_SIZE = 32

enc = send_payload('1', 'asdf')
dec = []
iv=b'\x00'*16
for i in range(0, len(enc), BLOCK_SIZE):
    dec_aes = send_payload('3', enc[i:i+BLOCK_SIZE]).decode()
    dec.append(xor(bytes.fromhex(dec_aes), iv))
    iv = dec[i//BLOCK_SIZE]

print(b''.join(dec))
