from storage import save_password, read_passwords, search_password

print("1. Save password")
print("2. View saved passwords")
print("3. Search by a website")

choice = input("Choose an option: ")

if choice == "1":
    website = input("Enter website: ")
    encrypted_password = input("Enter an encrypted password: ")

    save_password(website, encrypted_password)
    print("Password saved successfully.")

elif choice == "2":
    saved_passwords = read_passwords()

    if len(saved_passwords) == 0:
        print("No passwords saved.")
    else:
        print("\nSaved Passwords:")
        for website, encrypted_password in saved_passwords:
            print(website + " -> " + encrypted_password)

elif choice == "3":
    website_name = input("Enter a website to search: ")
    result = search_password(website_name)

    if result is None:
        print("Website not found.")
    else:
        print("Encrypted Password:", result)

else:
    print("Invalid.")