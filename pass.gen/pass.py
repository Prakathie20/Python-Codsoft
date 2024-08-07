import random
import tkinter as tk

def generate_password():
    password_length = 8  # Length of the password
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_label.config(text=password)

window = tk.Tk()

generate_button = tk.Button(window, text="Click here,,!! To Generate Password", command=generate_password)
generate_button.pack()

password_label = tk.Label(window, text="")
password_label.pack()

window.mainloop()