"""Author: Venise Saron
Professor: Corey Seliger
Subject: SDEV140
Last Revised: 5-10-2023
Purpose: This program is a GUI
application of a simple To-Do List
using Custom Tkinter."""

from tkinter import *
import customtkinter as ctk
from PIL import ImageTk, Image

ctk.set_appearance_mode("light")


class ApplicationPage(ctk.CTk):
    """Displays the main application page."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.geometry("1000x750")
        self.resizable(False, False)
        self.title("Private To-Do's")

        """Display a background image
        for the main application window"""
        self.background_img = ImageTk.PhotoImage(Image.open("images/main.png"))
        self.background_label = Label(self, image=self.background_img, bg="white")
        self.background_label.pack()

        """Create a mainframe
        that will hold the rest
        of the widgets"""
        self.main_frame = ctk.CTkFrame(self.background_label, width=800, height=620,
                                       fg_color="white", bg_color="transparent")
        self.main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        """Create button that will
        go back to previous page"""
        self.back_button = ctk.CTkButton(self.main_frame, text="Logout", width=100, corner_radius=6,
                                         font=ctk.CTkFont("Arial", size=14), fg_color="black",
                                         hover_color="gray", text_color="white", command=self.return_login)
        self.back_button.place(x=70, y=40)

        # Create two empty lists
        self.not_comp_list = []
        self.comp_list = []

        """Add labels for main header 
        and a subhead"""
        self.heading = ctk.CTkLabel(self.main_frame, text="To-Do List", font=ctk.CTkFont("Arial", size=35))
        self.heading.place(x=320, y=80)

        self.subheading = ctk.CTkLabel(self.main_frame, text="Start your day productively.",
                                       font=ctk.CTkFont("Arial", size=14))
        self.subheading.place(x=320, y=130)

        """Create scrollable frame"""
        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=700, height=350, corner_radius=10,
                                                       fg_color="black", scrollbar_fg_color="black")
        self.scrollable_frame.place(x=140, y=250)

        """Create an entry widget 
        within scrollable frame"""
        self.user_entry = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Input task name here...",
                                       placeholder_text_color="black", corner_radius=10,
                                       font=ctk.CTkFont("Arial", size=15, slant="italic"),
                                       border_color="white")
        self.user_entry.pack(fill="x")

        """Create a frame where initial 
        tasks are placed inside the 
        not completed category"""
        self.not_comp_frame = ctk.CTkFrame(self.scrollable_frame, height=150,
                                           fg_color="white", corner_radius=0)
        self.not_comp_label = ctk.CTkLabel(self.not_comp_frame, text="Not Completed",
                                           text_color="black",
                                           font=ctk.CTkFont("Arial", size=18))
        self.task_listbox_1 = Listbox(self.not_comp_frame, width=80, height=5,
                                      font=("Arial", 14), justify="center",
                                      selectbackground="gray", selectmode="single")

        # Place the frame, label, and listbox
        self.not_comp_frame.pack(pady=10, fill="x")
        self.not_comp_label.place(x=20, y=10)
        self.task_listbox_1.place(x=30, y=50)

        """Create a frame where after 
        check button is clicked,
        tasks are placed in the 
        completed category"""
        self.comp_frame = ctk.CTkFrame(self.scrollable_frame, height=150,
                                       fg_color="white", corner_radius=0)
        self.comp_label = ctk.CTkLabel(self.comp_frame, text="Completed",
                                       text_color="black",
                                       font=ctk.CTkFont("Arial", 18))
        self.task_listbox_2 = Listbox(self.comp_frame, width=80, height=5,
                                      font=("Arial", 14), justify="center",
                                      selectbackground="gray", selectmode="single")

        # Pack the frame, label, and listbox
        self.comp_frame.pack(fill="x")
        self.comp_label.place(x=20, y=10)
        self.task_listbox_2.place(x=30, y=50)

        """Add a functional button for adding tasks"""
        self.add_button = ctk.CTkButton(self.main_frame, text="Add Task", width=100,
                                        corner_radius=6, font=ctk.CTkFont("Arial", size=14),
                                        fg_color="black", hover_color="gray",
                                        text_color="white", command=self.add_task)
        self.add_button.place(x=230, y=570)

        """Add a functional button that when
        clicked, will move selected task to
        completed category"""
        self.check_button = ctk.CTkButton(self.main_frame, text="Finished", width=100,
                                          corner_radius=6, font=ctk.CTkFont("Arial", size=14),
                                          fg_color="black", hover_color="gray",
                                          text_color="white", command=self.check)
        self.check_button.place(x=350, y=570)

        """Add a functional button that when
        clicked, will delete selected task"""
        self.delete_button = ctk.CTkButton(self.main_frame, text="Delete", width=100,
                                           corner_radius=6, font=ctk.CTkFont("Arial", size=14),
                                           fg_color="black", hover_color="gray",
                                           text_color="white", command=self.delete)
        self.delete_button.place(x=470, y=570)

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

    def return_login(self):
        ApplicationPage.destroy(self)


if __name__ == "__main__":
    app = ApplicationPage()
    app.mainloop()
