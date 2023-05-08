"""This is the login window
for the main application"""

from tkinter import *
import customtkinter as ctk
from PIL import ImageTk, Image


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
                                          hover_color="gray")
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
                                           hover_color="gray")
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


if __name__ == "__main__":
    login = Login()
    login.mainloop()
