from tkinter import *
from services.user_service import UserService
from utils.helper import Helper

ENTRY_FIELD_WIDTH = 40

class GraphicalUi:

    def __init__(self, db_type:str = None, db_path:str = None):
        self.__user_service = UserService(db_type, db_path)
        self.root = Tk()
    
    def start_ui(self):
        self.sign_in_view()
        self.root.mainloop()
    
    # Views

    def sign_in_view(self):

        # Button Presses
        def sign_in_pressed():
            username = username_entry.get()
            password = password_entry.get()
            if self.__user_service.login(username, password):
                self.account_view()
            else:
                info_label.set # Miten laitat labelille arvon?
        
        def register_pressed():
            pass

        # Define Labels
        username_label = Label(self.root, text="username:")
        password_label = Label(self.root, text="password:")
        info_label = Label(self.root, text="")

        # Define entries
        username_entry = Entry(self.root, width=ENTRY_FIELD_WIDTH)
        password_entry = Entry(self.root, width=ENTRY_FIELD_WIDTH)

        # Define Buttons
        signin_button = Button(self.root, text="Sign in", command=lambda: sign_in_pressed())
        register_button = Button(self.root, text="Register")

        # Insert on screen
        username_label.grid(row=0, column=0, sticky="W")
        username_entry.grid(row=1, column=0, columnspan=1)
        password_label.grid(row=2, column=0, sticky="W")
        password_entry.grid(row=3, column=0, columnspan=1)
        info_label.grid(row=4, column=0, sticky="W")
        signin_button.grid(row=5, column=0)
        register_button.grid(row=6, column=0)
    
    def register_view(self):
        print("registering")
        Label(self.root, text="Registering").grid(row=6)

    def account_view(self):
        print("logged in")
        Label(self.root, text="Logged in").grid(row=6)
