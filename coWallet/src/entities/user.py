from utils.helper import Helper
from utils.error import CredentialsError

class User:
    """Class representing a User
    """

    def __init__(self, user_id:int, username:str, first_name:str, last_name:str):
        """Constructor of a User-object

        Args:
            user_id (int): id of the user
            username (str): username of the user
            first_name (str): first name of the user
            last_name (str): last name of the user
        """
        self.__user_id = self.check_id_valid(user_id)
        self.__first_name = self.check_first_name_valid(first_name)
        self.__last_name = self.check_last_name_valid(last_name)
        self.__username = self.check_username_valid(username)
        self.__balance = 0

    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def username(self) -> str:
        return self.__username

    @property
    def first_name(self) -> str:
        return self.__first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @property
    def balance(self) -> int:
        return self.__balance

    @staticmethod
    def check_id_valid(id_value:int) -> int:
        """Check the validity of a id number

        Args:
            id_value (int): id_value candidate

        Raises:
            CredentialsError: when is not valid

        Returns:
            int: return the same id number if it is valid
        """
        try:
            Helper.is_valid_id(id_value)
            return id_value
        except ValueError as e:
            raise CredentialsError(f"id_value is not valid:\n{str(e)}") from e

    @staticmethod
    def check_username_valid(username:str) -> str:
        """Check the validity of a username

        Args:
            username (str): username candidate

        Raises:
            CredentialsError: when is not valid

        Returns:
            str: return the same username if it is valid
        """
        try:
            Helper.is_valid_username(username)
            return username
        except ValueError as e:
            raise CredentialsError(f"username is not valid form:\n{str(e)}") from e

    @staticmethod
    def check_first_name_valid(first_name:str) -> str:
        """Check the validity of a first name

        Args:
            first_name (str): first name candidate

        Raises:
            CredentialsError: when is not valid

        Returns:
            str: return the same first_name if it is valid
        """
        try:
            Helper.is_valid_name(first_name)
            return first_name
        except ValueError as e:
            raise CredentialsError(f"first name is not valid form:\n{str(e)}") from e

    @staticmethod
    def check_last_name_valid(last_name:str) -> str:
        """Check the validity of a last name

        Args:
            last_name (str): last name candidate

        Raises:
            CredentialsError: when is not valid

        Returns:
            str: return the same last_name if it is valid
        """
        try:
            Helper.is_valid_name(last_name)
            return last_name
        except ValueError as e:
            raise CredentialsError(f"last name is not valid form:\n{str(e)}") from e

    def set_user_id(self, user_id:int):
        """method for resetting the user_id (used in register process)

        Args:
            user_id (int): user_id of the User
        """
        self.__user_id = self.check_id_valid(user_id)

    def __str__(self) -> str:
        """Returns a short string representation of the User object

        Returns:
            str: Users first name and last name in a str-object
        """
        return f"{self.__first_name} {self.__last_name}"

    def __repr__(self) -> str:
        """Returns a longer string representation of the User object

        Returns:
            str: User id, last name, first name and username in a str-object
        """
        return f"User({self.user_id}, {repr(self.last_name)} ,{repr(self.first_name)}, {repr(self.username)})"

    def __hash__(self) -> int:
        return self.user_id

    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.user_id == other.user_id
        return False

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, User):
            raise TypeError(f"'<' not supported between instances of '{type(self).__name__}' and '{type(other).__name__}'")
        if self.last_name < other.last_name:
            return True
        elif self.last_name > other.last_name:
            return False
        if self.first_name < other.first_name:
            return True
        elif self.first_name > other.first_name:
            return False
        if self.username < other.username:
            return True
        elif self.username > other.username:
            return False
        if self.user_id < other.user_id:
            return True
        else:
            return False
