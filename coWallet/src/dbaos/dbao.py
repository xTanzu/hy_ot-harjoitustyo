import sqlite3
from config import DB_TYPE, DB_PATH

class Dbao:

    def __init__(self, db_type:str = None, db_path:str = None):
        self.__db_type = (db_type if (db_type and isinstance(db_type, str)) else DB_TYPE)
        self.__db_path = (db_path if (db_path and isinstance(db_path, str)) else DB_PATH)
        self.__db = self.connect()

    @property
    def db_type(self) -> str:
        return self.__db_type

    @property
    def db_path(self) -> str:
        return self.__db_path

    @property
    def db(self) -> sqlite3.Connection:
        return self.__db

    def connect(self) -> sqlite3.Connection:
        try:
            if self.__db_type == "sqlite3_in_memory":
                db = sqlite3.connect("file::memory:?cache=shared", uri=True)
            elif self.__db_type == "sqlite3_file":
                db = sqlite3.connect(self.__db_path)
            else:
                raise ValueError("desired db destination not recognized")
        except Exception as e:
            raise ConnectionError(f"{type(self).__name__}: connection to {self.__db_type}\
                {(' in ' + self.__db_path) if self.__db_type == 'sqlite3_file' else ''} failed")\
                from e

        db.isolation_level = None
        db.execute("PRAGMA foreign_keys = ON")
        #print(f"Sqlite version: {sqlite3.version}")
        print(f"{type(self).__name__}: Connected to: {self.__db_type}\
            {(' in ' + self.__db_path) if self.__db_type == 'sqlite3_file' else ''}")
        return db

    def disconnect(self):
        try:
            self.__db.close()
        except Exception as e:
            raise ConnectionError("Error closing connection to db") from e