from cryptography.fernet import Fernet

def decrypt(in_filename, out_filename):
    # getting encrption key
    with open("encryption_key.key", "rb") as file:
        key = file.read()

    fernet = Fernet(key)

    # get file to encrypt
    with open(in_filename, "rb") as file:
        encrypted = file.read()

    decrypted = fernet.decrypt(encrypted)

    # wite the decrypted file back
    with open(out_filename, "wb") as file:
        file.write(decrypted)
