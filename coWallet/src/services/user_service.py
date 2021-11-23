from entities.user import User
from repositories.user_repository import User_Repository
from utils.helper import Helper

class CredentialsError(Exception):
    pass

class User_Service:

    def __init__(self, db_type:str = None, db_path:str = None):
        self.__user_repository = User_Repository(db_type, db_path)
        self.__user = None
    
    def create_user(self, username:str, password:str, first_name:str, last_name:str) -> bool:
        if not Helper.is_valid_username(username):
            raise CredentialsError("username is not correct form")
        if self.__user_repository.username_exists(username):
            raise CredentialsError("username already exists!")
        if not Helper.is_valid_password(password):
            raise CredentialsError("password is not correct form")
        if not Helper.is_valid_name(first_name):
            raise CredentialsError("first name is not correct form")
        if not Helper.is_valid_name(last_name):
            raise CredentialsError("last name is not correct form")
        return self.__user_repository.insert_new_user(username, password, first_name, last_name)
    
    def login(self, username:str, password:str) -> bool:
        if self.__user_repository.username_password_match(username, password):
            self.__user = self.__user_repository.get_user_by_username(username)
            return True
        return False
    
    def get_current_user(self) -> User:
        return self.__user
    
    def logout(self):
        self.__user = None