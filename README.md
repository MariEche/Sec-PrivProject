# SecretStorage - Password Manager Tool

## Group Members
Athraa Toma  
Haadia Siddiqui  
Maria Echeverri Solis  

---

## Project Description
This project is a simple password manager made using Python. It allows users to store, encrypt, and view their passwords using a graphical interface.

---

## Features
- Encrypt passwords before saving  
- Decrypt passwords  
- Store passwords in a text file  
- Check for empty inputs and minimum password length  
- Prevent duplicate passwords  
- View all saved passwords  

---

## Technologies Used
- Python  
- Tkinter (for the user interface)  
- Text file for storage  

---

## How It Works
The user enters a website and password in the interface.  
The password is encrypted and saved in a file called passwords.txt.  
The user can view saved passwords or decrypt them when needed.  

---

## Project Files
- ui.py – handles the user interface  
- encrypt.py – contains encryption and decryption logic  
- storage.py – saves and reads passwords from file  
- main.py – connects the program together  
- passwords.txt – stores encrypted passwords  
- userauth.py – handles login with a master password  

---

## How to Run
1. Install Python  
2. Install bcrypt:
   pip install bcrypt  
3. Run the program:
   python ui.py  

---

## Limitations
- The encryption used is basic  
- Passwords are stored in a text file  
- Not secure for real-world use  

---

## Conclusion
This project helped us learn how to use encryption, file handling, and build a user interface in Python while working as a team.
