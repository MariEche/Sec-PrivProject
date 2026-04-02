import bcrypt
salt = bcrypt.gensalt()

correct_password = "$2b$12$51UGFYdwfqfxbfMBscUVNuIA.PPH5aeyiRyfhE3bT645VGoDZ/ltG"
access_password = input("Enter your password to access the program: ")
if bcrypt.checkpw(access_password.encode('utf-8'), correct_password.encode('utf-8')):
    print("Access granted!")
    choice = input("Do you want to encrypt a password? (yes/no): ")
    if choice.lower() == "yes":
        password = input("Enter a password: ")
        website = input("Enter the website: ")
        
        password_characters = list(password)
        for i in range(len(password_characters)):
            password_characters[i] = chr(ord(password_characters[i]) + 2)
            encrypted_password = "".join(password_characters)
        print(website,": ", encrypted_password)
    if choice.lower() == "no":
        toDecrypt = input("Enter the encrypted password to decrypt: ")
        toDecrypt_characters = list(toDecrypt)
        for i in range(len(toDecrypt_characters)):
            toDecrypt_characters[i] = chr(ord(toDecrypt_characters[i]) - 2)
        decrypted_password = "".join(toDecrypt_characters)
        print("Decrypted password: ", decrypted_password)

else:
    print("Access denied!")
