from sqlite3 import IntegrityError
from dbaos.dbao import Dbao

class CliqueDbao(Dbao):

    def __init__(self, db_type:str = None, db_path:str = None):
        super().__init__(db_type, db_path)
        self.check_db()

    def check_db(self):
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
                clique_id INTEGER NOT NULL REFERENCES Clique(id)
            )
        """
        self.db.execute("BEGIN")
        self.db.execute(query_create_clique_table)
        self.db.execute(query_create_clique_member_table)
        self.db.execute("COMMIT")

    def insert_new_clique(self, clique_name:str, description:str, head_id:int) -> bool:
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

    def find_cliques_by_head_id(self, head_id:int) -> list:
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
