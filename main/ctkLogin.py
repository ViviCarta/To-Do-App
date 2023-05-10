"""This is the login window
for the main application"""
import tkinter
from tkinter import *
import customtkinter as ctk
from PIL import ImageTk, Image


class ApplicationPage(tkinter.Toplevel):
    """Displays the main application page."""
    def __init__(self, master):
        super().__init__(master)

        self.geometry("1050x750")
        self.resizable(False, False)
        self.title("Private To-Do's")

        """Create button that will
        go back to previous page"""
        self.back_button = ctk.CTkButton(self, text="Back", font=ctk.CTkFont("Arial", size=14))
        self.back_button.pack(padx=(0, 650), pady=(20, 0))

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


class Login(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.geometry("1000x750")
        self.resizable(False, False)
        self.title("Login")

        """Display a background image
        for the login window"""
        self.background_img = ImageTk.PhotoImage(Image.open("images/login.png"))
        self.background_label = Label(self, image=self.background_img, bg="white")
        self.background_label.pack()

        """Create a border frame for 
        label and entry widgets"""
        self.border_frame = ctk.CTkFrame(self.background_label, width=400, height=450,
                                         fg_color="white")
        self.border_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        """Add main header and 
        subhead for login page"""
        self.login_heading = ctk.CTkLabel(self.border_frame, text="Login",
                                          font=ctk.CTkFont("Arial", size=40),
                                          text_color="black")
        self.login_heading.place(x=150, y=40)

        self.login_subheading = ctk.CTkLabel(self.border_frame, text="Sign in to continue.",
                                             font=ctk.CTkFont("Arial", size=14),
                                             text_color="black")
        self.login_subheading.place(x=140, y=95)

        # Create entry widgets
        self.username_entry = ctk.CTkEntry(self.border_frame, width=240, height=35, fg_color="black",
                                           placeholder_text="Username", placeholder_text_color="white",
                                           font=ctk.CTkFont("Arial", size=14), text_color="white",
                                           border_color="gray")
        self.username_entry.place(x=80, y=150)

        self.password_entry = ctk.CTkEntry(self.border_frame, width=240, height=35, fg_color="black",
                                           placeholder_text="Password", placeholder_text_color="white",
                                           font=ctk.CTkFont("Arial", size=14), text_color="white",
                                           border_color="gray", show="•")
        self.password_entry.place(x=80, y=200)

        """Create a show/hide button
        for password_entry"""
        hide_image = ctk.CTkImage(Image.open("images/hide.png").resize((32, 32)))
        self.hide_button = ctk.CTkButton(self, image=hide_image, text="", width=10,
                                         anchor="center", fg_color="transparent", bg_color="black",
                                         hover=False, command=self.show)
        self.hide_button.place(x=570, y=353)

        """Create a login button"""
        self.login_button = ctk.CTkButton(self.border_frame, width=140, text="Login", corner_radius=6,
                                          font=ctk.CTkFont("Arial", size=14), fg_color="black",
                                          hover_color="gray", text_color="white", command=self.login)
        self.login_button.place(x=130, y=255)

        """Add subhead for create
        new account"""
        self.create_subheading = ctk.CTkLabel(self.border_frame, text="Don't have an account?",
                                              font=ctk.CTkFont("Arial", size=14),
                                              text_color="black")
        self.create_subheading.place(x=130, y=330)

        """Create a sign up 
        button"""
        self.signup_button = ctk.CTkButton(self.border_frame, width=140, text="Sign Up", corner_radius=6,
                                           font=ctk.CTkFont("Arial", size=14), fg_color="black",
                                           hover_color="gray", text_color="white")
        self.signup_button.place(x=130, y=370)

    def show(self):
        """Method for showing
        password_entry"""
        show_image = ctk.CTkImage(Image.open("images/show.png").resize((32, 32)))
        self.hide_button.configure(image=show_image, command=self.hide)
        self.password_entry.configure(show="")

    def hide(self):
        """Method for hiding
        password_entry"""
        hide_image = ctk.CTkImage(Image.open("images/hide.png").resize((32, 32)))
        self.hide_button.configure(image=hide_image, command=self.show)
        self.password_entry.configure(show="•")

    def login(self):
        """Method for
        logging in to the
        application"""
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == 'admin' and password == '1234':
            """Displays the main application window"""
            main_app = ApplicationPage(self)
            main_app.grab_set()


if __name__ == "__main__":
    login = Login()
    login.mainloop()
