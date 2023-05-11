"""This is the sign-up window
that will be linked to the
login window with database"""

from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
from PIL import ImageTk, Image
import ast


class Signup(ctk.CTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.geometry("1000x750")
        self.resizable(False, False)
        self.title("Create New Account")

        """Display a background image
        for the sign up window"""
        self.background_img = ImageTk.PhotoImage(Image.open("images/new.png"))
        self.background_label = Label(self, image=self.background_img, bg="white")
        self.background_label.pack()

        """Create a border frame for 
        label and entry widgets"""
        self.border_frame = ctk.CTkFrame(self.background_label, width=500, height=570,
                                         fg_color="white")
        self.border_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        """Add main header and 
        subhead for sign up page"""
        self.login_heading = ctk.CTkLabel(self.border_frame, text="Create New Account",
                                          font=ctk.CTkFont("Arial", size=40),
                                          text_color="black")
        self.login_heading.place(x=65, y=40)

        self.login_subheading = ctk.CTkLabel(self.border_frame, text="Not yet registered? Sign up now.",
                                             font=ctk.CTkFont("Arial", size=14),
                                             text_color="black")
        self.login_subheading.place(x=140, y=95)

        """This is a label and entry
        widget for username"""
        self.username_label = ctk.CTkLabel(self.border_frame, bg_color="transparent", fg_color="transparent",
                                           text="Username", text_color="black",
                                           font=ctk.CTkFont("Arial", size=16))
        self.username_label.place(x=120, y=155)
        self.username_entry = ctk.CTkEntry(self.border_frame, width=250, height=35, fg_color="black",
                                           placeholder_text="name@example.com", placeholder_text_color="white",
                                           font=ctk.CTkFont("Arial", size=13, slant="italic"), text_color="white",
                                           border_color="gray")
        self.username_entry.place(x=120, y=190)

        """This is a label and entry
        widget for first password"""
        self.password_label1 = ctk.CTkLabel(self.border_frame, bg_color="transparent", fg_color="transparent",
                                            text="Password", text_color="black",
                                            font=ctk.CTkFont("Arial", size=16))
        self.password_label1.place(x=120, y=235)
        self.password_entry1 = ctk.CTkEntry(self.border_frame, width=250, height=35, fg_color="black",
                                            placeholder_text="8-12 characters", placeholder_text_color="white",
                                            font=ctk.CTkFont("Arial", size=13, slant="italic"), text_color="white",
                                            border_color="gray", show="•")
        self.password_entry1.place(x=120, y=270)

        """Create a hide/show button
        for the first password entry"""
        hide_image1 = ctk.CTkImage(Image.open("images/hide.png").resize((32, 32)))
        self.hide_button1 = ctk.CTkButton(self, image=hide_image1, text="", width=10,
                                          anchor="center", fg_color="transparent", bg_color="black",
                                          hover=False, command=self.show1)
        self.hide_button1.place(x=570, y=363)

        """This is a label and entry
        widget for second password"""
        self.password_label2 = ctk.CTkLabel(self.border_frame, bg_color="transparent", fg_color="transparent",
                                            text="Confirm Password", text_color="black",
                                            font=ctk.CTkFont("Arial", size=16))
        self.password_label2.place(x=120, y=320)
        self.password_entry2 = ctk.CTkEntry(self.border_frame, width=250, height=35, fg_color="black",
                                            placeholder_text="Re-type your password", placeholder_text_color="white",
                                            font=ctk.CTkFont("Arial", size=13, slant="italic"), text_color="white",
                                            border_color="gray", show="•")
        self.password_entry2.place(x=120, y=355)

        """Create a hide/show button
        for the second password entry"""
        hide_image2 = ctk.CTkImage(Image.open("images/hide.png").resize((32, 32)))
        self.hide_button2 = ctk.CTkButton(self, image=hide_image2, text="", width=10,
                                          anchor="center", fg_color="transparent", bg_color="black",
                                          hover=False, command=self.show2)
        self.hide_button2.place(x=570, y=448)

        """Create a sign up button"""
        self.signup_button = ctk.CTkButton(self.border_frame, width=140, text="Sign Up", corner_radius=6,
                                           font=ctk.CTkFont("Arial", size=16), fg_color="black",
                                           hover_color="gray", text_color="white",
                                           command=self.signup)
        self.signup_button.place(x=180, y=420)

        """Create divider label
        that separates the two
        buttons"""
        self.separator_label = ctk.CTkLabel(self.border_frame, bg_color="transparent", fg_color="transparent",
                                            text="Already have an account?", text_color="black",
                                            font=ctk.CTkFont("Arial", size=14))
        self.separator_label.place(x=170, y=475)

        """Create a return to 
        login button"""
        self.return_button = ctk.CTkButton(self.border_frame, width=140, text="Return to Login", corner_radius=6,
                                           font=ctk.CTkFont("Arial", size=16), fg_color="black",
                                           hover_color="gray", text_color="white", command=self.return_login)
        self.return_button.place(x=180, y=520)

    def show1(self):
        """Method for showing
        first password entry"""
        show_image = ctk.CTkImage(Image.open("images/show.png").resize((32, 32)))
        self.hide_button1.configure(image=show_image, command=self.hide1)
        self.password_entry1.configure(show="")

    def hide1(self):
        """Method for hiding
        first password entry"""
        hide_image = ctk.CTkImage(Image.open("images/hide.png").resize((32, 32)))
        self.hide_button1.configure(image=hide_image, command=self.show1)
        self.password_entry1.configure(show="•")

    def show2(self):
        """Method for showing
        second password entry"""
        show_image = ctk.CTkImage(Image.open("images/show.png").resize((32, 32)))
        self.hide_button2.configure(image=show_image, command=self.hide2)
        self.password_entry2.configure(show="")

    def hide2(self):
        """Method for hiding
        second password entry"""
        hide_image = ctk.CTkImage(Image.open("images/hide.png").resize((32, 32)))
        self.hide_button2.configure(image=hide_image, command=self.show2)
        self.password_entry2.configure(show="•")

    def signup(self):
        """Method for creating
        an account"""
        username = self.username_entry.get()
        password = self.password_entry1.get()
        confirm_pass = self.password_entry2.get()

        if password == confirm_pass:
            try:
                """If file is available it will 
                read the file and append data"""
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
                """If file is unavailable, then
                it will create the file"""
                file = open('datasheet', 'w')
                pp = str({'Username': 'Password'})
                file.write(pp)
                file.close()
        else:
            """Shows an error dialog box"""
            messagebox.showerror("Invalid", "Both passwords don't match! Try again.")

    def return_login(self):
        """Method that will destroy
        current window and open login
        window"""
        Signup.destroy(self)


if __name__ == "__main__":
    signup = Signup()
    signup.mainloop()
