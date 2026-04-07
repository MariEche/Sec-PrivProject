# handles encrypting and decrypting passwords

def encrypt_password(password):
    password_characters = list(password)
    for i in range(len(password_characters)):
        password_characters[i] = chr(ord(password_characters[i]) + 2)
    encrypted_password = "".join(password_characters)
    return encrypted_password

def decrypt_password(encrypted_password):
    password_characters = list(encrypted_password)
    for i in range(len(password_characters)):
        password_characters[i] = chr(ord(password_characters[i]) - 2)
    decrypted_password = "".join(password_characters)
    return decrypted_password