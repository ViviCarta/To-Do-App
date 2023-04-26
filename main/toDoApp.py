"""Author: Venise Saron
Professor: Corey Seliger
Subject: SDEV140
Last Revised: 4-26-2023
Purpose: This program is a GUI
application of a simple To-Do List
using Tkinter."""

from tkinter import *

root = Tk()
root.geometry("1050x750")
root.title("Private To-Do's")

# Set the header and subhead of the application
header_label = Label(root, text="To-Do List", font=("Arial", 35))
header_label.pack(padx=10, pady=(40, 10))

subhead_label = Label(root, text="Start your day productively.", font=("Arial", 14))
subhead_label.pack()

# Add the input frame
frame1 = Frame(root, width=750, height=280, bd=1, relief="solid", bg="white")
frame1.pack(pady=40)

root.mainloop()
