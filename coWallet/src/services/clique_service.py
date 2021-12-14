from typing import List

from entities.clique import Clique
from repositories.clique_repository import CliqueRepository

class CliqueService:
    """The Application logic regarding the Clique-objects
    """

    def __init__(self, db_type:str = None, db_path:str = None):
        """Constructor of CliqueService class

        Args:
            db_type (str, optional): Where to save db-file, either 'sqlite3_in_memory' or
                'sqlite3_file'. Defaults to 'sqlite3_file' (from config.py).

            db_path (str, optional): path where to save db-file. When
                db_type == 'sqlite3_in_memory', then has no effect.
                Defaults to "data/data.db" (from config.py).
        """
        self.__clique_repository = CliqueRepository(db_type, db_path)

    def disconnect_db(self):
        """Closes the connection to the database.
            Essential for 'sqlite3_in_memory' testing
            in order to discard the database file.

        Raises:
            ConnectionError: If disconnection to database
                encounters an unexpected error
        """
        self.__clique_repository.disconnect_db()

    def create_clique(self, clique_name:str, description:str, head_id:int) -> bool:
        """Create a new clique for the application

        Args:
            clique_name (str): name of the clique
            description (str): description of the clique
            head_id (int): user_id of the User creating the clique

        Returns:
            bool: Boolean value representing the success of the insert operation
        """
        return self.__clique_repository.insert_new_clique(clique_name, description, head_id)

    def get_cliques_by_head_id(self, head_id:int) -> List[Clique]:
        """Get all cliques that the user has created

        Args:
            head_id (int): user_id of the owner

        Returns:
            List[Clique]: list of Clique-objects
        """
        return self.__clique_repository.get_cliques_by_head_id(head_id)

    def get_latest_clique_by_head_id(self, head_id:int) -> Clique:
        """Get the latest clique that user has created

        Args:
            head_id (int): user_id of the owner

        Returns:
            Clique: matching Clique-object
        """
        return self.__clique_repository.get_latest_clique_by_head_id(head_id)

    def get_clique_personal_balance(self, user_id:int, clique_id:int) -> int:
        """Calculate the current personal balance in a clique

        Args:
            user_id (int): user_id of a User
            clique_id (int): clique_id of a Clique

        Returns:
            int: amount of personal balance in a clique
        """
        # Jatka toimintoa myöhemmin!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        return 0
