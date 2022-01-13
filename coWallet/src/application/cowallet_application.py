from typing import List

from entities.user import User
from entities.clique import Clique
from repositories.user_repository import UserRepository
from repositories.clique_repository import CliqueRepository

class CoWalletApplication:
    """coWallet application logic
    """

    def __init__(self, db_type:str = None, db_path:str = None):
        """Constructor of CoWalletApplication class

        Args:
            db_type (str, optional): Where to save db-file, either 'sqlite3_in_memory' or
                'sqlite3_file'. Defaults to 'sqlite3_file' (from config.py).

            db_path (str, optional): path where to save db-file. When
                db_type == 'sqlite3_in_memory', then has no effect.
                Defaults to "data/data.db" (from config.py).
        """
        self.__user_repository = UserRepository(db_type, db_path)
        self.__clique_repository = CliqueRepository(db_type, db_path)
        self.__user = None
        self.__mbr_cliques = set()

    def disconnect_db(self):
        """Closes the connection to the database.
            Essential for 'sqlite3_in_memory' testing
            in order to discard the database file.

        Raises:
            ConnectionError: If disconnection to database
                encounters an unexpected error
        """
        self.__user_repository.disconnect_db()
        self.__clique_repository.disconnect_db()

    # User related things -------------------------------------------------------------------------

    def create_user(self, username:str, password:str, password_again:str, first_name:str, last_name:str) -> User:
        """Create a new user for the application

        Args:
            username (str): username of the user
            password (str): password of the user
            password_again (str): re-enter of the password (similarity check)
            first_name (str): first name of the user
            last_name (str): last name of the user

        Raises:
            CredentialsError: if username, password or either of the names are not in valid form, or if passwords do not match

        Returns:
            User: the User object created
        """
        self.__user = self.__user_repository.insert_new_user(username, password, password_again, first_name, last_name)
        return self.__user

    def login(self, username:str, password:str) -> bool:
        """Log a user in to the application

        Args:
            username (str): username of the User
            password (str): password of the user

        Returns:
            bool: Boolean value representing the success of the login operation
        """
        if not self.__user_repository.username_password_match(username, password):
            return False
        self.__user = self.__user_repository.get_user_by_username(username)
        return True

    def get_current_user(self) -> User:
        """Get the currently logged in user

        Returns:
            User: currently logged in User-object
        """
        return self.__user

    def username_available(self, username:str) -> bool:
        """Check if a given username in not taken by a User

        Args:
            username (str): username that is wanted to checked

        Returns:
            bool: Boolean value representing the availability of the username
                False also if not correct form
        """
        username = User.check_username_valid(username)
        return not self.__user_repository.username_exists(username)

    def logout(self):
        """Log the currently logged in user out of the application
        """
        self.__user = None
        self.__mbr_cliques = set()
        self.__user_repository.forget_users()
        self.__clique_repository.forget_cliques()

    # Clique related things -----------------------------------------------------------------------

    def create_clique(self, clique_name:str, description:str) -> Clique:
        """Create a new clique for the application

        Args:
            clique_name (str): name of the clique
            description (str): description of the clique

        Raises:
            CredentialsError: If clique_name, description or head_user id are not valid form

        Returns:
            Clique: created Clique object
        """
        created_clique = self.__clique_repository.insert_new_clique(clique_name, description, self.__user)
        self.__mbr_cliques.add(created_clique)
        return created_clique

    def insert_new_member(self, clique:Clique, new_member:User) -> bool:
        """Insert a new member into a given Clique

        Args:
            clique (Clique): the Clique where to add the user
            new_member (User):  the User to add to the clique

        Returns:
            bool: Boolean value representing the success of the insert operation
        """
        return self.__clique_repository.insert_new_member(clique, new_member)

    def get_mbr_cliques(self, update=False) -> List[Clique]:      
        """Get all the Clique-objects that the logged in User is a member of

        Args:
            update (bool, optional): Set to True if want to update existing cliques. Defaults to False.

        Returns:
            List[Clique]: List of Clique-objects that the User is a member of
        """
        if update:
            self.__mbr_cliques = set()
            self.__clique_repository.forget_cliques()
        self.__mbr_cliques.update(self.__clique_repository.get_cliques_by_member(self.__user, self.__user_repository))
        return list(self.__mbr_cliques)

    def get_personal_clique_data(self, clique:Clique) -> tuple:
        """Calculate the current users current personal balance in a clique

        Args:
            clique (Clique): Clique whose balance to get

        Returns:
            int: amount of personal balance in a clique
        """
        # Jatka toimintoa myöhemmin!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        return 0.0, 0.0, 0.0, 0.0
