from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


aes_key = get_random_bytes(16)

cipher = AES.new(aes_key, AES.MODE_CTR)

plaintext = "Secret message!"
print(f"Plain text: {plaintext}")

cipher_text = cipher.encrypt(plaintext.encode())
print(f"Cipher Text: {cipher_text}")

plaintext = AES.new(aes_key, AES.MODE_CTR, nonce=cipher.nonce).decrypt(cipher_text).decode()
print(f"Plain Text: {plaintext}")


