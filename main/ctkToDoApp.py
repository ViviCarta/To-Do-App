"""This is the main application window
that is linked to the login window"""

from tkinter import *
import customtkinter as ctk
from PIL import ImageTk, Image

ctk.set_appearance_mode("light")


class ApplicationPage(ctk.CTk):
    """Displays the main application page."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.geometry("1050x900")
        self.resizable(False, False)
        self.title("Private To-Do's")

        """Display a background image
        for the main application window"""
        self.background_img = ImageTk.PhotoImage(Image.open("images/main2.jpg"))
        self.background_label = Label(self, image=self.background_img, bg="white")
        self.background_label.pack()

        """Create a mainframe
        that will hold the rest
        of the widgets"""
        self.main_frame = ctk.CTkFrame(self.background_label, width=800, height=750,
                                       fg_color="white", bg_color="black", corner_radius=30)
        self.main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        """Create button that will
        go back to previous page"""
        self.back_button = ctk.CTkButton(self.main_frame, text="Logout", width=110, corner_radius=6,
                                         font=ctk.CTkFont("Arial", size=16), fg_color="black",
                                         hover_color="gray", text_color="white", command=self.return_login)
        self.back_button.place(x=40, y=40)

        # Create two empty lists
        self.not_comp_list = []
        self.comp_list = []

        """Add labels for main header 
        and a subhead"""
        self.heading = ctk.CTkLabel(self.main_frame, text="To-Do List", font=ctk.CTkFont("Arial", size=40))
        self.heading.place(x=310, y=75)

        self.subheading = ctk.CTkLabel(self.main_frame, text="Start your day productively.",
                                       font=ctk.CTkFont("Arial", size=16))
        self.subheading.place(x=310, y=130)

        """Create scrollable frame"""
        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=700, height=500, corner_radius=10,
                                                       fg_color="black", scrollbar_fg_color="black")
        self.scrollable_frame.place(x=160, y=250)

        """Create an entry widget
        within scrollable frame"""
        self.user_entry = ctk.CTkEntry(self.scrollable_frame, placeholder_text="Input task name here...",
                                       placeholder_text_color="black", corner_radius=10,
                                       font=ctk.CTkFont("Arial", size=18, slant="italic"),
                                       border_color="white", height=40)
        self.user_entry.pack(fill="x")

        """Create a frame where initial
        tasks are placed inside the
        not completed category"""
        self.not_comp_frame = ctk.CTkFrame(self.scrollable_frame, height=210,
                                           fg_color="white", corner_radius=10)
        self.not_comp_label = ctk.CTkLabel(self.not_comp_frame, text="Not Completed",
                                           text_color="black",
                                           font=ctk.CTkFont("Times New Roman", size=20, weight="bold"))
        self.task_listbox_1 = Listbox(self.not_comp_frame, width=71, height=6,
                                      font=("Arial", 16), justify="center",
                                      selectbackground="gray", selectmode="single")

        # Place the frame, label, and listbox
        self.not_comp_frame.pack(pady=10, fill="x")
        self.not_comp_label.place(x=30, y=10)
        self.task_listbox_1.place(x=30, y=50)

        """Create a frame where after
        check button is clicked,
        tasks are placed in the
        completed category"""
        self.comp_frame = ctk.CTkFrame(self.scrollable_frame, height=210,
                                       fg_color="white", corner_radius=10)
        self.comp_label = ctk.CTkLabel(self.comp_frame, text="Completed",
                                       text_color="black",
                                       font=ctk.CTkFont("Times New Roman", size=20, weight="bold"))
        self.task_listbox_2 = Listbox(self.comp_frame, width=71, height=6,
                                      font=("Arial", 16), justify="center",
                                      selectbackground="gray", selectmode="single")

        # Pack the frame, label, and listbox
        self.comp_frame.pack(pady=10, fill="x")
        self.comp_label.place(x=30, y=10)
        self.task_listbox_2.place(x=30, y=50)

        """Add a functional button for adding tasks"""
        self.add_button = ctk.CTkButton(self.scrollable_frame, text="Add Task", width=120,
                                        corner_radius=6, font=ctk.CTkFont("Arial", size=16),
                                        fg_color="black", hover_color="gray", bg_color="white",
                                        text_color="white", command=self.add_task)
        self.add_button.place(x=570, y=6)

        """Add a functional button that when
        clicked, will move selected task to
        completed category"""
        self.comp_button = ctk.CTkButton(self.not_comp_frame, text="Finished", width=100,
                                         corner_radius=6, font=ctk.CTkFont("Arial", size=16),
                                         fg_color="black", hover_color="gray",
                                         text_color="white", command=self.complete)
        self.comp_button.place(x=230, y=175)

        """Add a functional button that when
        clicked, will move selected task to
        not completed category"""
        self.not_comp_button = ctk.CTkButton(self.comp_frame, text="Unfinished", width=100,
                                             corner_radius=6, font=ctk.CTkFont("Arial", size=16),
                                             fg_color="black", hover_color="gray",
                                             text_color="white", command=self.not_complete)
        self.not_comp_button.place(x=230, y=175)

        """Add a functional button that when
        clicked, will delete selected task in 
        not completed category"""
        self.del_not_comp_button = ctk.CTkButton(self.not_comp_frame, text="Delete", width=100,
                                                 corner_radius=6, font=ctk.CTkFont("Arial", size=16),
                                                 fg_color="black", hover_color="gray",
                                                 text_color="white", command=self.delete_not_comp)
        self.del_not_comp_button.place(x=370, y=175)

        """Add a functional button that when
        clicked, will delete selected task in 
        completed category"""
        self.del_comp_button = ctk.CTkButton(self.comp_frame, text="Delete", width=100,
                                             corner_radius=6, font=ctk.CTkFont("Arial", size=16),
                                             fg_color="black", hover_color="gray",
                                             text_color="white", command=self.delete_comp)
        self.del_comp_button.place(x=370, y=175)

        """Define commands"""

    def add_task(self):
        """This command takes initial task input
        and contains it within the not completed
        category"""
        task = self.user_entry.get()
        self.user_entry.delete(0, ctk.END)

        self.not_comp_list.append(task)
        self.task_listbox_1.insert(END, task)

    def not_complete(self):
        """This command removes the selected task
        from the completed category and moves
        it under the not completed category"""
        task = str(self.task_listbox_2.get(ANCHOR))

        if task:
            self.not_comp_list.append(task)
            self.task_listbox_1.insert(END, task)
            self.task_listbox_2.delete(ANCHOR)

    def complete(self):
        """This command removes the selected task
        from the not completed category and moves
        it under the completed category"""
        task = str(self.task_listbox_1.get(ANCHOR))

        if task:
            self.comp_list.append(task)
            self.task_listbox_2.insert(END, task)
            self.task_listbox_1.delete(ANCHOR)

    def delete_not_comp(self):
        """This command permanently deletes
        the selected task inside the not completed
        category"""
        task_1 = str(self.task_listbox_1.get(ANCHOR))

        if task_1 in self.not_comp_list:
            self.task_listbox_1.delete(ANCHOR)

    def delete_comp(self):
        """This command permanently deletes
        the selected task inside the completed
        category"""
        task_2 = str(self.task_listbox_2.get(ANCHOR))

        if task_2 in self.comp_list:
            self.task_listbox_2.delete(ANCHOR)

    def return_login(self):
        ApplicationPage.destroy(self)


if __name__ == "__main__":
    app = ApplicationPage()
    app.mainloop()

"""Will be making a separate module that will
combine all windows; as well as change the linked
windows into toplevel subclasses"""