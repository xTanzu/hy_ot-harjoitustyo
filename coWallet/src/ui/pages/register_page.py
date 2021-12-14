import tkinter

from ui.pages.page import Page
import ui.pages.sign_in_page as sign_in_page

from utils.helper import Helper
from config import *

class RegisterPage(Page):
    """Class for the register page

    Args:
        Page: Inherits the Page base-class
    """

    def __init__(self, *args, **kwargs):
        """Constructor of the RegisterPage class
        """
        super().__init__(*args, **kwargs)
        
        # Define Labels
        self.first_name_label = tkinter.Label(self, text="first name:")
        self.last_name_label = tkinter.Label(self, text="last name:")
        self.username_label = tkinter.Label(self, text="username:")
        self.username_available_label = tkinter.Label(self, text="")
        self.password_label = tkinter.Label(self, text="password:")
        self.password_again_label = tkinter.Label(self, text="password again:")
        self.info_label = tkinter.Label(self, text="")
        self.error_label = tkinter.Label(self, text="")

        # Define entries
        self.first_name_entry = tkinter.Entry(self, width=ENTRY_FIELD_WIDTH)
        self.last_name_entry = tkinter.Entry(self, width=ENTRY_FIELD_WIDTH)
        self.username_entry = tkinter.Entry(self, width=ENTRY_FIELD_WIDTH)
        self.password_entry = tkinter.Entry(self, width=ENTRY_FIELD_WIDTH)
        self.password_again_entry = tkinter.Entry(self, width=ENTRY_FIELD_WIDTH)

        # Define Buttons
        self.check_username_available_button = tkinter.Button(self, text="Check", command=lambda: self.check_username_available())
        self.register_button = tkinter.Button(self, text="Register", command=self.register_pressed)
        self.back_button = tkinter.Button(self, text="Back", command=lambda: self.controller.switch_page_to(sign_in_page.SignInPage))

        # Position Widgets
        self.first_name_label.grid(row=0, column=0, sticky="W")
        self.first_name_entry.grid(row=1, column=0)
        self.last_name_label.grid(row=2, column=0, sticky="W")
        self.last_name_entry.grid(row=3, column=0)
        self.username_label.grid(row=4, column=0, sticky="W")
        self.username_entry.grid(row=5, column=0)
        self.check_username_available_button.grid(row=5, column=1)
        self.username_available_label.grid(row=6, column=1)
        self.password_label.grid(row=6, column=0, sticky="W")
        self.password_entry.grid(row=7, column=0)
        self.password_again_label.grid(row=8, column=0, sticky="W")
        self.password_again_entry.grid(row=9, column=0)
        self.info_label.grid(row=10, column=0, sticky="W")
        self.back_button.grid(row=11, column=0, sticky="W")
        self.register_button.grid(row=11, column=0)
        self.error_label.grid(row=12, column=0, sticky="W")
    
    def check_username_available(self) -> bool:
        """Check if a given username is available

        Returns:
            bool: Boolean value representing the availability of the username,
                False also if not correct form
        """
        username = self.username_entry.get()
        if Helper.is_valid_username(username):
            if self.controller.user_service.username_available(username):
                self.username_available_label["text"] = "Available!"
                return True
            else:
                self.username_available_label["text"] = "Not available..."
                return False
        else:
            self.username_available_label["text"] = "Not valid form"
            return False
    
    def register_pressed(self):
        """Functionality what happens when the "Register" button is pressed

        Raises:
            SystemError: If an unexpected error happens
        """
        errorMsgs = {
        "username": """username must be:
                6-200 chars long
                consist of lowercase letters (a-ö)
                uppercase letters (A-Ö)
                numbers (0-9) and
                special characters !()-.?[]_'~;:!@#$%^&*+=
                it cannot start with a special character\n""", 
        "password": """password must be:
                8-200 chars long
                consist of lowercase letters (a-ö)
                uppercase letters (A-Ö)
                numbers (0-9) and
                special characters !()-.?[]_'~;:!@#$%^&*+=
                must contain at least one character of each
                it cannot start with a special character\n""", 
        "first_name": """first name must be:
                1-200 chars long
                consist of lowercase letters (a-ö)
                uppercase letters (A-Ö)
                numbers (0-9) and
                special characters !()-.?[]_'~;:!@#$%^&*+=
                it must start with a letter\n""", 
        "last_name": """last name must be:
                1-200 chars long
                consist of lowercase letters (a-ö)
                uppercase letters (A-Ö)
                numbers (0-9) and
                special characters !()-.?[]_'~;:!@#$%^&*+=
                it must start with a letter\n"""}
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        password_again = self.password_again_entry.get()
        if not Helper.is_valid_name(first_name):
            self.info_label["text"] = "First name is not valid form"
            self.error_label["text"] = errorMsgs["first_name"]
        elif not Helper.is_valid_name(last_name):
            self.info_label["text"] = "Last name is not valid form"
            self.error_label["text"] = errorMsgs["last_name"]
        elif not self.check_username_available():
            self.info_label["text"] = "Try another username"
            self.error_label["text"] = ""
            if not Helper.is_valid_username(username):
                self.error_label["text"] = errorMsgs["username"]
        elif not Helper.is_valid_password(password):
            self.info_label["text"] = "Password is not valid form"
            self.error_label["text"] = errorMsgs["password"]
        elif password != password_again:
            self.error_label["text"] = ""
            self.info_label["text"] = "Passwords do not match"
        else:
            self.error_label["text"] = ""
            self.info_label["text"] = ""
            if self.controller.user_service.create_user(username, password, first_name, last_name):
                self.info_label["text"] = "Got it!"
                self.controller.switch_page_to(sign_in_page.SignInPage)
            else:
                raise SystemError("Something went wrong")