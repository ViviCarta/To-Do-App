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
frame1 = Frame(root, width=750, height=280, bg="white")
frame1.pack(pady=40)

list_box = Listbox(frame1, width=100, height=16, font=("Arial", 14),
                   fg="black", bd=1, relief="solid", cursor="mouse")
list_box.pack(side="left", fill="both", expand=FALSE)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side="right", fill="both")

list_box.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=list_box.yview)

# Add a functional add button
add_button = Button(root, text="add task", width=50)
add_button.pack(pady=20)

root.mainloop()
