from cryptography.fernet import Fernet

# getting encrption key
with open("encryption_key.key", "rb") as file:
    key = file.read()

fernet = Fernet(key)

# get file to encrypt
with open("script.py", "rb") as file:
    encrypted = file.read()

decrypted = fernet.decrypt(encrypted)

# wite the decrypted file back
with open("script.py", "wb") as file:
    file.write(decrypted)