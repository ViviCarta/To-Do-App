"""Author: Venise Saron
Professor: Corey Seliger
Subject: SDEV140
Last Revised: 4-26-2023
Purpose: This program is a GUI
application of a simple To-Do List
using Custom Tkinter."""

import customtkinter as ctk


class ListFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame...
        # self.label = ctk.CTkLabel(self)
        # self.label.grid(row=0, column=0, padx=20)


class App(ctk.CTk):
    """Displays the parent window."""

    def __init__(self):
        super().__init__()
        self.geometry("1050x750")
        self.title("Private To-Do's")

        """Add labels for main header and a subhead"""
        self.heading = ctk.CTkLabel(self, text="To-Do List", font=ctk.CTkFont("Arial", size=35))
        self.heading.pack(padx=10, pady=(40, 10))

        self.subheading = ctk.CTkLabel(self, text="Start your day productively.",
                                       font=ctk.CTkFont("Arial", size=14))
        self.subheading.pack(pady=(5, 10))

        """Create scrollable frame"""
        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=750, height=280)
        self.scrollable_frame.pack(pady=20)

        """Add a add_button"""
        self.add_button = ctk.CTkButton(self, text="add task", width=50)
        self.add_button.pack(pady=20)


app = App()
app.mainloop()