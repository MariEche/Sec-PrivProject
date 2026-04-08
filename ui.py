from storage import save_password, read_passwords
from encrypt import encrypt_password, decrypt_password
import tkinter as tk

def encrypt():
    website = website_entry.get()
    password = password_entry.get()

    if website.strip() == "" or password.strip() == "":
        result_label.config(text="❌ Fill all fields")
        return

    if len(password) < 6:
        result_label.config(text="❌ Password too short (min 6 chars)")
        return

    encrypted = encrypt_password(password)

    saved = read_passwords()
    for w, p in saved:
        if encrypted == p:
            result_label.config(text="⚠️ Password already used")
            return

    save_password(website, encrypted)

    result_label.config(text=f"✅ Saved")

def decrypt():
    password = password_entry.get()

    if password.strip() == "":
        result_label.config(text="❌ Enter encrypted password")
        return

    decrypted = decrypt_password(password)

    result_label.config(text=f"🔓 Decrypted: {decrypted}")

   

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



def view_all():
    saved = read_passwords()

    if not saved:
        result_label.config(text="No saved passwords")
        return

    text = ""
    for website, password in saved:
        text += f"{website}: {password}\n"

    result_label.config(text=text)

# buttons
tk.Button(root, text="Encrypt", command=encrypt).pack(pady=5)
tk.Button(root, text="Decrypt", command=decrypt).pack(pady=5)
tk.Button(root, text="View Saved", command=view_all).pack(pady=5)


# result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()