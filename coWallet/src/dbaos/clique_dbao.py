from sqlite3 import IntegrityError
from dbaos.dbao import Dbao

class CliqueDbao(Dbao):
    """DataBase Access Object class for data relating to Clique objects.

    Args:
        Dbao: Inherits the Dbao-base class
    """

    def __init__(self, db_type:str = None, db_path:str = None):
        """Constructor of CliqueDbao class

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
        query_create_clique_table = """
            CREATE TABLE IF NOT EXISTS Clique (
                id INTEGER PRIMARY KEY,
                clique_name TEXT NOT NULL,
                description TEXT,
                head_id INTEGER REFERENCES User(id)
            );
        """
        query_create_clique_member_table = """
            CREATE TABLE IF NOT EXISTS CliqueMember (
                id INTEGER PRIMARY KEY,
                user_id INTEGER NOT NULL REFERENCES User(id),
                clique_id INTEGER NOT NULL REFERENCES Clique(id),
                UNIQUE(user_id, clique_id)
            )
        """
        self.db.execute("BEGIN")
        self.db.execute(query_create_clique_table)
        self.db.execute(query_create_clique_member_table)
        self.db.execute("COMMIT")

    def insert_new_clique(self, clique_name:str, description:str, head_id:int) -> bool:
        """Inserts a new Clique to the database.

        Args:
            clique_name (str): Name of Clique object
            description (str): Description of Clique object
            head_id (int): user_id of the owner of the Clique object. Must be an existing User

        Raises:
            ConnectionError: If encounters an unexpected error when inserting, insert aborted

        Returns:
            bool: Boolean value representing the success of the insert operation
        """
        query_insert_new_clique = """
            INSERT INTO Clique(
                clique_name, description, head_id
            )
            VALUES (
                :clique_name, :description, :head_id
            );
        """
        query_values = {"clique_name": clique_name, "description":description, "head_id":head_id}

        try:
            self.db.execute(query_insert_new_clique, query_values)
        except IntegrityError as e:
            print(f"DB error: {e}")
            return False
        except Exception as e:
            raise ConnectionError(f"DB faced an error inserting clique data: {e}") from e

        return True

    def insert_new_member(self, clique_id:int, user_id:int) -> bool:
        """Insert a new member into the database under a given Clique

        Args:
            clique_id (int): clique_id of the Clique where to add the user
            user_id (int): user_id of the user to add to the Clique

        Returns:
            bool: Boolean value representing the success of the insert operation
        """
        query_insert_new_member = """
            INSERT INTO CliqueMember(
                user_id, clique_id
            )
            VALUES(
                :user_id, :clique_id
            );
        """
        query_values = {"user_id": user_id, "clique_id": clique_id}

        try:
            self.db.execute(query_insert_new_member, query_values)
        except IntegrityError as e:
            print(f"clique_id: {clique_id}, user_id: {user_id}")
            print(f"DB error: {e}")
            return False
        except Exception as e:
            raise ConnectionError(f"DB faced an error inserting clique data: {e}") from e
        
        return True

    def remove_clique_by_id(self, clique_id:int) -> bool:
        """Remove all data of a clique

        Args:
            clique_id (int): clique_id of the clique to be removed

        Raises:
            ConnectionError: If database encounters an unexpected error when deleting data, delete aborted

        Returns:
            bool: Boolean value representing the success of the delete operation
        """        
        query_remove_clique_members = """
            DELETE FROM
                CliqueMember
            WHERE
                clique_id=:clique_id
            ;
        """
        query_remove_clique = """
            DELETE FROM
                Clique
            WHERE
                id=:clique_id
            ;
        """
        query_values = {"clique_id": clique_id}

        try:
            self.db.execute("BEGIN")
            self.db.execute(query_remove_clique_members, query_values)
            self.db.execute(query_remove_clique, query_values)
            self.db.execute("COMMIT")
        except IntegrityError as e:
            print(f"DB error: {e}")
            return False
        except Exception as e:
            raise ConnectionError(f"DB faced an error removing clique data: {e}") from e

        return True

    def find_cliques_by_head_id(self, head_id:int) -> list('tuple'):
        """Find the information of all Cliques that belong to a User
            from database using the user_id of the owner.

        Args:
            head_id (int): user_id of the owner of the Clique

        Returns:
            list(tuple): List of tuples containing Clique information
                [(clique_id, clique_name, description, head_id),(-,-,-,-),...]
        """
        query_find_cliques_by_head_id = """
            SELECT 
                *
            FROM 
                Clique 
            WHERE 
                head_id=:head_id
            ;
        """
        query_values = {"head_id": head_id}
        result = self.db.execute(query_find_cliques_by_head_id, query_values)
        return result.fetchall()

    def find_latest_clique_by_head_id(self, head_id:int) -> tuple:
        """Find the information of the latest inserted Clique that belong to a User

        Args:
            head_id (int): user_id of the owner of the Clique

        Returns:
            tuple: A tuple containing Clique information in form
                (clique_id, clique_name, description, head_id)
        """
        query_find_latest_clique_by_head_id = """
            SELECT 
                * 
            FROM 
                Clique 
            WHERE 
                head_id=:head_id 
            ORDER BY 
                id DESC
            ;
        """
        query_values = {"head_id": head_id}
        result = self.db.execute(query_find_latest_clique_by_head_id, query_values)
        return result.fetchone()

    def find_cliques_by_member_id(self, user_id:int) -> list('tuple'):
        """Find the information of all cliques that a User is a member of
            from the database using the user_id.

        Args:
            user_id (int): the user_id of the User whos cliques are looked for
        """
        query_find_cliques_by_member_id = """
            SELECT 
                Cli.id, Cli.clique_name, Cli.description, Cli.head_id 
            FROM 
                CliqueMember CliMem, Clique Cli 
            WHERE 
                CliMem.user_id=:user_id 
                and CliMem.clique_id=Cli.id
            ;
        """
        query_values = {"user_id": user_id}
        return self.db.execute(query_find_cliques_by_member_id, query_values).fetchall()

    def find_clique_member_list_by_id(self, clique_id:int) -> list('int'):
        """Find all user_id's of the members of a clique

        Args:
            clique_id (int): the clique_id of the Clique in question
        
        Returns:
            list(int): List of the members user_id's
        """        
        query_find_clique_member_list_by_id = """
            SELECT DISTINCT 
                user_id 
            FROM 
                CliqueMember 
            WHERE 
                clique_id=:clique_id 
            ORDER BY 
                user_id
            ;
        """
        query_values = {"clique_id": clique_id}
        result = self.db.execute(query_find_clique_member_list_by_id, query_values)
        return [val[0] for val in result]
