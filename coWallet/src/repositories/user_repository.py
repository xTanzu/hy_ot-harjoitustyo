from entities.user import User
from dbaos.user_dbao import UserDbao
from utils.helper import Helper

class UserRepository:

    def __init__(self, db_type:str = None, db_path:str = None):
        self.__user_dbao = UserDbao(db_type, db_path)

    def disconnect_db(self):
        self.__user_dbao.disconnect()

    def insert_new_user(self, username:str, password:str, first_name:str, last_name:str) -> bool:
        if Helper.is_valid_username(username) and Helper.is_valid_password(password) and \
            Helper.is_valid_name(first_name) and Helper.is_valid_name(last_name):
            return self.__user_dbao.insert_new_user(username, password, first_name, last_name)
        print("""User insert consists of illegal characters\n
        Use only lower case (a-ö) or upper case (A-Ö) characters, \n
        digits (0-9) and special characters (!()-.?[]_'~;:!@#$%^&*+=)""")
        return False

    def username_exists(self, inserted_username:str) -> bool:
        result = self.__user_dbao.find_user_by_username(inserted_username)
        if result:
            return True
        return False

    def get_user_by_username(self, inserted_username:str) -> User:
        user_id, username, first_name, last_name = \
            self.__user_dbao.find_user_by_username(inserted_username)
        user = User(user_id, username, first_name, last_name)
        return user

    def username_password_match(self, inserted_username:str, inserted_password:str) -> bool:
        if not self.username_exists(inserted_username):
            return False
        username, password = self.__user_dbao.find_password_by_username(inserted_username)
        return (inserted_username, inserted_password) == (username, password)
