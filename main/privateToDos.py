"""Author: Venise Saron
Professor: Corey Seliger
Subject: SDEV140
Last Revised: 5-13-2023
Purpose: This program is a GUI application of a private
To-Do List coupled with a Login Window and Sign-Up Window."""

# Import the necessary modules
import tkinter
from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
from PIL import ImageTk, Image
import ast

# This sets the appearance mode for the entire application
ctk.set_appearance_mode("light")


class Signup(tkinter.Toplevel):
    """Class that holds all the widgets for the Sign-Up window.
    Users who don't have an account may interact with this window
    to create one. This will immediately be saved in the 'datasheet'
    - our app's database."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.geometry("1000x750")
        self.resizable(False, False)  # Sets the window to be non-resizable
        self.title("Create New Account")

        """Displays a background image for the sign-up window"""
        self.background_img = ImageTk.PhotoImage(Image.open("images/new.png"))
        self.background_label = Label(self, image=self.background_img, bg="white")
        self.background_label.pack()

        """Create a border frame for label and entry widgets"""
        self.border_frame = ctk.CTkFrame(self.background_label, width=500, height=570,
                                         fg_color="white")
        self.border_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        """Add a main header and subhead for sign-up page"""
        # Customizations for Header
        self.login_heading = ctk.CTkLabel(self.border_frame, text="Create New Account",
                                          font=ctk.CTkFont("Arial", size=40),
                                          text_color="black")
        self.login_heading.place(x=65, y=40)

        # Customizations for Subhead
        self.login_subheading = ctk.CTkLabel(self.border_frame, text="Not yet registered? Sign up now.",
                                             font=ctk.CTkFont("Arial", size=14),
                                             text_color="black")
        self.login_subheading.place(x=140, y=95)

        """This is a label and entry widget for username"""
        # Customizations for Username Label
        self.username_label = ctk.CTkLabel(self.border_frame, bg_color="transparent", fg_color="transparent",
                                           text="Username", text_color="black",
                                           font=ctk.CTkFont("Arial", size=16))
        self.username_label.place(x=120, y=155)

        # Customizations for Username Entry
        self.username_entry = ctk.CTkEntry(self.border_frame, width=250, height=35, fg_color="black",
                                           placeholder_text="name@example.com", placeholder_text_color="white",
                                           font=ctk.CTkFont("Arial", size=13, slant="italic"), text_color="white",
                                           border_color="gray")
        self.username_entry.place(x=120, y=190)

        """This is a label and entry widget for the first password"""
        # Customizations for Password Label
        self.password_label1 = ctk.CTkLabel(self.border_frame, bg_color="transparent", fg_color="transparent",
                                            text="Password", text_color="black",
                                            font=ctk.CTkFont("Arial", size=16))
        self.password_label1.place(x=120, y=235)

        # Customizations for Password Entry
        self.password_entry1 = ctk.CTkEntry(self.border_frame, width=250, height=35, fg_color="black",
                                            placeholder_text="8-12 characters", placeholder_text_color="white",
                                            font=ctk.CTkFont("Arial", size=13, slant="italic"), text_color="white",
                                            border_color="gray", show="•")
        self.password_entry1.place(x=120, y=270)

        """Create a hide/show button for the first password entry"""
        self.hide_image1 = ctk.CTkImage(Image.open("images/hide.png").resize((32, 32)))
        self.hide_button1 = ctk.CTkButton(self, image=self.hide_image1, text="", width=10,
                                          anchor="center", fg_color="transparent", bg_color="black",
                                          hover=False, command=self.show1)
        self.hide_button1.place(x=570, y=363)

        """This is a label and entry widget for the second password"""
        # Customizations for Confirm Password Label
        self.password_label2 = ctk.CTkLabel(self.border_frame, bg_color="transparent", fg_color="transparent",
                                            text="Confirm Password", text_color="black",
                                            font=ctk.CTkFont("Arial", size=16))
        self.password_label2.place(x=120, y=320)
        # Customizations for Confirm Password Entry
        self.password_entry2 = ctk.CTkEntry(self.border_frame, width=250, height=35, fg_color="black",
                                            placeholder_text="Re-type your password", placeholder_text_color="white",
                                            font=ctk.CTkFont("Arial", size=13, slant="italic"), text_color="white",
                                            border_color="gray", show="•")
        self.password_entry2.place(x=120, y=355)

        """Create a hide/show button for the second password entry"""
        self.hide_image2 = ctk.CTkImage(Image.open("images/hide.png").resize((32, 32)))
        self.hide_button2 = ctk.CTkButton(self, image=self.hide_image2, text="", width=10,
                                          anchor="center", fg_color="transparent", bg_color="black",
                                          hover=False, command=self.show2)
        self.hide_button2.place(x=570, y=448)

        """Create a sign-up button"""
        self.signup_button = ctk.CTkButton(self.border_frame, width=140, text="Sign Up", corner_radius=6,
                                           font=ctk.CTkFont("Arial", size=16), fg_color="black",
                                           hover_color="gray", text_color="white",
                                           command=self.signup)
        self.signup_button.place(x=180, y=420)

        """Create divider label that separates the two buttons"""
        self.separator_label = ctk.CTkLabel(self.border_frame, bg_color="transparent", fg_color="transparent",
                                            text="Already have an account?", text_color="black",
                                            font=ctk.CTkFont("Arial", size=14))
        self.separator_label.place(x=170, y=475)

        """Create a return to login button"""
        self.return_button = ctk.CTkButton(self.border_frame, width=140, text="Return to Login", corner_radius=6,
                                           font=ctk.CTkFont("Arial", size=16), fg_color="black",
                                           hover_color="gray", text_color="white", command=self.return_login)
        self.return_button.place(x=180, y=520)

    def show1(self):
        """Method for showing password entry"""
        show_image = ctk.CTkImage(Image.open("images/show.png").resize((32, 32)))
        self.hide_button1.configure(image=show_image, command=self.hide1)
        self.password_entry1.configure(show="")

    def hide1(self):
        """Method for hiding password entry"""
        hide_image = ctk.CTkImage(Image.open("images/hide.png").resize((32, 32)))
        self.hide_button1.configure(image=hide_image, command=self.show1)
        self.password_entry1.configure(show="•")

    def show2(self):
        """Method for showing confirm password entry"""
        show_image = ctk.CTkImage(Image.open("images/show.png").resize((32, 32)))
        self.hide_button2.configure(image=show_image, command=self.hide2)
        self.password_entry2.configure(show="")

    def hide2(self):
        """Method for hiding confirm password entry"""
        hide_image = ctk.CTkImage(Image.open("images/hide.png").resize((32, 32)))
        self.hide_button2.configure(image=hide_image, command=self.show2)
        self.password_entry2.configure(show="•")

    def signup(self):
        """Method for creating an account"""
        username = self.username_entry.get()
        password = self.password_entry1.get()
        confirm_pass = self.password_entry2.get()

        """If-Elif-Else statements for validation checks"""
        if username == "" and password == "" and confirm_pass == "":
            """Shows a warning dialog box"""
            messagebox.showwarning("Warning", "Please don't leave any empty fields!")

        elif username == "" and password != "" and confirm_pass == "":
            """Shows a warning dialog box"""
            messagebox.showwarning("Warning", "Please don't leave any empty fields!")

        elif username == "" and password == "" and confirm_pass != "":
            """Shows a warning dialog box"""
            messagebox.showwarning("Warning", "Please don't leave any empty fields!")

        elif username != "" and password == "" and confirm_pass == "":
            """Shows an error dialog box"""
            messagebox.showerror("Empty Field Detected", "Please don't leave passwords fields empty!")

        elif username == "" and password == confirm_pass:
            """Shows an error dialog box"""
            messagebox.showerror("Empty Field Detected", "Please don't leave username field empty!")

        elif username != "" and password != confirm_pass:
            """Shows an error dialog box"""
            messagebox.showerror("Invalid", "Both passwords don't match! Try again.")

        else:
            """If requirements are met, the account will be created"""
            try:
                """If file is available it will read the file and append data"""
                file = open("datasheet", "r+")
                d = file.read()
                r = ast.literal_eval(d)

                database = {username: password}
                r.update(database)
                file.truncate(0)
                file.close()

                file = open('datasheet', 'w')
                file.write(str(r))

                messagebox.showinfo("Sign Up", "Your account has been created.")

            except:
                """If file is unavailable, then it will create the file"""
                file = open('datasheet', 'w')
                pp = str({'Username': 'Password'})
                file.write(pp)
                file.close()

    def return_login(self):
        """Method that will destroy current window and open login window"""
        Signup.destroy(self)


class ApplicationPage(tkinter.Toplevel):
    """Class that displays the Main Application window. After logging
    in, users can interact with the widgets inside this window."""

    def __init__(self, master):
        super().__init__(master)

        self.geometry("1050x900")  # May need a bigger screen display to accommodate app size
        self.resizable(False, False)  # Sets the window to be non-resizable
        self.title("Private To-Do's")

        """Displays a background image for the main application window"""
        self.background_img = ImageTk.PhotoImage(Image.open("images/main2.jpg"))
        self.background_label = Label(self, image=self.background_img, bg="white")
        self.background_label.pack()

        """Create a main frame that will hold the rest of the widgets"""
        self.main_frame = ctk.CTkFrame(self.background_label, width=800, height=750,
                                       fg_color="white", bg_color="black", corner_radius=30)
        self.main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        """Create logout button that will return to previous page"""
        self.back_button = ctk.CTkButton(self.main_frame, text="Logout", width=110, corner_radius=6,
                                         font=ctk.CTkFont("Arial", size=16), fg_color="black",
                                         hover_color="gray", text_color="white", command=self.return_login)
        self.back_button.place(x=40, y=40)

        """Create two empty lists that will hold the tasks entered for each category"""
        self.not_comp_list = []
        self.comp_list = []

        """Add labels for main header and a subhead"""
        # Customizations for Main Header
        self.heading = ctk.CTkLabel(self.main_frame, text="To-Do List", font=ctk.CTkFont("Arial", size=40))
        self.heading.place(x=310, y=75)

        # Customizations for Subhead
        self.subheading = ctk.CTkLabel(self.main_frame, text="Start your day productively.",
                                       font=ctk.CTkFont("Arial", size=16))
        self.subheading.place(x=310, y=130)

        """Create scrollable frame that will hold the widgets needed for the task entries"""
        self.scrollable_frame = ctk.CTkScrollableFrame(self, width=700, height=500, corner_radius=10,
                                                       fg_color="black", scrollbar_fg_color="black")
        self.scrollable_frame.place(x=160, y=250)

        """Create an entry widget within scrollable frame"""
        self.user_entry = ctk.CTkEntry(self.scrollable_frame, height=40,
                                       placeholder_text="Input task name here...",
                                       placeholder_text_color="black", corner_radius=10,
                                       font=ctk.CTkFont("Arial", size=18, slant="italic"),
                                       border_color="white")
        self.user_entry.pack(fill="x")

        """Create a frame where initial tasks are placed inside the not completed category"""
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

        """Create a frame where after finished button is clicked, 
        tasks are placed in the completed category"""
        self.comp_frame = ctk.CTkFrame(self.scrollable_frame, height=210,
                                       fg_color="white", corner_radius=10)
        self.comp_label = ctk.CTkLabel(self.comp_frame, text="Completed",
                                       text_color="black",
                                       font=ctk.CTkFont("Times New Roman", size=20, weight="bold"))
        self.task_listbox_2 = Listbox(self.comp_frame, width=80, height=5,
                                      font=("Arial", 16), justify="center",
                                      selectbackground="gray", selectmode="single")

        # Pack the frame, label, and listbox
        self.comp_frame.pack(pady=10, fill="x")
        self.comp_label.place(x=30, y=10)
        self.task_listbox_2.place(x=30, y=50)

        """Create a button for adding tasks"""
        self.add_button = ctk.CTkButton(self.scrollable_frame, text="Add Task", width=120,
                                        corner_radius=6, font=ctk.CTkFont("Arial", size=16),
                                        fg_color="black", bg_color="white", hover_color="gray",
                                        text_color="white", command=self.add_task)
        self.add_button.place(x=570, y=6)

        """Add a functional button that when clicked, will move 
        selected task to under the completed category"""
        self.comp_button = ctk.CTkButton(self.not_comp_frame, text="Finished", width=100,
                                         corner_radius=6, font=ctk.CTkFont("Arial", size=16),
                                         fg_color="black", hover_color="gray",
                                         text_color="white", command=self.complete)
        self.comp_button.place(x=230, y=175)

        """Add a functional button that when clicked, will move 
        selected task under the not completed category"""
        self.not_comp_button = ctk.CTkButton(self.comp_frame, text="Unfinished", width=100,
                                             corner_radius=6, font=ctk.CTkFont("Arial", size=16),
                                             fg_color="black", hover_color="gray",
                                             text_color="white", command=self.not_complete)
        self.not_comp_button.place(x=230, y=175)

        """Add a functional button that when clicked, will delete 
        selected task in the not completed category"""
        self.del_not_comp_button = ctk.CTkButton(self.not_comp_frame, text="Delete", width=100,
                                                 corner_radius=6, font=ctk.CTkFont("Arial", size=16),
                                                 fg_color="black", hover_color="gray",
                                                 text_color="white", command=self.delete_not_comp)
        self.del_not_comp_button.place(x=370, y=175)

        """Add a functional button that when clicked, will delete 
        selected task in the completed category"""
        self.del_comp_button = ctk.CTkButton(self.comp_frame, text="Delete", width=100,
                                             corner_radius=6, font=ctk.CTkFont("Arial", size=16),
                                             fg_color="black", hover_color="gray",
                                             text_color="white", command=self.delete_comp)
        self.del_comp_button.place(x=370, y=175)

        """Define button commands"""

    def add_task(self):
        """This command takes initial task input and puts it
        inside the not completed listbox"""
        task = self.user_entry.get()
        self.user_entry.delete(0, ctk.END)

        self.not_comp_list.append(task)
        self.task_listbox_1.insert(END, task)

    def not_complete(self):
        """This command removes the selected task from the
        completed category and moves it under the not_completed category"""
        task = str(self.task_listbox_2.get(ANCHOR))

        if task:
            self.not_comp_list.append(task)
            self.task_listbox_1.insert(END, task)
            self.task_listbox_2.delete(ANCHOR)

    def complete(self):
        """This command removes the selected task from the
        not_completed category and moves it under the completed category"""
        task = str(self.task_listbox_1.get(ANCHOR))

        if task:
            self.comp_list.append(task)
            self.task_listbox_2.insert(END, task)
            self.task_listbox_1.delete(ANCHOR)

    def delete_not_comp(self):
        """This command permanently deletes the selected task
        inside the not_completed category"""
        task_1 = str(self.task_listbox_1.get(ANCHOR))

        if task_1 in self.not_comp_list:
            self.task_listbox_1.delete(ANCHOR)

    def delete_comp(self):
        """This command permanently deletes the selected task
        inside the completed category"""
        task_2 = str(self.task_listbox_2.get(ANCHOR))

        if task_2 in self.comp_list:
            self.task_listbox_2.delete(ANCHOR)

    def return_login(self):
        """Method that closes the main application
        window and displays the login window"""
        ApplicationPage.destroy(self)


class Login(ctk.CTk):
    """This class contains all the widgets within the Login window.
    The user will interact with this window first and input a valid
    username and password before being directed to the main
    application window."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.geometry("1000x750")
        self.resizable(False, False)  # Sets the window to be non-resizable
        self.title("Login")

        """Displays a background image for the login window"""
        self.background_img = ImageTk.PhotoImage(Image.open("images/login.png"))
        self.background_label = Label(self, image=self.background_img, bg="white")
        self.background_label.pack()

        """Create a border frame for label and entry widgets"""
        self.border_frame = ctk.CTkFrame(self.background_label, width=400, height=450,
                                         fg_color="white")
        self.border_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        """Add main header and subhead for login page"""
        self.login_heading = ctk.CTkLabel(self.border_frame, text="Login",
                                          font=ctk.CTkFont("Arial", size=40),
                                          text_color="black")
        self.login_heading.place(x=150, y=40)

        self.login_subheading = ctk.CTkLabel(self.border_frame, text="Sign in to continue.",
                                             font=ctk.CTkFont("Arial", size=14),
                                             text_color="black")
        self.login_subheading.place(x=140, y=95)

        # Entry widgets for Login window don't have labels
        # for styling purposes, but they do have
        # placeholder texts to identify which is which
        """Create an entry widget for username"""
        self.username_entry = ctk.CTkEntry(self.border_frame, width=240, height=35, fg_color="black",
                                           placeholder_text="Username", placeholder_text_color="white",
                                           font=ctk.CTkFont("Arial", size=14), text_color="white",
                                           border_color="gray")
        self.username_entry.place(x=80, y=150)

        """Create an entry widget for password"""
        self.password_entry = ctk.CTkEntry(self.border_frame, width=240, height=35, fg_color="black",
                                           placeholder_text="Password", placeholder_text_color="white",
                                           font=ctk.CTkFont("Arial", size=14), text_color="white",
                                           border_color="gray", show="•")
        self.password_entry.place(x=80, y=200)

        """Create a show/hide button for password_entry"""
        self.hide_image = ctk.CTkImage(Image.open("images/hide.png").resize((32, 32)))
        self.hide_button = ctk.CTkButton(self, image=self.hide_image, text="", width=10,
                                         anchor="center", fg_color="transparent", bg_color="black",
                                         hover=False, command=self.show)
        self.hide_button.place(x=570, y=353)

        """Create a login button"""
        self.login_button = ctk.CTkButton(self.border_frame, width=140, text="Login", corner_radius=6,
                                          font=ctk.CTkFont("Arial", size=14), fg_color="black",
                                          hover_color="gray", text_color="white", command=self.login)
        self.login_button.place(x=130, y=255)

        """Add subhead for create new account"""
        self.create_subheading = ctk.CTkLabel(self.border_frame, text="Don't have an account?",
                                              font=ctk.CTkFont("Arial", size=14),
                                              text_color="black")
        self.create_subheading.place(x=130, y=330)

        """Create a sign-up button"""
        self.signup_button = ctk.CTkButton(self.border_frame, width=140, text="Sign Up", corner_radius=6,
                                           font=ctk.CTkFont("Arial", size=14), fg_color="black",
                                           hover_color="gray", text_color="white", command=self.signup_command)
        self.signup_button.place(x=130, y=370)

    def show(self):
        """Method for showing password_entry"""
        show_image = ctk.CTkImage(Image.open("images/show.png").resize((32, 32)))
        self.hide_button.configure(image=show_image, command=self.hide)
        self.password_entry.configure(show="")

    def hide(self):
        """Method for hiding password_entry"""
        hide_image = ctk.CTkImage(Image.open("images/hide.png").resize((32, 32)))
        self.hide_button.configure(image=hide_image, command=self.show)
        self.password_entry.configure(show="•")

    def login(self):
        """Method for logging in to the application"""
        username = self.username_entry.get()
        password = self.password_entry.get()

        file = open('datasheet', 'r')
        d = file.read()
        r = ast.literal_eval(d)
        file.close()

        # Prints the available accounts in the datasheet to the console
        print(r.keys())
        print(r.values())

        if username in r.keys() and password == r[username]:
            """Displays the main application window"""
            main_app = ApplicationPage(self)
            main_app.grab_set()

        else:
            """Displays an error dialog box"""
            messagebox.showerror("Invalid", "Username and Password entered don't exist in the system.")

    def signup_command(self):
        """Method for displaying the Sign-Up window"""
        signup_window = Signup()


"""Important!! Include the entry point for program execution"""
if __name__ == "__main__":
    login = Login()
    login.mainloop()
