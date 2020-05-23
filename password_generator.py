import random
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo

win = tk.Tk()
win.title("Password Generator")

def generator():
    string = entry.get()
    length = int(entry2.get())
    password = " "
    for i in range(0, length):
        password += random.choice(string)
    showinfo("Generated Passwords ","Your Password : {0}".format(password))

label = tk.Label(win, text = "Enter the string: ")
label.grid(row = 0, column = 0, padx = 8, pady = 8)

entry = tk.Entry(win)
entry.grid(row = 0, column = 1, padx = 8)

label1 = tk.Label(win, text = 'Enter Length: ')
label1.grid(row = 1, column = 0, padx = 8, pady = 8)

entry2 = tk.Entry(win)
entry2.grid(row = 1, column = 1, padx = 8)

button = ttk.Button(win, text = "Generate", command = generator)
button.grid(row = 2, column = 0, columnspan = 2, padx = 8)

win.mainloop()
