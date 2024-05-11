#!/usr/bin/env python3

import random
import string
import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip

# Set default options
DEFAULT_LENGTH = 16
DEFAULT_UPPERCASE = True
DEFAULT_LOWERCASE = True
DEFAULT_DIGITS = True
DEFAULT_SPECIAL_CHARS = True

# Create main window
root = tk.Tk()
root.title("Random Password Generator")

# Define variables
length_var = tk.StringVar(value=str(DEFAULT_LENGTH))
uppercase_var = tk.BooleanVar(value=DEFAULT_UPPERCASE)
lowercase_var = tk.BooleanVar(value=DEFAULT_LOWERCASE)
digits_var = tk.BooleanVar(value=DEFAULT_DIGITS)
special_chars_var = tk.BooleanVar(value=DEFAULT_SPECIAL_CHARS)

# Function to generate password
def generate_password():
    length = int(length_var.get())
    options = (uppercase_var.get(), lowercase_var.get(), digits_var.get(), special_chars_var.get())
    characters = ''
    if options[0]:
        characters += string.ascii_uppercase
    if options[1]:
        characters += string.ascii_lowercase
    if options[2]:
        characters += string.digits
    if options[3]:
        characters += "!@#$%^&*()_+-=[]{}|;:,.<>?`~"
    
    if not characters:
        messagebox.showwarning("Error", "Please select at least one character type.")
        return
    
    password = ''.join(random.choice(characters) for _ in range(length))
    pyperclip.copy(password)
    messagebox.showinfo("Password Generated", "Password copied to clipboard:\n" + password)

# Function to reset options to default values
def reset_defaults():
    length_var.set(str(DEFAULT_LENGTH))
    uppercase_var.set(DEFAULT_UPPERCASE)
    lowercase_var.set(DEFAULT_LOWERCASE)
    digits_var.set(DEFAULT_DIGITS)
    special_chars_var.set(DEFAULT_SPECIAL_CHARS)

# Length label and entry
length_label = ttk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=5, pady=5)
length_entry = ttk.Entry(root, textvariable=length_var)
length_entry.grid(row=0, column=1, padx=5, pady=5)

# Options checkboxes
options_frame = ttk.Frame(root)
options_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
checkboxes = [("Uppercase", uppercase_var), ("Lowercase", lowercase_var),
              ("Digits", digits_var), ("Special Characters", special_chars_var)]
for i, (text, var) in enumerate(checkboxes):
    checkbox = ttk.Checkbutton(options_frame, text=text, variable=var)
    checkbox.grid(row=i//2, column=i%2, padx=5, pady=5, sticky="w")

# Generate password button
generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Reset to defaults button
reset_button = ttk.Button(root, text="Back to Defaults", command=reset_defaults)
reset_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Start the GUI event loop
root.mainloop()
