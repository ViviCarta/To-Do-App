"""Author: Venise Saron
Professor: Corey Seliger
Subject: SDEV140
Last Revised: 4-26-2023
Purpose: This program is a GUI
application of a simple To-Do List
using Custom Tkinter."""

from tkinter import *
import customtkinter as ctk


class App(ctk.CTk):
    """Displays the parent window."""

    def __init__(self):
        super().__init__()
        self.geometry("1050x750")
        self.title("Private To-Do's")

        # Create two empty lists
        self.task_list = []
        self.comp_list = []

        """Add labels for main header and a subhead"""
        self.heading = ctk.CTkLabel(self, text="To-Do List", font=ctk.CTkFont("Arial", size=35))
        self.heading.pack(padx=10, pady=(40, 10))

        self.subheading = ctk.CTkLabel(self, text="Start your day productively.",
                                       font=ctk.CTkFont("Arial", size=14))
        self.subheading.pack(pady=(5, 10))

        """Create scrollable frame"""
        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=750, height=350, corner_radius=10,
                                                       fg_color="white", scrollbar_fg_color="white")
        self.scrollable_frame.pack(pady=20)

        """Create an entry widget within scrollable frame"""
        self.user_entry = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Input task name here...",
                                       corner_radius=10, font=ctk.CTkFont("Arial", 16))
        self.user_entry.pack(fill="x")

        """Create a frame where initial tasks are placed
        inside the not completed category"""
        self.not_comp_frame = ctk.CTkFrame(self.scrollable_frame, fg_color="transparent")
        self.not_comp_label = ctk.CTkLabel(self.not_comp_frame, text="Not Completed",
                                           font=ctk.CTkFont("Arial", 18))
        self.task_listbox_1 = Listbox(self.not_comp_frame, width=10, height=5, font=("Arial", 14),
                                      selectbackground="gray", selectmode="single")

        # Pack the frame and label
        self.not_comp_frame.pack()
        self.not_comp_label.pack(padx=(0, 600), pady=20)
        self.task_listbox_1.pack(fill="x")

        """Create a frame where after check button is clicked,
        tasks are placed in the completed category"""
        self.comp_frame = ctk.CTkFrame(self.scrollable_frame, fg_color="transparent")
        self.comp_label = ctk.CTkLabel(self.comp_frame, text="Completed",
                                       font=ctk.CTkFont("Arial", 18))
        self.task_listbox_2 = Listbox(self.comp_frame, width=10, height=5, font=("Arial", 14),
                                      selectbackground="gray", selectmode="single")

        # Pack the frame and label
        self.comp_frame.pack()
        self.comp_label.pack(padx=(0, 635), pady=20)
        self.task_listbox_2.pack(fill="x")

        """Add a functional button for adding tasks"""
        self.add_button = ctk.CTkButton(self, text="Add Task", width=100,
                                        font=ctk.CTkFont("Arial", size=14, weight="bold"),
                                        command=self.add_task)
        self.add_button.pack(pady=20)

        """Add a functional button that when
        clicked, will move selected task to completed
        category"""
        self.check_button = ctk.CTkButton(self, text="✅", command=self.check, width=10)
        self.check_button.pack()

        """Define commands"""

    def add_task(self):
        """This command takes initial task input
        and contains it within the not completed
        category"""
        task = self.user_entry.get()
        self.user_entry.delete(0, ctk.END)

        self.task_list.append(task)
        self.task_listbox_1.insert(END, task)

    def check(self):
        """This command removes the selected task
        and moves it under the completed category"""
        task = str(self.task_listbox_1.get(ANCHOR))
        if task in self.task_list:
            self.comp_list.append(task)
            self.task_listbox_2.insert(END, task)
            self.task_listbox_1.delete(ANCHOR)


if __name__ == "__main__":
    app = App()
    app.mainloop()
