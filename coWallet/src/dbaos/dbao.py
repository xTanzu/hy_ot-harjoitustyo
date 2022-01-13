import sqlite3
from utils.config import DB_TYPE, DB_PATH

class Dbao:
    """DataBase Access Object base class,
        creates the basic functionality of a dbao.

    Attributes:
        __db_type: type of database
        __db_path: path to database file from root
        __db: database connection-object
    """

    def __init__(self, db_type:str = None, db_path:str = None):
        """Constructor of Dbao class

        Args:
            db_type (str, optional): Where to save db-file, either 'sqlite3_in_memory' or
                'sqlite3_file'. Defaults to 'sqlite3_file' (from config.py).

            db_path (str, optional): path where to save db-file. When
                db_type == 'sqlite3_in_memory', then has no effect.
                Defaults to "data/data.db" (from config.py).
        """
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
        """Connects Dbao to the Sqlite3 file using the sqlite3 library

        Raises:
            ValueError: If given db_type is not recognized
            ConnectionError: If connection to sqlite3 encounters
                an unexpected error (cannot proceed)

        Returns:
            sqlite3.Connection: sqlite3.Connection object holds
                a reference to the established connection to the database
        """
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
        """Closes the connection object to the database.
            Essential for 'sqlite3_in_memory' testing
            in order to discard the database file.

        Raises:
            ConnectionError: If disconnection of sqlite3 connection
                encounters an unexpected error
        """
        try:
            self.__db.close()
        except Exception as e:
            raise ConnectionError("Error closing connection to db") from e
