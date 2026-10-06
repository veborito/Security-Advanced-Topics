from Crypto.PublicKey import RSA

keypair = RSA.generate(3072)
public_key = keypair.public_key().export_key()

with open("public_key.pem", "wb") as f:
  f.write(public_key)

passphrase = b"classified" # bad practice
protection = "PBKDF2WithHMAC-SHA512AndAES256-CBC"
prot_params = {"iteration_count": 131072}
private_key = keypair.export_key(passphrase=passphrase, pkcs=8,
                                protection=protection, 
                                prot_params=prot_params)

with open("private_key.pem", "wb") as f:
  f.write(private_key)
