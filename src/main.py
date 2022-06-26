# TKinter 
import tkinter as tk
from tkinter import filedialog, Text
import os


root = tk.Tk()
# Change the title from tk to OSiNT Toolkit
root.title("OSINT Toolkit")

canvas = tk.Canvas(width = 300, height = 150)
canvas.pack()

# Display text that says "Enter a username"
label = tk.Label(root, text = "Enter a username")
label.pack()
# Style the label to make it look modern
label.configure(font = ("Arial", 18))


# Create an input field that takes in input from the user
# and stores it in the variable 'input_field'
input_field = tk.Entry(root, width = 30)
input_field.pack()

if input_field == "":
    print("Please enter a username")
    exit()

# Create a button that opens terminal and runs the program
open_terminal_button = tk.Button(root, text = "Run Sherlock", command = lambda: os.system("python3 src/sherlock.py " + input_field.get()))
open_terminal_button.pack(anchor=tk.CENTER)

# Display text that says "Enter a domain to look up"
label1 = tk.Label(root, text = "Enter a domain to lookup")
label1.pack()
# Style the label using the font and size
label1.configure(font = ("Arial", 18), underline=True)

breached_dbs = tk.Button(root, text = "Look for breached Databases", command = lambda: os.system("python3 src/lookup/breached_dbs.py " + input_field.get()))
# Center the button
breached_dbs.pack()

# Display text that says "Enter a email too look up"
label2 = tk.Label(root, text = "Enter an email to lookup")
label2.pack()
label2.configure(font = ("Arial", 18), underline=True)

reverse_email_lookup = tk.Button(root, text = "Reverse Email Lookup", command = lambda: os.
system("python3 src/lookup/reverse_email_lookup.py")
)
reverse_email_lookup.pack()

# Check if variable has been clicked
if breached_dbs == True:
    # Run reverse_phone_lookup.py
    os.system("python3 src/lookup/breached_dbs.py " + input_field.get())

root.mainloop()