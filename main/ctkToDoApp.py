"""Author: Venise Saron
Professor: Corey Seliger
Subject: SDEV140
Last Revised: 4-26-2023
Purpose: This program is a GUI
application of a simple To-Do List
using Custom Tkinter."""

import customtkinter as ctk

root = ctk.CTk()
root.geometry("1050x750")
root.title("Private To-Do's")

first_header = ctk.CTkLabel(root, text="To-Do List", font=ctk.CTkFont("Arial", size=35))
first_header.pack(padx=10, pady=(40, 10))

second_header = ctk.CTkLabel(root, text="Start your day productively.", font=ctk.CTkFont("Arial", size=14))
second_header.pack(pady=(5, 10))

scrollable_frame = ctk.CTkScrollableFrame(root, width=750, height=280)
scrollable_frame.pack(pady=20)

add_button = ctk.CTkButton(root, text="add task", width=50)
add_button.pack(pady=20)

root.mainloop()
