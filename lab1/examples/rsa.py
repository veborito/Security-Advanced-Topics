from Crypto.PublicKey import RSA

keypair = RSA.generate(3072)
public_key = keypair.public_key().export_key().decode()

print(f"Public key: {public_key}")

passphrase = b"classified"
protection = "PBKDF2WithHMAC-SHA512AndAES256-CBC"
prot_params = {"iteration_count": 131072}
privatekey = keypair.export_key(passphrase=passphrase, pkcs=8,
                                protection=protection, 
                                prot_params=prot_params).decode()

print(f"private key: {privatekey}")
