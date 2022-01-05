# from typing import List

# from entities.clique import Clique
# from entities.user import User
# from repositories.clique_repository import CliqueRepository

# class CliqueService:
#     """The Application logic regarding the Clique-objects
#     """

#     def __init__(self, db_type:str = None, db_path:str = None):
#         """Constructor of CliqueService class

#         Args:
#             db_type (str, optional): Where to save db-file, either 'sqlite3_in_memory' or
#                 'sqlite3_file'. Defaults to 'sqlite3_file' (from config.py).

#             db_path (str, optional): path where to save db-file. When
#                 db_type == 'sqlite3_in_memory', then has no effect.
#                 Defaults to "data/data.db" (from config.py).
#         """
#         self.__clique_repository = CliqueRepository(db_type, db_path)
#         self.my_cliques = []

#     def disconnect_db(self):
#         """Closes the connection to the database.
#             Essential for 'sqlite3_in_memory' testing
#             in order to discard the database file.

#         Raises:
#             ConnectionError: If disconnection to database
#                 encounters an unexpected error
#         """
#         self.__clique_repository.disconnect_db()

#     def create_clique(self, clique_name:str, description:str, head_user:User) -> Clique:
#         """Create a new clique for the application

#         Args:
#             clique_name (str): name of the clique
#             description (str): description of the clique
#             head_id (int): User creating the clique

#         Raises:
#             CredentialsError: If clique_name, description or head_user id are not valid form

#         Returns:
#             Clique: created Clique object
#         """
#         created_clique = Clique(0, clique_name, description, head_user)
#         clique_id = self.__clique_repository.insert_new_clique(created_clique)
#         if not clique_id:
#             raise MemoryError("database encoutered an error")
#         created_clique.set_clique_id(clique_id)
#         self.my_cliques.append(created_clique)
#         return created_clique

#     def insert_new_member(self, clique:Clique, new_member:User) -> bool:
#         """Insert a new member into a given Clique

#         Args:
#             clique (Clique): the Clique where to add the user
#             new_member (User):  the User to add to the clique

#         Returns:
#             bool: Boolean value representing the success of the insert operation
#         """
#         return self.__clique_repository.insert_new_member(clique, new_member)

#     def get_cliques_by_head(self, head_user:User) -> List[Clique]:
#         """Get all cliques that the user has created

#         Args:
#             head_user (User): the owner User of the Clique

#         Returns:
#             List[Clique]: list of Clique-objects
#         """
#         return self.__clique_repository.get_cliques_by_head_id(head_user)

#     # def get_latest_clique_by_head(self, head_id:int) -> Clique:
#     #     """Get the latest clique that user has created

#     #     Args:
#     #         head_id (int): user_id of the owner

#     #     Returns:
#     #         Clique: matching Clique-object
#     #     """
#     #     return self.__clique_repository.get_latest_clique_by_head_id(head_id)

#     def get_cliques_by_member(self, member:User) -> List[Clique]:
#         """Get all the Clique-objects that a User is a member of

#         Args:
#             member (User): the User who is an alleged member of some Cliques

#         Returns:
#             List[Clique]: List of Clique-objects that the User is a member of
#         """
#         cliques = self.__clique_repository.get_cliques_by_member(member)
#         #print(cliques)
#         return cliques

#     def get_clique_personal_balance(self, user_id:int, clique_id:int) -> int:
#         """Calculate the current personal balance in a clique

#         Args:
#             user_id (int): user_id of a User
#             clique_id (int): clique_id of a Clique

#         Returns:
#             int: amount of personal balance in a clique
#         """
#         # Jatka toimintoa myöhemmin!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#         return 0

#     def update_my_cliques(self):
#         """updates the state of my cliques
#         """
#         #Tänne klikkien päivitystoiminto
#         pass
