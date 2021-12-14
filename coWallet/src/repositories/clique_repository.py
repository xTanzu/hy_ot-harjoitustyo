from typing import List

from entities.clique import Clique
from dbaos.clique_dbao import CliqueDbao
from utils.helper import Helper

class CliqueRepository:
    """Repository object for data relating to Clique objects.
        Combines the clique data from dbao and makes Clique-objects.
        Has some low level methods and checks.
    """

    def __init__(self, db_type:str = None, db_path:str = None):
        """Constructor of CliqueRepository class

        Args:
            db_type (str, optional): Where to save db-file, either 'sqlite3_in_memory' or
                'sqlite3_file'. Defaults to 'sqlite3_file' (from config.py).

            db_path (str, optional): path where to save db-file. When
                db_type == 'sqlite3_in_memory', then has no effect.
                Defaults to "data/data.db" (from config.py).
        """
        self.__clique_dbao = CliqueDbao(db_type, db_path)

    def disconnect_db(self):
        """Closes the connection to the database.
            Essential for 'sqlite3_in_memory' testing
            in order to discard the database file.

        Raises:
            ConnectionError: If disconnection to database
                encounters an unexpected error
        """
        self.__clique_dbao.disconnect()

    def insert_new_clique(self, clique_name:str, description:str, head_id:int) -> bool:
        """Inserts new Clique to the database

        Args:
            clique_name (str): name of the Clique
            description (str): description of the Clique
            head_id (int): user_id of the owner of the Clique. Must be an existing User

        Returns:
            bool: Boolean value representing the success of the insert operation
        """
        if Helper.is_valid_name(clique_name) and Helper.is_valid_short_text(description) \
            and isinstance(head_id, int):
            return self.__clique_dbao.insert_new_clique(clique_name, description, head_id)
        return False

    def get_cliques_by_head_id(self, head_id:int) -> List[Clique]:
        """Get all the the Clique-objects that belong to a User

        Args:
            head_id (int): user_id of the User that owns the Clique

        Returns:
            List[Clique]: List of Clique-objects
        """
        cliques = self.__clique_dbao.find_cliques_by_head_id(head_id)
        return [Clique(*clique) for clique in cliques]

    def get_latest_clique_by_head_id(self, head_id:int) -> Clique:
        """Get the users latest Clique-object that was inserted

        Args:
            head_id (int): username of the User

        Returns:
            Clique: The latest Clique-object
        """
        clique_info = self.__clique_dbao.find_latest_clique_by_head_id(head_id)
        if not clique_info:
            return None
        return Clique(*clique_info)
