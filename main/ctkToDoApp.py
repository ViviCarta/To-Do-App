"""Author: Venise Saron
Professor: Corey Seliger
Subject: SDEV140
Last Revised: 4-30-2023
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
        self.not_comp_list = []
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
        self.task_listbox_1 = Listbox(self.not_comp_frame, width=10, height=5,
                                      font=("Arial", 14), justify="center",
                                      selectbackground="gray", selectmode="single")

        # Pack the frame, label, and listbox
        self.not_comp_frame.pack()
        self.not_comp_label.pack(padx=(0, 600), pady=20)
        self.task_listbox_1.pack(fill="x")

        """Create a frame where after check button is clicked,
        tasks are placed in the completed category"""
        self.comp_frame = ctk.CTkFrame(self.scrollable_frame, fg_color="transparent")
        self.comp_label = ctk.CTkLabel(self.comp_frame, text="Completed",
                                       font=ctk.CTkFont("Arial", 18))
        self.task_listbox_2 = Listbox(self.comp_frame, width=10, height=5,
                                      font=("Arial", 14), justify="center",
                                      selectbackground="gray", selectmode="single")

        # Pack the frame, label, and listbox
        self.comp_frame.pack()
        self.comp_label.pack(padx=(0, 635), pady=20)
        self.task_listbox_2.pack(fill="x")

        """Create a frame that will hold
        all buttons but oriented side-by-side"""
        self.button_frame = ctk.CTkFrame(self, width=100, fg_color="transparent")
        self.button_frame.pack()

        """Add a functional button for adding tasks"""
        self.add_button = ctk.CTkButton(self.button_frame, text="Add Task", width=100,
                                        font=ctk.CTkFont("Arial", size=14, weight="bold"),
                                        command=self.add_task)
        self.add_button.pack(side="left", padx=10)

        """Add a functional button that when
        clicked, will move selected task to 
        completed category"""
        self.check_button = ctk.CTkButton(self.button_frame, text="✅", command=self.check, width=10)
        self.check_button.pack(side="left")

        """Add a functional button that when 
        clicked, will delete selected task"""
        self.delete_button = ctk.CTkButton(self.button_frame, text="🗑", command=self.delete, width=10)
        self.delete_button.pack(side="left", padx=10)

        """Define commands"""

    def add_task(self):
        """This command takes initial task input
        and contains it within the not completed
        category"""
        task = self.user_entry.get()
        self.user_entry.delete(0, ctk.END)

        self.not_comp_list.append(task)
        self.task_listbox_1.insert(END, task)

    def check(self):
        """This command removes the selected task
        from the not completed category and moves
        it under the completed category"""
        task = str(self.task_listbox_1.get(ANCHOR))
        if task:
            self.comp_list.append(task)
            self.task_listbox_2.insert(END, task)
            self.task_listbox_1.delete(ANCHOR)

    def delete(self):
        """This command permanently deletes
        the selected task regardless of
        category"""
        task_1 = str(self.task_listbox_1.get(ANCHOR))
        task_2 = str(self.task_listbox_2.get(ANCHOR))
        if task_1 in self.not_comp_list or task_2 in self.comp_list:
            self.task_listbox_1.delete(ANCHOR)
            self.task_listbox_2.delete(ANCHOR)


if __name__ == "__main__":
    app = App()
    app.mainloop()
