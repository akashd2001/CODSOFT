import tkinter as tk
import random
import string
from tkinter import messagebox

def generate_password():
    length = int(password_length.get())
    
    
    characters = string.ascii_letters + string.digits + string.punctuation
    
    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    
    generated_password.delete(0, tk.END)
    generated_password.insert(0, password)

def reset_entries():
    generated_password.delete(0, tk.END)

def accept_entries():
    username.delete(0, tk.END)
    password_length.delete(0, tk.END)
    generated_password.delete(0, tk.END)
    messagebox.showinfo("Accepted", "Password Accepted!")


root = tk.Tk()
root.title("Password Generator")

header = tk.Label(root, text="Password Generator", font=("Times New Roman", 30, "italic", "bold",))
header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

#
username_label = tk.Label(root, text="Username:", font=("Times New Roman", 15,"bold"))
username_label.grid(row=1, column=0, padx=10, pady=10)

username = tk.Entry(root)
username.grid(row=1, column=1, padx=10, pady=10)

password_length_label = tk.Label(root, text="Password Length:", font=("Times New Roman", 15,"bold"))
password_length_label.grid(row=2, column=0, padx=10, pady=10)

password_length = tk.Entry(root)
password_length.grid(row=2, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="green", fg="white")
generate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

generated_password_label = tk.Label(root, text="Generated Password:", font=("Times New Roman", 15,"bold"))
generated_password_label.grid(row=4, column=0, padx=10, pady=10)

generated_password = tk.Entry(root)
generated_password.grid(row=4, column=1, padx=10, pady=10)

accept_button = tk.Button(root, text="ACCEPT", bg="orange", fg="white", command=accept_entries)
accept_button.grid(row=5, column=0, padx=(5, 5), pady=10)

reset_button = tk.Button(root, text="RESET", bg="blue", fg="white", command=reset_entries)
reset_button.grid(row=5, column=1, padx=(5, 5), pady=10)


root.mainloop()
