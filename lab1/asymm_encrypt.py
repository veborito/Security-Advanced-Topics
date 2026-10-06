import argparse
from Crypto.Hash import SHA256
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

def retrieve_info(file):
  public_key = RSA.import_key(open(file, "rb").read())
  return public_key

def aes_key_cipher():
  key = get_random_bytes(16)
  cipher = AES.new(key=key, mode=AES.MODE_EAX)
  return key, cipher

def rsa_encrypt(public_key, aes_key):
  cipher = PKCS1_OAEP.new(key=public_key, hashAlgo=SHA256)
  enc_aes_key = cipher.encrypt(aes_key)
  return enc_aes_key

def aed_encrypt(plaintext, file):
  public_key = retrieve_info(file)
  aes_key, cipher_aes = aes_key_cipher()
  cipher_text, tag = cipher_aes.encrypt_and_digest(plaintext=plaintext.encode())
  enc_key_aes = rsa_encrypt(public_key, aes_key)
  
  with open("encrypted.bin", "wb") as file:
    file.write(tag)
    file.write(cipher_aes.nonce)
    file.write(enc_key_aes)
    file.write(cipher_text)
  return
  


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("message", help="your message to encrypt")
  parser.add_argument("public_key_path", help="your public key file path")
  args = parser.parse_args()
  aed_encrypt(args.message, args.public_key_path)
