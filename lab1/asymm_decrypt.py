import argparse
from Crypto.Hash import SHA256
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA


def rsa_decrypt(private_key, aes_key):
  cipher = PKCS1_OAEP.new(key=private_key, hashAlgo=SHA256)
  enc_aes_key = cipher.decrypt(aes_key)
  return enc_aes_key

def read_and_decrypt(private_key_path, encrypt_bin_path):
  passphrase = b"classified" # bad practice
  private_key = RSA.import_key(open(private_key_path).read(), passphrase=passphrase)
  with open(encrypt_bin_path, "rb") as file:
    tag = file.read(16)
    nonce = file.read(16)
    enc_aes_key = file.read(private_key.size_in_bytes())
    cipher_text = file.read(16)
  
  aes_key = rsa_decrypt(private_key, enc_aes_key)
  cipher_aes = AES.new(key=aes_key, mode=AES.MODE_EAX, nonce=nonce)
  plain_text = cipher_aes.decrypt_and_verify(cipher_text, tag).decode()
  
  return plain_text

  


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("private_key_path", help="your private key file path")
  parser.add_argument("encrypt_bin_path", help="your cipher text and session key, nonce and tag")
  args = parser.parse_args()
  plain_text = read_and_decrypt(args.private_key_path, args.encrypt_bin_path)
  print(plain_text)
