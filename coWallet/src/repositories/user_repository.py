from entities.user import User
from dbaos.user_dbao import UserDbao

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

    def disconnect_db(self):
        """Closes the connection to the database.
            Essential for 'sqlite3_in_memory' testing
            in order to discard the database file.

        Raises:
            ConnectionError: If disconnection to database
                encounters an unexpected error
        """
        self.__user_dbao.disconnect()

    def insert_new_user(self, user:User, password:str) -> int:
        """Inserts a new User to the database.

        Args:
            user (User): User-object to be inserted
            password (str): Password of the user

        Returns:
            int: user_id of the inserted user
        """
        username = user.username
        first_name = user.first_name
        last_name = user.last_name
        successful = self.__user_dbao.insert_new_user(username, password, first_name, last_name)
        if not successful:
            return None
        user_id = self.__user_dbao.find_user_by_username(username)[0]
        return user_id

    def username_exists(self, inserted_username:str) -> bool:
        """Check if a given username exists in the database

        Args:
            inserted_username (str): Users username that is wanted to be tested

        Returns:
            bool: Boolean value representing the existence fo the username
        """
        result = self.__user_dbao.find_user_by_username(inserted_username)
        if result:
            return True
        return False

    def get_user_by_username(self, inserted_username:str) -> User:
        """Get the User-object of user by username

        Args:
            inserted_username (str): username of the User

        Returns:
            User: An User-object of the user
        """
        user_id, username, first_name, last_name = \
            self.__user_dbao.find_user_by_username(inserted_username)
        user = User(user_id, username, first_name, last_name)
        return user

    def username_password_match(self, inserted_username:str, inserted_password:str) -> bool:
        """Check if a given username and password are a match

        Args:
            inserted_username (str): username of supposed user
            inserted_password (str): password of supposed user

        Returns:
            bool: A boolean value representing the match of the username and password
        """
        if not self.username_exists(inserted_username):
            return False
        username, password = self.__user_dbao.find_password_by_username(inserted_username)
        return (inserted_username, inserted_password) == (username, password)
