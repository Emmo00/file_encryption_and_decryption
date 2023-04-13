from cryptography.fernet import Fernet

def encrypt(in_filename, out_filename):
    # get the key
    with open("encryption_key.key", "rb") as file:
        key = file.read()

    fernet = Fernet(key)

    # opening file to encrpt
    with open(in_filename, "rb") as file:
        fileToEncrypt = file.read()

    # Encrpting file
    encrypted = fernet.encrypt(fileToEncrypt)

    # write it back
    with open(out_filename, "wb") as file:
        file.write(encrypted)
