# handles saving and reading passwords from file

def save_password(website, encrypted_password):
    if website.strip() == "" or encrypted_password.strip() == "":
        print("Website or password cannot be empty.")
        return

    with open("passwords.txt", "a") as file:
        file.write(website + ":" + encrypted_password + "\n")


def read_passwords():
    saved_data = []

    try:
        with open("passwords.txt", "r") as file:
            for line in file:
                line = line.strip()

                if line != "":
                    parts = line.split(":", 1)

                    if len(parts) == 2:
                        website = parts[0]
                        encrypted_password = parts[1]
                        saved_data.append((website, encrypted_password))

    except FileNotFoundError:
        print("No saved passwords found yet.")

    return saved_data


def search_password(website_name):
    saved_data = read_passwords()

    for website, encrypted_password in saved_data:
        if website.lower() == website_name.lower():
            return encrypted_password

    return None