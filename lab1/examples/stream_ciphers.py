from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes


key = get_random_bytes(32)
cipher = ChaCha20.new(key=key)

plaintext = "Secret message!"
print(f"Plain text: {plaintext}")

cipher_text = cipher.encrypt(plaintext.encode())
print(f"Cipher Text: {cipher_text}")

plaintext = ChaCha20.new(key=key, nonce=cipher.nonce).decrypt(cipher_text).decode()
print(f"Plain Text: {plaintext}")


