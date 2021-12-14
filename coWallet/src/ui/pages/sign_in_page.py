import tkinter

from ui.pages.page import Page
import ui.pages.register_page as register_page
import ui.pages.user_main_page as user_main_page

from config import *

class SignInPage(Page):
    """Class for the sign in page

    Args:
        Page: Inherits the Page base-class
    """

    def __init__(self, *args, **kwargs):
        """Constructor of the SignInPage class
        """

        super().__init__(*args, **kwargs)

        # Define Labels
        self.username_label = tkinter.Label(self, text="username:")
        self.password_label = tkinter.Label(self, text="password:")
        self.info_label = tkinter.Label(self, text="")

        # Define entries
        self.username_entry = tkinter.Entry(self, width=ENTRY_FIELD_WIDTH)
        self.password_entry = tkinter.Entry(self, width=ENTRY_FIELD_WIDTH)
        self.username_entry.insert(0, "tanzu") # POISTA!!!!!!!!!!!!!!!!!
        self.password_entry.insert(0, "Salasana1!") # POISTA!!!!!!!!!!!!!!!!!

        # Define Buttons
        self.signin_button = tkinter.Button(self, text="Sign in", command=lambda: self.sign_in_pressed())
        self.register_button = tkinter.Button(self, text="Register", command=lambda: self.register_pressed())

        # Insert on screen
        self.username_label.grid(row=0, column=0, sticky="W")
        self.username_entry.grid(row=1, column=0)
        self.password_label.grid(row=2, column=0, sticky="W")
        self.password_entry.grid(row=3, column=0)
        self.info_label.grid(row=4, column=0, sticky="W")
        self.signin_button.grid(row=5, column=0)
        self.register_button.grid(row=6, column=0)
    
    def sign_in_pressed(self):
        """Functionality what happens when the "Sign in" button is pressed
        """
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.controller.user_service.login(username, password):
            self.controller.switch_page_to(user_main_page.UserMainPage)
        else:
            self.info_label["text"] = "Wrong username or password"

    def register_pressed(self):
        """Functionality what happens when the register button is pressed
        """
        self.controller.switch_page_to(register_page.RegisterPage)