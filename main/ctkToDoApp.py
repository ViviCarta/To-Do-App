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
        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=750, height=300, corner_radius=10,
                                                       fg_color="white", scrollbar_fg_color="white")
        self.scrollable_frame.pack(pady=20)

        """Create an entry widget within scrollable frame"""
        self.user_entry = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Input task name here...",
                                       corner_radius=10, font=ctk.CTkFont("Arial", 16))
        self.user_entry.pack(fill="x")

        """Create a frame where initial tasks are sent
        to the not complete category"""
        self.not_comp_frame = ctk.CTkFrame(self.scrollable_frame, fg_color="transparent")
        self.not_comp_label = ctk.CTkLabel(self.not_comp_frame, text="Not Completed",
                                           font=ctk.CTkFont("Arial", 18))

        # Pack the frame and label
        self.not_comp_frame.pack(padx=(0, 600), pady=20)
        self.not_comp_label.pack()

        """Add a functional button for adding tasks"""
        self.add_button = ctk.CTkButton(self, text="Add Task", width=100,
                                        font=ctk.CTkFont("Arial", size=14, weight="bold"),
                                        command=self.add_task)
        self.add_button.pack(pady=20)

        """Define commands"""
    def add_task(self):
        task = self.user_entry.get()
        task_label = ctk.CTkLabel(self.scrollable_frame, text=task)
        task_label.pack(side="left")
        self.user_entry.delete(0, ctk.END)


if __name__ == "__main__":
    app = App()
    app.mainloop()
