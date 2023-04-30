"""Author: Venise Saron
Professor: Corey Seliger
Subject: SDEV140
Last Revised: 4-26-2023
Purpose: This program is a GUI
application of a simple To-Do List
using Custom Tkinter."""

import customtkinter as ctk


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
        self.scrollable_frame = ctk.CTkScrollableFrame(master=self, width=750, height=300, fg_color="white",
                                                       scrollbar_fg_color="white")
        self.scrollable_frame.pack(pady=20)

        """Create an entry widget"""
        self.user_entry = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Input task name here...",
                                       corner_radius=0)
        self.user_entry.pack(fill="x")

        """Add a add_button"""
        self.add_button = ctk.CTkButton(self, text="add task", width=100,
                                        font=ctk.CTkFont("Arial", size=14, weight="bold"),
                                        command=self.add_task)
        self.add_button.pack(pady=20)

        """Define commands"""
    def add_task(self):
        task = self.user_entry.get()
        task_label = ctk.CTkLabel(self.scrollable_frame, text=task)
        task_label.pack()
        self.user_entry.delete(0, ctk.END)


if __name__ == "__main__":
    app = App()
    app.mainloop()
