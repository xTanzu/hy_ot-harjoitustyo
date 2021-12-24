from entities.user import User
from repositories.user_repository import UserRepository
from utils.helper import Helper
from utils.error import CredentialsError

class UserService:
    """The Application logic regarding the User-objects
    """

    def __init__(self, db_type:str = None, db_path:str = None):
        """Constructor of UserService class

        Args:
            db_type (str, optional): Where to save db-file, either 'sqlite3_in_memory' or
                'sqlite3_file'. Defaults to 'sqlite3_file' (from config.py).

            db_path (str, optional): path where to save db-file. When
                db_type == 'sqlite3_in_memory', then has no effect.
                Defaults to "data/data.db" (from config.py).
        """
        self.__user_repository = UserRepository(db_type, db_path)
        self.__user = None

    def disconnect_db(self):
        """Closes the connection to the database.
            Essential for 'sqlite3_in_memory' testing
            in order to discard the database file.

        Raises:
            ConnectionError: If disconnection to database
                encounters an unexpected error
        """
        self.__user_repository.disconnect_db()

    def create_user(self, username:str, password:str, password_again:str, first_name:str, last_name:str) -> bool:
        """Create a new user for the application

        Args:
            username (str): username of the user
            password (str): password of the user
            password_again (str): re-enter of the password (similarity check)
            first_name (str): first name of the user
            last_name (str): last name of the user

        Raises:
            CredentialsError: if username, password or either of the names are not in correct form

        Returns:
            bool: Boolean value representing the success of the create operation
        """
        self.__user = User(0, username, first_name, last_name)
        if self.__user_repository.username_exists(username):
            raise CredentialsError("username already exists")
        if not Helper.is_valid_password(password):
            raise CredentialsError("password not valid form")
        if password != password_again:
            raise CredentialsError("passwords do not match")
        user_id = self.__user_repository.insert_new_user(self.__user, password)
        if not user_id:
            self.__user = None
            raise MemoryError("database encoutered an error")
        self.__user.set_user_id(user_id)
        return True

    def login(self, username:str, password:str) -> bool:
        """Log a user in to the application

        Args:
            username (str): username of the User
            password (str): password of the user

        Returns:
            bool: Boolean value representing the success of the login operation
        """
        if self.__user_repository.username_password_match(username, password):
            self.__user = self.__user_repository.get_user_by_username(username)
            return True
        return False

    def get_current_user(self) -> User:
        """Get the currently logged in user

        Returns:
            User: currently logged in User-object
        """
        return self.__user

    def username_available(self, username:str) -> bool:
        """Check if a given username in not taken by a User

        Args:
            username (str): username that is wanted to checked

        Returns:
            bool: Boolean value representing the availability of the username
                False also if not correct form
        """
        username = User.check_username_valid(username)
        return not self.__user_repository.username_exists(username)

    def logout(self):
        """Log the currently logged in user out of the application
        """
        self.__user = None
