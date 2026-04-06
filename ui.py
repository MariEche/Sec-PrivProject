from encrypt import encrypt_password, decrypt_password
from storage import save_password
import tkinter as tk

def encrypt():
    website = website_entry.get()
    password = password_entry.get()
    key = key_entry.get()

    encrypted = encrypt_password(password, key)

    save_password(website, encrypted)

    result_label.config(text=f"Encrypted: {encrypted}")

def decrypt():
    encrypted_text = password_entry.get()
    key = key_entry.get()

    decrypted = decrypt_password(encrypted_text, key)

    result_label.config(text=f"Decrypted: {decrypted}")

# main window
root = tk.Tk()
root.title("Password Tool")
root.geometry("300x250")

# labels + inputs
tk.Label(root, text="Website").pack()
website_entry = tk.Entry(root)
website_entry.pack()

tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root)
password_entry.pack()

tk.Label(root, text="Key").pack()
key_entry = tk.Entry(root)
key_entry.pack()

# buttons
tk.Button(root, text="Encrypt", command=encrypt).pack(pady=5)
tk.Button(root, text="Decrypt", command=decrypt).pack(pady=5)

# result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()