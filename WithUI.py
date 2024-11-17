import tkinter as tk
from tkinter import messagebox

def check_number():
    try:
        number = int(entry.get())  # Get input from the user
        if number % 2 == 0:
            result = "The number is even."
        else:
            result = "The number is odd."
        messagebox.showinfo("Result", result)  # Show result in a popup
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")  # Handle invalid input

root = tk.Tk()
root.title("Even or Odd Checker")

label = tk.Label(root, text="Enter a number:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12), width=15)
entry.pack(pady=5)

button = tk.Button(root, text="Check", font=("Arial", 12), command=check_number)
button.pack(pady=10)

root.mainloop()
