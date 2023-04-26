"""Author: Venise Saron
Professor: Corey Seliger
Subject: SDEV140
Last Revised: 4-26-2023
Purpose: This program is a GUI
application of a simple To-Do List
using Tkinter."""

import tkinter as tk

root = tk.Tk()
root.geometry("1050x750")
root.title("Private To-Do's")

header_label = tk.Label(root, text="To-Do List", font=("Arial", 35))
header_label.pack(padx=10, pady=(40, 10))

subhead_label = tk.Label(root, text="Start your day productively.", font=("Arial", 14))
subhead_label.pack()

root.mainloop()