import tkinter as tk
from tkinter import messagebox
import random
import string
import re
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk, ImageSequence

# Function to generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

# Function to check password strength
def check_password_strength(password):
    # Rule 1: Check if the password length is at least 12 characters
    if len(password) < 12:
        return 'weak'
    
    # Rule 2: Check for at least one uppercase letter, one lowercase letter, one digit, and one special character
    if not re.search(r'[a-z]', password):  # check for lowercase
        return 'weak'
    if not re.search(r'[A-Z]', password):  # check for uppercase
        return 'weak'
    if not re.search(r'\d', password):  # check for numbers
        return 'weak'
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):  # check for special characters
        return 'weak'
    
    # Rule 3: Ensure the password doesn't contain common dictionary words (check for some examples)
    common_words = ["password", "123456", "qwerty", "letmein", "welcome", "admin"]
    if any(word in password.lower() for word in common_words):
        return 'weak'
    
    # Rule 4: Ensure the password doesn't use personal information (e.g., user’s name, birthday, etc.)
    # Assuming the username is passed or known. You can implement additional logic to check for that.
    # For now, let's just check against an example name "john". You can customize this check as needed.
    if "john" in password.lower():  # Replace with user-specific check if needed
        return 'weak'
    
    # Rule 5: Check if the password contains repeated or sequential characters (e.g., "aaaa" or "1234")
    if re.search(r'(.)\1{3,}', password):  # Repeated characters (e.g., "aaaa")
        return 'weak'
    if re.search(r'0123|abcd|qwerty', password.lower()):  # Sequential characters
        return 'weak'
    
    # If the password passes all checks, it is considered strong
    return 'strong'

# Function to update the progress bar and show the strength
def update_strength(password):
    strength = check_password_strength(password)
    progress['value'] = 0
    if strength == 'weak':
        progress['value'] = 33
        strength_label.config(text="Weak Password", fg="#e74c3c")  # Red color for weak
        play_gif("weak.gif")  # Weak gif
    elif strength == 'medium':
        progress['value'] = 66
        strength_label.config(text="Medium Password", fg="#f39c12")  # Yellow color for medium
        play_gif("loading.gif")  # Loading gif
    else:
        progress['value'] = 100
        strength_label.config(text="Strong Password", fg="#2ecc71")  # Green color for strong
        play_gif("strong.gif")  # Strong gif

# Function to display the gif based on the password strength
def play_gif(gif_path):
    try:
        gif = Image.open(gif_path)
        frames = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(gif)]
        label_gif.config(image=frames[0])
        label_gif.image = frames[0]

        # Create a function to loop through frames of GIF
        def update_gif(frame_num=0):
            frame = frames[frame_num]
            label_gif.config(image=frame)
            label_gif.image = frame
            frame_num = (frame_num + 1) % len(frames)
            root.after(100, update_gif, frame_num)

        update_gif()
    except Exception as e:
        print(f"Error loading GIF: {e}")

# Function to generate password and update the entry field
def generate():
    password = generate_password()
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    update_strength(password)

# Function to handle manual password entry
def check_manual_password():
    password = password_entry.get()
    if password:  # Only check if there is a password
        update_strength(password)
    else:
        messagebox.showwarning("Input Error", "Please enter a password.")

# Setting up the main Tkinter window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x700")
root.config(bg="#ecf0f1")  # Light grey background

# Title Label (with more styling)
title_label = tk.Label(root, text="Password Strength Checker", font=("Helvetica", 18, 'bold'), bg="#ecf0f1", fg="#34495e")
title_label.pack(pady=20)

# Password Label and Entry (with padding and font size adjustments)
password_label = tk.Label(root, text="Enter Password:", font=("Helvetica", 12), bg="#ecf0f1", fg="#34495e")
password_label.pack()

password_entry = tk.Entry(root, width=40, font=("Helvetica", 12), bd=2, relief="solid")
password_entry.pack(pady=10)  # Apply padding through pack() instead

# Buttons for manual password check and generating a password (with styles)
manual_check_button = tk.Button(root, text="Check Password", command=check_manual_password, width=20, bg="#2980b9", fg="white", font=("Helvetica", 12), relief="raised", bd=2)
manual_check_button.pack(pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate, width=20, bg="#16a085", fg="white", font=("Helvetica", 12), relief="raised", bd=2)
generate_button.pack(pady=10)

# Progress Bar (with styling)
progress = Progressbar(root, orient="horizontal", length=300, mode="determinate", style="TProgressbar")
progress.pack(pady=20)

# Strength Label (with custom font)
strength_label = tk.Label(root, text="Password Strength", font=("Helvetica", 14), bg="#ecf0f1", fg="#34495e")
strength_label.pack(pady=10)

# Gif Label (to display gifs)
label_gif = tk.Label(root)
label_gif.pack(pady=20)

# Password Tips (Display the tips or rules for a strong password)
password_tips = """
Tips for a Strong Password:

1. Use at least 12 characters.
2. Include uppercase and lowercase letters.
3. Use numbers (0-9) and special characters (e.g., !@#).
4. Avoid common words like 'password', '123456', etc.
5. Avoid personal information (e.g., names, birthdays).
6. Don't use repetitive or sequential characters (e.g., 'aaaa', '1234').

A strong password helps protect your accounts!
"""
tips_label = tk.Label(root, text=password_tips, font=("Helvetica", 10), bg="#ecf0f1", fg="#34495e", anchor="w", justify="left")
tips_label.pack(pady=20, padx=20)

# Running the app
root.mainloop()
