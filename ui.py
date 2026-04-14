from storage import save_password, read_passwords
from encrypt import encrypt_password, decrypt_password
import tkinter as tk
from tkinter import messagebox, simpledialog
import sys
from userauth import check_master_password

def ask_user_password():
    password = simpledialog.askstring("Master Password", "Enter your master password:", show='*')
    if check_master_password(password):
        return True
    else:
        messagebox.showerror("Access Denied", "Incorrect master password. Exiting.")
        return False

def encrypt():
    website = website_entry.get()
    password = password_entry.get()

    if website.strip() == "" or password.strip() == "":
        result_label.config(text="❌ Fill all fields")
        return

    if len(password) < 6:
        result_label.config(text="❌ Password too short (Reccommended: 6+ characters)")
        return

    encrypted = encrypt_password(password)

    saved = read_passwords()
    for w, p in saved:
        if encrypted == p:
            result_label.config(text="⚠️ Password already used")
            return
        
    for w, p in saved:
        if website.lower() == w.lower():
            result_label.config(text="⚠️ Password for this website already exists")
            return

    save_password(website, encrypted)

    result_label.config(text=f"✅ Saved")

def decrypt():
    password = password_entry.get()
    website = website_entry.get()

    if website.strip() == "" and password.strip() == "":
        result_label.config(text="❌ Fill at least one field")
        return
    
    if website.strip() != "":
        saved = read_passwords()
        for w, p in saved:
            if website.lower() == w.lower():
                decrypted = decrypt_password(p)
                result_label.config(text=f"🔓 Decrypted: {decrypted}")
                return
        result_label.config(text="❌ Website not found")
        return
    
    if password.strip() != "":
        decrypted = decrypt_password(password)
        result_label.config(text=f"🔓 Decrypted: {decrypted}")

   

# main window
root = tk.Tk()
root.withdraw()  # Hide the main window while asking for password

if ask_user_password():
    root.deiconify()  # Show the main window if password is correct
root.title("Password Tool")
root.geometry("1200x1000")

# labels + inputs

main_frame = tk.Frame(root)
main_frame.pack(expand=True) 
font_style = ("Arial", 30)


tk.Label(main_frame, text="Website", font=font_style).pack(pady=10)
website_entry = tk.Entry(main_frame, width=30, font=font_style)
website_entry.pack(pady=5)

tk.Label(main_frame, text="Password", font=font_style).pack(pady=10)
password_entry = tk.Entry(main_frame, width=30, font=font_style)
password_entry.pack(pady=5)



def view_all():
    saved = read_passwords()

    if not saved:
        result_label.config(text="No saved passwords")
        return

    text = ""
    for website, password in saved:
        text += f"{website}: {decrypt_password(password)}\n"

    result_label.config(text=text)

# buttons
tk.Button(main_frame, text="Encrypt", command=encrypt, width=20, font=font_style).pack(pady=10)
tk.Button(main_frame, text="Decrypt", command=decrypt, width=20, font=font_style).pack(pady=10)
tk.Button(main_frame, text="View Saved", command=view_all, width=20, font=font_style).pack(pady=10)


# result
result_label = tk.Label(main_frame, text="", font=font_style, wraplength=900, justify="center")
result_label.pack(pady=10)

root.mainloop()