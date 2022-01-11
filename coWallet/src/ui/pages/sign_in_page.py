import tkinter
from entities.user import User

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
        sign_in_frame = self.set_up_sign_in_frame()
        sign_in_frame.pack(side="top", fill=None, expand=True)

    def set_up_sign_in_frame(self) -> tkinter.Frame:
        """Set up the frame for sign in form

        Returns:
            tkinter.Frame: A tkinter.Frame-object
        """
        frame = tkinter.Frame(self)
        frame.columnconfigure(0, weight=1)

        def sign_in_pressed():
            """Functionality what happens when the "Sign in" button is pressed
            """
            username = username_entry.get()
            password = password_entry.get()
            if self.controller.app_logic.login(username, password):
                user:User = self.controller.app_logic.get_current_user()
                self.controller.switch_page_to(user_main_page.UserMainPage)
            else:
                info_label["text"] = "Wrong username or password"

        def register_pressed():
            """Functionality what happens when the register button is pressed
            """
            self.controller.switch_page_to(register_page.RegisterPage)

        # Define Labels
        username_label = tkinter.Label(frame, text="username:")
        password_label = tkinter.Label(frame, text="password:")
        info_label = tkinter.Label(frame, text="")

        # Define entries
        username_entry = tkinter.Entry(frame, width=ENTRY_FIELD_WIDTH)
        password_entry = tkinter.Entry(frame, width=ENTRY_FIELD_WIDTH)
        username_entry.insert(0, "Tanzuu") # POISTA MYÖHEMMIN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        password_entry.insert(0, "Salasana1!") # POISTA MYÖHEMMIN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        # Define Buttons
        signin_button = tkinter.Button(frame, text="Sign in", command=sign_in_pressed)
        register_button = tkinter.Button(frame, text="Register", command=register_pressed)

        # Insert on screen
        username_label.grid(row=0, column=0, sticky="W")
        username_entry.grid(row=1, column=0)
        password_label.grid(row=2, column=0, sticky="W")
        password_entry.grid(row=3, column=0)
        info_label.grid(row=4, column=0, sticky="W")
        signin_button.grid(row=5, column=0)
        register_button.grid(row=6, column=0)

        return frame
