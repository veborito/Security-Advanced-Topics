from Crypto.Cipher import ChaCha20_Poly1305
from Crypto.Random import get_random_bytes


key = get_random_bytes(32)
header = b"header"
cipher = ChaCha20_Poly1305.new(key=key)

plaintext = "Secret message!"
print(f"Plain text: {plaintext}")

cipher_text, tag = cipher.encrypt_and_digest(plaintext=plaintext.encode())
print(f"Cipher Text: {cipher_text}")
print(f"Tag: {tag}")

plaintext = ChaCha20_Poly1305.new(key=key, nonce=cipher.nonce).decrypt_and_verify(cipher_text, tag).decode()
print(f"Plain Text: {plaintext}")


