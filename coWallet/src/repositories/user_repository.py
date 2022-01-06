from entities.user import User
from dbaos.user_dbao import UserDbao

from utils.helper import Helper
from utils.error import CredentialsError

class UserRepository:
    """Repository object for data relating to User objects.
        Combines the user data from dbao and makes User-objects.
        Has some low level methods and checks.
    """

    def __init__(self, db_type:str = None, db_path:str = None):
        """Constructor of UserRepository class

        Args:
            db_type (str, optional): Where to save db-file, either 'sqlite3_in_memory' or
                'sqlite3_file'. Defaults to 'sqlite3_file' (from config.py).

            db_path (str, optional): path where to save db-file. When
                db_type == 'sqlite3_in_memory', then has no effect.
                Defaults to "data/data.db" (from config.py).
        """
        self.__user_dbao = UserDbao(db_type, db_path)
        self.__users:dict(User) = {}

    def disconnect_db(self):
        """Closes the connection to the database.
            Essential for 'sqlite3_in_memory' testing
            in order to discard the database file.

        Raises:
            ConnectionError: If disconnection to database
                encounters an unexpected error
        """
        self.__user_dbao.disconnect()

    def insert_new_user(self, username:str, password:str, password_again:str, first_name:str, last_name:str) -> User:
        """Inserts a new User to the database.

        Args:
            username (str): username of the user
            password (str): password of the user
            password_again (str): re-enter of the password (similarity check)
            first_name (str): first name of the user
            last_name (str): last name of the user

        Raises:
            CredentialsError: if username, password or either of the names are not in valid form, or if passwords do not match

        Returns:
            User: the User object created
        """
        created_user = User(0, username, first_name, last_name)
        if self.username_exists(username):
            raise CredentialsError("username already exists")
        try:
            Helper.is_valid_password(password)
        except ValueError as e:
            raise CredentialsError(f"password not valid form:\n{str(e)}") from e
        if password != password_again:
            raise CredentialsError("passwords do not match")
        insert_new_user_successful = self.__user_dbao.insert_new_user(username, password, first_name, last_name)
        if not insert_new_user_successful:
            raise MemoryError("Registration not succesful")
        user_id = self.__user_dbao.find_user_by_username(username)[0]
        if not user_id:
            raise MemoryError("database encoutered an error")
        created_user.set_user_id(user_id)
        self.__users[user_id] = created_user
        return created_user
    
    def forget_users(self):
        self.__users:dict(User) = {}

    def username_exists(self, username:str) -> bool:
        """Check if a given username exists in the database

        Args:
            username (str): Users username that is wanted to be tested

        Returns:
            bool: Boolean value representing the existence fo the username
        """
        result = self.__user_dbao.find_user_by_username(username)
        if result:
            return True
        return False

    def get_user_by_username(self, username:str) -> User:
        """Get the User-object of user by username

        Args:
            username (str): username of the User

        Returns:
            User: An User-object of the user
        """
        user = None
        for usr in self.__users.values():
            if usr.username == username:
                user = usr
        if not user:
            user_id, username, first_name, last_name = \
                self.__user_dbao.find_user_by_username(username)
            user = User(user_id, username, first_name, last_name)
            self.__users[user.user_id] = user
        return user

    def get_users_by_user_id_list(self, user_ids:list("int")) -> list("User"):
        """Get the User-objects of users by their user_id's provided as a list

        Args:
            user_ids (list("int")): list of user_id's

        Returns:
            list("User"): a list of User-objects in the same order as the id's came in
        """
        not_in_users = [usr_id for usr_id in user_ids if usr_id not in self.__users]
        user_infos = self.__user_dbao.find_users_by_user_id_list(not_in_users)
        self.__users.update({user[0] : User(*user) for user in user_infos})
        return [self.__users[usr_id] for usr_id in user_ids]

    def username_password_match(self, username:str, inserted_password:str) -> bool:
        """Check if a given username and password are a match

        Args:
            username (str): username of supposed user
            inserted_password (str): password of supposed user

        Returns:
            bool: A boolean value representing the match of the username and password
        """
        if not self.username_exists(username):
            return False
        username, password = self.__user_dbao.find_password_by_username(username)
        return (username, inserted_password) == (username, password)
