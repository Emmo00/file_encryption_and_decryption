from cryptography.fernet import Fernet

def generate_key():
    # Key generation
    key = Fernet.generate_key()
    
    # Store key in a .key file
    with open("encryption_key.key", "wb") as file:
        file.write(key)
