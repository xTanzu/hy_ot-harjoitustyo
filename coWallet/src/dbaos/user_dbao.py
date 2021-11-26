import sqlite3
from config import DB_TYPE, DB_PATH

class UserDbao:

    def __init__(self, db_type:str = None, db_path:str = None):
        self.__db_type = (db_type if (db_type and isinstance(db_type, str)) else DB_TYPE)
        self.__db_path = (db_path if (db_path and isinstance(db_path, str)) else DB_PATH)
        self.__db = self.connect()
        self.check_db()

    @property
    def db_type(self) -> str:
        return self.__db_type

    @property
    def db_path(self) -> str:
        return self.__db_path

    def connect(self) -> object:
        if self.__db_type[0:7] == "sqlite3":
            if self.__db_type == "sqlite3_in_memory":
                self.__db_path = ":memory:"
            if self.__db_type in ("sqlite3_in_memory", "sqlite3_file"):
                try:
                    db = sqlite3.connect(self.__db_path)
                except Exception as e:
                    raise ConnectionError("connection to db not succesful") from e
            else:
                raise ValueError("desired sqlite3 db destination not recognized")
            db.isolation_level = None
            print(sqlite3.version)
            print(f"Connected to: {self.__db_type}, path: {self.__db_path}")
            return db
        raise ValueError("desired DB type not recognized")

    def check_db(self):
        query = """
            CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL
        );"""
        self.__db.execute(query, [])

    def insert_new_user(self, username:str, password:str, first_name:str, last_name:str) -> bool:
        query = """
            INSERT INTO Users (
                username, password, first_name, last_name
            ) 
            VALUES (
                :username, :password, :first_name, :last_name
            );
        """
        insert_values = {"username": username, "password": password, \
        "first_name": first_name, "last_name": last_name}

        try:
            self.__db.execute(query, insert_values)
        except sqlite3.IntegrityError as e:
            print(f"DB error: {e}")
            return False

        return True

    def find_user_by_username(self, username:str) -> tuple:
        query = """
            SELECT 
                id, username, first_name, last_name
            FROM 
                Users
            WHERE
                username = :username
            ;
        """
        search_values = {"username": username}
        return self.__db.execute(query, search_values).fetchone()

    def find_password_by_username(self, username:str) -> tuple:
        query = """
            SELECT 
                username, password
            FROM 
                Users
            WHERE
                username = :username
            ;
        """
        search_values = {"username": username}
        return self.__db.execute(query, search_values).fetchone()
