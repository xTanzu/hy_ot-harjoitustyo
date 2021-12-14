from sqlite3 import IntegrityError
from dbaos.dbao import Dbao

class UserDbao(Dbao):
    """DataBase Access Object class for data relating to User objects.

    Args:
        Dbao: Inherits the Dbao-base class
    """

    def __init__(self, db_type:str = None, db_path:str = None):
        """Constructor of UserDbao class

        Args:
            db_type (str, optional): Where to save db-file, either 'sqlite3_in_memory' or
                'sqlite3_file'. Defaults to 'sqlite3_file' (from config.py).

            db_path (str, optional): path where to save db-file. When
                db_type == 'sqlite3_in_memory', then has no effect.
                Defaults to "data/data.db" (from config.py).
        """
        super().__init__(db_type, db_path)
        self.check_db()

    def check_db(self):
        """Check the database file for the existance of required tables.
            If they don't exist, creates them.
        """
        query = """
            CREATE TABLE IF NOT EXISTS User (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL
            );
        """
        self.db.execute(query, [])

    def insert_new_user(self, username:str, password:str, first_name:str, last_name:str) -> bool:
        """Inserts a new User to the database.

        Args:
            username (str): Name of the user
            password (str): Password of the user
            first_name (str): First name of the user
            last_name (str): Last name of the user

        Raises:
            ConnectionError: If encounters an unexpected error when inserting, insert aborted

        Returns:
            bool: Boolean value representing the success of the insert operation
        """
        query = """
            INSERT INTO User (
                username, password, first_name, last_name
            ) 
            VALUES (
                :username, :password, :first_name, :last_name
            );
        """
        insert_values = {"username": username, "password": password, \
        "first_name": first_name, "last_name": last_name}

        try:
            self.db.execute(query, insert_values)
        except IntegrityError as e:
            print(f"DB error: {e}")
            return False
        except Exception as e:
            raise ConnectionError(f"DB faced an error inserting user data: {e}") from e

        return True

    def find_user_by_username(self, username:str) -> tuple:
        """Find the information of a user from database by its username

        Args:
            username (str): Users username

        Returns:
            tuple: A tuple containing the information of the user
                (user_id, username, password, first_name, last_name)
        """
        query = """
            SELECT 
                id, username, first_name, last_name
            FROM 
                User
            WHERE
                username = :username
            ;
        """
        search_values = {"username": username}
        return self.db.execute(query, search_values).fetchone()

    def find_password_by_username(self, username:str) -> tuple:
        """Find the password of a user
            [Horrible way to verify a password]

        Args:
            username (str): The username of a user

        Returns:
            tuple: A tuple of username and corresponding password
                (username, password)
        """
        query = """
            SELECT 
                username, password
            FROM 
                User
            WHERE
                username = :username
            ;
        """
        search_values = {"username": username}
        return self.db.execute(query, search_values).fetchone()
