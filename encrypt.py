from cryptography.fernet import Fernet


# get the key
with open("encryption_key.key", "rb") as file:
    key = file.read()

fernet = Fernet(key)

# opening file to encrpt
with open("script.py", "rb") as file:
    fileToEncrypt = file.read()

# Encrpting file
encrypted = fernet.encrypt(fileToEncrypt)

# write it back
with open("script.py", "wb") as file:
    file.write(encrypted)