from encrypt import encrypt_password, decrypt_password
from storage import save_password, read_passwords, search_password
from userauth import check_master_password
import tkinter as tk
from tkinter import messagebox, simpledialog
import sys

def ask_user_password():
    password = simpledialog.askstring("Master Password", "Enter master password:", show='*')
    if check_master_password(password):
        return True
    else:
        messagebox.showerror("Authentication Failed", "Incorrect master password.")
        return False

def encrypt():

    website = website_entry.get()
    password = password_entry.get()
    #key = key_entry.get()

    if not website or not password:
        messagebox.showerror("Input Error", "Website and password cannot be empty.")
        return

    encrypted = encrypt_password(password)
    save_password(website, encrypted)
    result_label.config(text=f"Encrypted: {encrypted}")

def decrypt():
    #encrypted_text = password_entry.get()
    #key = key_entry.get()
    website = website_entry.get().strip()

    if not website:
        messagebox.showerror("Input Error", "Website cannot be empty.")
        return

    #decrypted = decrypt_password(encrypted_text, key)

    #result_label.config(text=f"Decrypted: {decrypted}")

    encrypted_password = search_password(website)
    if encrypted_password is None:
        messagebox.showinfo("Not Found", "No password found for the given website.")
        return
    decrypted_password = decrypt_password(encrypted_password)
    result_label.config(text=f"Decrypted: {decrypted_password}")

def view_all_passwords():
    saved_passwords = read_passwords()
    if not saved_passwords:
        messagebox.showinfo("Passwords:", "No passwords saved.")
        return
        
    passwords_text = ""
    for website, encrypted in saved_passwords:
        decrypted = decrypt_password(encrypted)
        passwords_text += f"{website}: {decrypted}\n"

    top = tk.Toplevel(root)
    top.title("Saved Passwords")
    text_widget = tk.Text(top, wrap='word')
    text_widget.pack(expand=True, fill='both')
    text_widget.insert('1.0', passwords_text)
    text_widget.config(state='disabled')

def find_password():
    website = simpledialog.askstring("Search Password", "Enter website to search:")
    if not website:
        messagebox.showerror("Input Error", "Website cannot be empty.")
        return

    encrypted_password = search_password(website.strip())
    if encrypted_password is None:
        messagebox.showinfo("Not Found", "No password found for the given website.")
        return
    try:
        decrypted_password = decrypt_password(encrypted_password)
        messagebox.showinfo("Password Found", f"Website: {website}\nPassword: {decrypted_password}")
    except Exception as e:
        messagebox.showerror("Decryption Error", f"Error occurred while decrypting password for {website}: {e}")

# main window
root = tk.Tk()
root.withdraw()  # Hide the main window until authentication is successful

if ask_user_password():
    root.deiconify()  # Show the main window after successful authentication
    root.title("Password Tool")
    root.geometry("300x250")

    # labels + inputs
    tk.Label(root, text="Website").pack()
    website_entry = tk.Entry(root)
    website_entry.pack()

    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root)
    password_entry.pack()

    #tk.Label(root, text="Key").pack()
    #key_entry = tk.Entry(root)
    #key_entry.pack()

    # buttons
    tk.Button(root, text="Encrypt", command=encrypt).pack(pady=5)
    tk.Button(root, text="Decrypt", command=decrypt).pack(pady=5)

    tk.Button(root, text="View All Passwords", command=view_all_passwords).pack(pady=5)
    tk.Button(root, text="Find Password", command=find_password).pack(pady=5)

    # result
    result_label = tk.Label(root, text="")
    result_label.pack(pady=10)

    root.mainloop()