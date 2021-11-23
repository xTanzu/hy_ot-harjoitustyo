from services.user_service import User_Service
from utils.helper import Helper

class TextUi:

    def __init__(self):
        self.__user_service = User_Service()
    
    def start_ui(self):

        self.print_possible_ui_commands()

        while(True):
            command = input(">")

            if command == "quit":
                break
            elif command == "cmnds":
                self.print_possible_ui_commands()
            elif command == "login":
                self.login()
            elif command == "register":
                self.register()
            elif command == "logdas":
                self.logged_as()
            elif command == "logout":
                self.logout()
            else:
                print(f"command -{command}- does not exist\n")
        
        print("exiting")

    def print_possible_ui_commands(self):
        message = """
            Commands:
                "quit"      Quits the user interface
                "login"     Signs in to the user-account
                "register"  Registers a user-account to the system
                "logdas"    Displays the currently signed in user-account
                "logout"    Signs out from the current user account
                "cmnds"     Displays the possible commands\n"""
        print(message)
    
    def login(self):
        #print("Signs in to the user-account")
        for i in range(3):
            print(f'login tries left: {3-i}, submit empty field to quit login')
            fields = {"username": None, "password": None}
            for key in fields.keys():
                fields[key] = input(key + ": ")
                if fields[key] == "":
                    return
            if self.__user_service.login(fields["username"], fields["password"]):
                print(f"logged in as {fields['username']}\n")
                break
            print("wrong username or password\n")

    
    def register(self):
        #print("Registers a user-account to the system")
        fields = {"username": None, "password": None, "first_name": None, "last_name": None}
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
        for key in fields.keys():
            for i in range(10):
                fields[key] = input(key + ": ")
                if fields[key] == "":
                    return
                checker = None
                checker = Helper.is_valid_username if key == "username" else checker
                checker = Helper.is_valid_password if key == "password" else checker
                checker = Helper.is_valid_name if key == "first_name" or key == "last_name" else checker
                valid = checker(fields[key])
                if i > 6:
                    print("Thats too many tries, quitting\n")
                    return
                if not valid:
                    print(errorMsgs[key])
                else:
                    break
        success = self.__user_service.create_user(fields["username"], fields["password"], fields["first_name"], fields["last_name"])
        print(f'registered user {fields["username"]}\n') if success else print("Something went wrong, try again\n")
    
    def logged_as(self):
        #print("Displays the currently signed in user-account")
        user = self.__user_service.get_current_user()
        if user:
            print(f"Logged in as {user.username}\n")
            return
        print(f"No one is logged in\n")
    
    def logout(self):
        #print("Signs out from the current user account")
        logout_user_name = self.__user_service.get_current_user().username
        self.__user_service.logout()
        print(f"Logged out user {logout_user_name}\n")



if __name__ == "__main__":
    ui = TextUi()
    ui.print_possible_ui_commands()