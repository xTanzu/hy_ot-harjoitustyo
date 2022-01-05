from entities.user import User
from utils.error import CredentialsError
from utils.helper import Helper

class Clique:
    """Class representing a clique, a group of Users
    """

    def __init__(self, clique_id:int, clique_name:str, description:str, head_user:User):
        """Constructor of a Clique-object

        Args:
            clique_id (int): id # of the clique
            clique_name (str): name of the clique
            description (str): description of the clique
            head_user (User): the owner User of the Clique
        """
        self.__clique_id = self.check_id_valid(clique_id)
        self.__clique_name = self.check_clique_name_valid(clique_name)
        self.__description = self.check_description_valid(description)
        self.__head_user = head_user
        self.__members = set()

    @property
    def clique_id(self) -> int:
        return self.__clique_id

    @property
    def clique_name(self) -> str:
        return self.__clique_name

    @property
    def description(self) -> str:
        return self.__description

    @property
    def head_user(self) -> User:
        return self.__head_user

    @property
    def members(self) -> list:
        return list(self.__members)

    @staticmethod
    def check_id_valid(id_value:int) -> int:
        """Check the validity of a id number

        Args:
            id_value (int): id_value candidate

        Raises:
            CredentialsError: when is not valid

        Returns:
            int: return the same id_value if it is valid
        """
        try:
            Helper.is_valid_id(id_value)
            return id_value
        except ValueError as e:
            raise CredentialsError(f"id_value not valid:\n{str(e)}") from e

    @staticmethod
    def check_clique_name_valid(clique_name:str) -> str:
        """Check the validity of a clique_name

        Args:
            clique_name (str): clique_name candidate

        Raises:
            CredentialsError: when is not valid

        Returns:
            str: return the same clique_name if it is valid
        """        
        try:
            Helper.is_valid_name(clique_name)
            return clique_name
        except ValueError as e:
            raise CredentialsError(f"clique_name not valid form:\n{str(e)}") from e

    @staticmethod
    def check_description_valid(description:str) -> str:
        """Check the validity of a clique description

        Args:
            description (str): description candidate

        Raises:
            CredentialsError: whe is not valid

        Returns:
            str: return the same description if it is valid
        """        
        try:
            Helper.is_valid_short_text(description)
            return description
        except ValueError as e:
            raise CredentialsError(f"description not valid form:\n{str(e)}") from e

    def set_clique_id(self, clique_id:int):
        """method for resetting the clique_id (used in create clique process)

        Args:
            clique_id (int): clique_id of the Clique
        """
        self.__clique_id = self.check_id_valid(clique_id)

    def insert_new_member(self, new_member:User):
        """Inserts a new member in the Clique object

        Args:
            new_member (User): the User object to insert as new member
        """        
        self.__members.add(new_member)

    def __str__(self) -> str:
        """Returns a short string representation of the Clique object

        Returns:
            str: Clique name and description in a str-object
        """
        return f"{self.clique_name if len(self.clique_name)<=20 else self.clique_name[:18]+'...'}\
: {self.description if len(self.description) <= 20 else (self.description[:18] + '...')}"

    def __repr__(self) -> str:
        """Returns a longer string representation of the Clique object

        Returns:
            str: Clique id, name, description and head_user in a multi-line str-object
        """
        return f"""<Clique-object>:
            id: {self.clique_id},
            name: {self.clique_name},
            description: {self.description[:100]},
            head_user: {self.head_user}
        """

    def __hash__(self) -> int:
        return self.clique_id

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Clique):
            return self.clique_id == other.clique_id
        return False

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Clique):
            raise TypeError(f"'<' not supported between instances of '{type(self).__name__}' and '{type(other).__name__}'")
        if self.clique_name < other.clique_name:
            return True
        elif self.clique_name > other.clique_name:
            return False
        if self.description < other.description:
            return True
        elif self.description > other.description:
            return False
        if self.head_user < other.head_user:
            return True
        elif self.head_user > other.head_user:
            return False
        if self.clique_id < other.clique_id:
            return True
        else:
            return False
