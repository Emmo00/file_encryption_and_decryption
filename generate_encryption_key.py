from cryptography.fernet import Fernet

# Key generation
key = Fernet.generate_key()

# Store key in a .key file
with open("encryption_key.key", "wb") as file:
    file.write(key)