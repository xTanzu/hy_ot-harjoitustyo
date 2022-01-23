
from typing import List

from entities.clique import Clique
from entities.user import User
from dbaos.clique_dbao import CliqueDbao
from repositories.user_repository import UserRepository

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
        created_clique.set_clique_id(clique_id)
        insert_head_as_member_successful = self.insert_new_member(created_clique, head_user)
        if not insert_head_as_member_successful:
            self.__clique_dbao.remove_clique_by_id(clique_id)
            raise MemoryError("Clique creation not succesful")
        self.__cliques[clique_id] = created_clique
        return created_clique

    def forget_cliques(self):
        self.__cliques:dict(Clique) = {}

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

    def insert_new_transaction(self, timestamp:str, transaction_type:int, user:User, clique:Clique, amount:int) -> bool:
        """[summary]

        Args:
            timestamp (str): timestamp of the transaction
            transaction_type (str/int): transaction type as a str ('deposit'/'withdraw') or int (0/1)
            user (User): user-object associated with the transaction
            clique (Clique): clique-object associated with the transaction
            amount (int/float): amount of money moved in euro-cents as int

        Returns:
            bool: boolean value representing the success of the transaction
        """
        Helper.is_valid_timestamp(timestamp)
        transaction_type = Helper.convert_transaction_type(transaction_type)
        amount = Helper.convert_euro_to_cents(amount)
        return self.__clique_dbao.insert_new_transaction(timestamp, transaction_type, user.user_id, clique.clique_id, amount)

    def get_cliques_by_member(self, member:User, user_repo:UserRepository) -> List[Clique]:
        """Get all the Clique-objects that a User is a member of

        Args:
            member (User): the User who is an alleged member of some Cliques

        Returns:
            List[Clique]: List of Clique-objects that the User is a member of
        """
        clique_infos:list("tuple") = self.__clique_dbao.find_cliques_by_member_id(member.user_id)
        clique_ids = [clq_info[0] for clq_info in clique_infos]
        clique_infos = [clq_info for clq_info in clique_infos if clq_info[0] not in self.__cliques]
        for clq_info in clique_infos:
            clique_id = clq_info[0]
            clique_name = clq_info[1]
            description = clq_info[2]
            head_user_id = clq_info[3]
            member_id_list = self.__clique_dbao.find_clique_member_list_by_id(clique_id)
            members = user_repo.get_users_by_user_ids(*[head_user_id] + member_id_list)
            head_user = members[0]
            members = members[1:]
            clique = Clique(clique_id, clique_name, description, head_user)
            clique.insert_new_members(*members)
            self.__cliques[clique.clique_id] = clique
        return [self.__cliques[clq_id] for clq_id in clique_ids]

    def get_all_transactions_by_clique(self, clique:Clique, user_repo:UserRepository) -> List[tuple]:
        """get all transactions made in a clique

        Args:
            clique (Clique): the clique in which the transactions are made
            user_repo (UserRepository): UserRepository-object used

        Returns:
            list(tuple): list of transactions, where the information of the transactions is 
            displayed in a 4-tuple (timestamp, transaction-type, user associated with the 
            transaction, amount of transaction)
        """        
        transaction_info = self.__clique_dbao.find_all_transactions_by_clique_id(clique.clique_id)
        user_ids = set([transaction_nugget[2] for transaction_nugget in transaction_info])
        users = user_repo.get_users_by_user_ids(*user_ids)
        users_by_ids = {user.user_id : user for user in users}
        return [transaction_nugget[:2] + (users_by_ids[transaction_nugget[2]],) + transaction_nugget[3:] for transaction_nugget in transaction_info]
