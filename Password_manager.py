import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import datetime

FILE_PATH = "passwords.json"

def save_password():
    site = site_entry.get()
    username = user_entry.get()
    password = pass_entry.get()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if not site or not username or not password:
        messagebox.showwarning("Warning", "All fields are required!")
        return
    
    data = {"site": site, "username": username, "password": password, "date": timestamp}
    
    passwords = load_passwords()
    passwords.append(data)
    
    with open(FILE_PATH, "w") as file:
        json.dump(passwords, file, indent=4)
    
    messagebox.showinfo("Success", "Password Saved Successfully!")
    site_entry.delete(0, tk.END)
    user_entry.delete(0, tk.END)
    pass_entry.delete(0, tk.END)

def load_passwords():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    return []

def show_passwords():
    passwords = load_passwords()
    
    if not passwords:
        messagebox.showinfo("Stored Passwords", "No passwords stored yet.")
        return
    
    password_window = tk.Toplevel(root)
    password_window.title("Stored Passwords")
    password_window.geometry("400x300")
    
    tk.Label(password_window, text="Stored Passwords", font=("Arial", 14, "bold")).pack(pady=5)
    text_area = tk.Text(password_window, height=10, width=50)
    text_area.pack(pady=5)
    
    for entry in passwords:
        text_area.insert(tk.END, f"Website: {entry['site']}\nUsername: {entry['username']}\nPassword: {entry['password']}\nSaved On: {entry['date']}\n\n")
    text_area.config(state=tk.DISABLED)
    
    clear_btn = tk.Button(password_window, text="Clear All", bg="red", fg="white", command=clear_passwords)
    clear_btn.pack(pady=5)

def clear_passwords():
    os.remove(FILE_PATH)
    messagebox.showinfo("Cleared", "All stored passwords have been deleted!")

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("Secure Password Manager")
root.geometry("350x250")

tk.Label(root, text="Secure Password Manager", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Website").pack()
site_entry = tk.Entry(root, width=30)
site_entry.pack()

tk.Label(root, text="Username").pack()
user_entry = tk.Entry(root, width=30)
user_entry.pack()

tk.Label(root, text="Password").pack()
pass_entry = tk.Entry(root, width=30, show="*")
pass_entry.pack()

save_btn = tk.Button(root, text="Save Password", command=save_password)
save_btn.pack(pady=5)

retrieve_btn = tk.Button(root, text="Retrieve Passwords", command=show_passwords)
retrieve_btn.pack()

exit_btn = tk.Button(root, text="Exit", bg="red", fg="white", command=exit_app)
exit_btn.pack(pady=5)

root.mainloop()

