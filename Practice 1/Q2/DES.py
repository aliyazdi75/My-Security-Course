from Crypto.Cipher import DES3
from Crypto import Random

key = '133457799BBCDFF1'
iv = Random.new().read(DES3.block_size)
cipher_encrypt = DES3.new(key, DES3.MODE_OFB, iv)
plaintext = '0123456789ABCDEF'
encrypted_text = cipher_encrypt.encrypt(plaintext)

cipher_decrypt = DES3.new(key, DES3.MODE_OFB, iv)
cipher_decrypt.decrypt(encrypted_text)
cipher_decrypt.decrypt(encrypted_text)

print(plaintext)
print(encrypted_text)
