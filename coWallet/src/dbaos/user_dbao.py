from sqlite3 import IntegrityError
from dbaos.dbao import Dbao

class UserDbao(Dbao):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.check_db()

    def check_db(self):
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
