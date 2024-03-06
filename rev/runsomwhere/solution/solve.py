from Crypto.Cipher import ChaCha20
import binascii
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <encrypted_file>")
    sys.exit(1)

key_hex = "a22427226377cc867d51ad3f130af08ad13451de7160efa2b23076fd782de967"
nonce_hex = "ea9f11f8dfb0ca08a8810f9e"

input_file = sys.argv[1]
output_file = f"decrypted_{input_file}"

with open(input_file, 'rb') as file:
    encrypted_data = file.read()

key = binascii.unhexlify(key_hex)
nonce = binascii.unhexlify(nonce_hex)

cipher = ChaCha20.new(key=key, nonce=nonce)
decrypted_data = cipher.decrypt(encrypted_data)

with open(output_file, 'wb') as file:
    file.write(decrypted_data)
