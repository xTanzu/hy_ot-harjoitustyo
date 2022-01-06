from typing import List

from entities.clique import Clique
from entities.user import User
from dbaos.clique_dbao import CliqueDbao
from repositories.user_repository import UserRepository

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
        self.__cliques:dict(Clique) = {}

    def disconnect_db(self):
        """Closes the connection to the database.
            Essential for 'sqlite3_in_memory' testing
            in order to discard the database file.

        Raises:
            ConnectionError: If disconnection to database
                encounters an unexpected error
        """
        self.__clique_dbao.disconnect()

    def insert_new_clique(self, clique_name:str, description:str, head_user:User) -> Clique:
        """Insert new Clique to the database

        Args:
            clique_name (str): name of the clique
            description (str): description of the clique
            head_user (User): User creating the clique

        Raises:
            CredentialsError: If clique_name, description or head_user id are not valid form

        Returns:
            Clique: created Clique object
        """
        created_clique = Clique(0, clique_name, description, head_user)
        insert_new_clique_successful = self.__clique_dbao.insert_new_clique(clique_name, description, head_user.user_id)
        if not insert_new_clique_successful:
            raise MemoryError("Clique creation not succesful")
        clique_id = self.__clique_dbao.find_latest_clique_by_head_id(head_user.user_id)[0]
        if not clique_id:
            raise MemoryError("database encoutered an error")
        created_clique.set_clique_id(clique_id)
        insert_head_as_member_successful = self.insert_new_member(created_clique, head_user)
        if not insert_head_as_member_successful:
            self.__clique_dbao.remove_clique_by_id(clique_id)
            raise MemoryError("Clique creation not succesful")
        return created_clique

    def insert_new_member(self, clique:Clique, new_member:User) -> bool:
        """Insert a new member into a given Clique

        Args:
            clique (Clique): the Clique where to add the user
            new_member (User):  the User to add to the clique

        Returns:
            bool: Boolean value representing the success of the insert operation
        """
        insert_new_member_successful = self.__clique_dbao.insert_new_member(clique.clique_id, new_member.user_id)
        if not insert_new_member_successful:
            return False
        clique.insert_new_members(new_member)
        return True

    # def get_cliques_by_head(self, head_user:User) -> List[Clique]:
    #     """Get all cliques that the user has created

    #     Args:
    #         head_user (User): the owner User of the Clique

    #     Returns:
    #         List[Clique]: list of Clique-objects
    #     """
    #     cliques = self.__clique_dbao.find_cliques_by_head_id(head_user.user_id)
    #     return [Clique(*clique) for clique in cliques]

    def get_cliques_by_member(self, member:User, user_repo:UserRepository) -> List[Clique]:
        """Get all the Clique-objects that a User is a member of

        Args:
            member (User): the User who is an alleged member of some Cliques

        Returns:
            List[Clique]: List of Clique-objects that the User is a member of
        """
        # Hae klikkien tiedot dbaosta (Cli.id, Cli.clique_name, Cli.description, Cli.head_id)
        clique_infos:list("tuple") = self.__clique_dbao.find_cliques_by_member_id(member.user_id)
        # ota klikeistä vain id:t listaan
        clique_ids = [clq_info[0] for clq_info in clique_infos]
        # katso mitkä tiedot ei ole jo __cliques:ssa ja poista clique_infos:sta kaikki turha
        clique_infos = [clq_info for clq_info in clique_infos if clq_info[0] not in self.__cliques]
        # looppaa jokainen dbaosta haettava tietue läpi
        for clq_info in clique_infos:
            # hae kaikki klikkiin kuuluvien user_id:t clique_dbaosta
            clique_id = clq_info[0]
            clique_name = clq_info[1]
            description = clq_info[2]
            head_user_id = clq_info[3]
            member_id_list = self.__clique_dbao.find_clique_member_list_by_id(clique_id)
            # hae näitä vastaavat User-objektit user_reposta niin että head_user on ekana
            members = user_repo.get_users_by_user_id_list([head_user_id] + member_id_list)
            head_user = members[0]
            members = members[1:]
            # rakenna näillä tiedoilla klikki olio
            clique = Clique(clique_id, clique_name, description, head_user)
            # aseta nämä käyttäjät klikin jäsenlistaan
            clique.insert_new_members(*members)
            # lisää klikki __cliquesiin
            self.__cliques[clique.clique_id] = clique
        # palauta palautettavat nklikit
        return [self.__cliques[clq_id] for clq_id in clique_ids]
