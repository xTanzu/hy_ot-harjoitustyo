import tkinter
from services.user_service import UserService
from utils.helper import Helper

ENTRY_FIELD_WIDTH = 40

class Page(tkinter.Frame):

    def __init__(self, *args, **kwargs):
        self.name, parent, self.controller = (kwargs.pop(x) for x in ("name", "parent", "controller"))
        super().__init__(parent, *args, **kwargs)

    def show(self):
        self.lift()

class MainTkFrame(tkinter.Tk):

    def __init__(self, user_service:UserService, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_service = user_service
        self.container = tkinter.Frame()
        self.container.grid(row=0, column=0, sticky='nesw')
        self.pages = {}
        self.usable_pages = [SignInPage, RegisterPage, UserMainPage, WelcomePage, SecondPage]
        page = self.construct_page(self.usable_pages[0])
        page.show()
    
    def construct_page(self, usable_page:type) -> Page:
        page_name = usable_page.__name__
        if page_name in self.pages:
            raise NameError(f"Page {page_name} allready exists, can't construct it")
        page = usable_page(name=page_name, parent=self.container, controller=self)
        page.grid(row=0, column=0, sticky="nsew")
        self.pages[page_name] = page
        return page
    
    def switch_page_to(self, page_name:str):
        if page_name not in self.pages:
            try:
                page_indx = [usable_page.__name__ for usable_page in self.usable_pages].index(page_name)
                self.construct_page(self.usable_pages[page_indx])
            except:
                raise NameError(f"Page {page_name} is not usable, can't switch to it")
        self.pages[page_name].show()

class WelcomePage(Page):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        label = tkinter.Label(self, text=f"I'm {self.name}")
        button = tkinter.Button(self, text=f"Button to SecondPage", command= lambda: self.controller.switch_page_to("SecondPage"))
        label.pack()
        button.pack()

class SecondPage(Page):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class SignInPage(Page):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Define Labels
        self.username_label = tkinter.Label(self, text="username:")
        self.password_label = tkinter.Label(self, text="password:")
        self.info_label = tkinter.Label(self, text="")

        # Define entries
        self.username_entry = tkinter.Entry(self, width=ENTRY_FIELD_WIDTH)
        self.password_entry = tkinter.Entry(self, width=ENTRY_FIELD_WIDTH)

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
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.controller.user_service.login(username, password):
            self.controller.switch_page_to("UserMainPage")
        else:
            self.info_label["text"] = "Wrong username or password"

    def register_pressed(self):
        self.controller.switch_page_to("RegisterPage")

class RegisterPage(Page):

    def __init__(self, *args, **kwargs):
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
        self.register_button = tkinter.Button(self, text="Register", command=lambda: self.register_pressed())

        # Insert on screen
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
        self.register_button.grid(row=11, column=0)
        self.error_label.grid(row=12, column=0, sticky="W")
    
    def check_username_available(self) -> bool:
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
                self.controller.switch_page_to("SignInPage")
            else:
                raise SystemError("Something went wrong")

class UserMainPage(Page):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("Not yet implemented")
        label = tkinter.Label(self, text="UserMainPage: Not yet implemented")
        label.pack()

class GraphicalUi:

    def __init__(self, db_type:str = None, db_path:str = None):
        self.__user_service = UserService(db_type, db_path)
        self.__mainFrame = MainTkFrame(self.__user_service)
    
    def start_ui(self):
        self.__mainFrame.mainloop()
