from typing import List

from entities.clique import Clique
from entities.user import User
from dbaos.clique_dbao import CliqueDbao

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

    def insert_new_clique(self, clique:Clique) -> int:
        """Insert new Clique to the database

        Args:
            clique (Clique): Clique-object to be inserted

        Returns:
            bool: Boolean value representing the success of the insert operation
        """
        if not clique:
            return None
        clique_name = clique.clique_name
        description = clique.description
        head_id = clique.head_user.user_id
        insert_new_clique_successful = self.__clique_dbao.insert_new_clique(clique_name, description, head_id)
        if not insert_new_clique_successful:
            return None
        clique_id = self.__clique_dbao.find_latest_clique_by_head_id(head_id)[0]
        insert_head_as_member_successful = self.__clique_dbao.insert_new_member(clique_id, head_id)
        if not insert_head_as_member_successful:
            self.__clique_dbao.remove_clique_by_id(clique_id)
            return None
        return clique_id

    def insert_new_member(self, clique:Clique, new_member:User) -> bool:
        """Insert a new member into a given Clique

        Args:
            clique (Clique): the Clique where to add the user
            new_member (User):  the User to add to the clique

        Returns:
            bool: Boolean value representing the success of the insert operation
        """
        return self.__clique_dbao.insert_new_member(clique.clique_id, new_member.user_id)

    def get_cliques_by_head(self, head_user:User) -> List[Clique]:
        """Get all cliques that the user has created

        Args:
            head_user (User): the owner User of the Clique

        Returns:
            List[Clique]: list of Clique-objects
        """
        cliques = self.__clique_dbao.find_cliques_by_head_id(head_user.user_id)
        return [Clique(*clique) for clique in cliques]

    # def get_latest_clique_by_head_id(self, head_id:int) -> Clique:
    #     """Get the users latest Clique-object that was inserted

    #     Args:
    #         head_id (int): user_id of the User

    #     Returns:
    #         Clique: The latest Clique-object
    #     """
    #     clique_info = self.__clique_dbao.find_latest_clique_by_head_id(head_id)
    #     if not clique_info:
    #         return None
    #     return Clique(*clique_info)

    def get_cliques_by_member(self, member:User) -> List[Clique]:
        """Get all the Clique-objects that a User is a member of

        Args:
            member (User): the User who is an alleged member of some Cliques

        Returns:
            List[Clique]: List of Clique-objects that the User is a member of
        """
        cliques = self.__clique_dbao.find_cliques_by_member_id(member.user_id)
        return [Clique(*clique) for clique in cliques]
