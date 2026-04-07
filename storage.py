# handles saving and reading passwords from file
import os

def save_password(website, encrypted_password):
    if not website.strip() or not encrypted_password.strip():
        print("Website or password cannot be empty.")
        return

    with open("passwords.txt", "a") as file:
        file.write(f"{website}:{encrypted_password}\n")


def read_passwords():
    saved_data = []
    if not os.path.exists("passwords.txt"):
        return saved_data

    with open("passwords.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(":", 1)
                if len(parts) == 2:
                    website, encrypted_password = parts
                    saved_data.append((website, encrypted_password))

    return saved_data


def search_password(website_name):
    saved_data = read_passwords()

    for website, encrypted_password in saved_data:
        if website.lower() == website_name.lower():
            return encrypted_password

    return None