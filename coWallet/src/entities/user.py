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
        self.__user_id = self.check_user_id_valid(user_id)
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
    def balance(self):
        return self.__balance

    @staticmethod
    def check_user_id_valid(user_id:int) -> int:
        """Check the validity of a user_id number

        Args:
            user_id (int): some user_id candidate

        Raises:
            CredentialsError: when is not valid

        Returns:
            int: return the same id number if it is valid
        """
        if not Helper.is_valid_id(user_id):
            raise CredentialsError("user_id is not valid")
        return user_id

    @staticmethod
    def check_username_valid(username:str) -> str:
        """Check the validity of a username

        Args:
            username (str): some username candidate

        Raises:
            CredentialsError: when is not valid

        Returns:
            str: return the same username if it is valid
        """
        if not Helper.is_valid_username(username):
            raise CredentialsError("username is not valid form")
        return username

    @staticmethod
    def check_first_name_valid(first_name:str) -> str:
        """Check the validity of a first name

        Args:
            first_name (str): some first name candidate

        Raises:
            CredentialsError: when is not valid

        Returns:
            str: return the same first_name if it is valid
        """
        if not Helper.is_valid_name(first_name):
            raise CredentialsError("first name is not valid form")
        return first_name

    @staticmethod
    def check_last_name_valid(last_name:str) -> str:
        """Check the validity of a last name

        Args:
            last_name (str): some last name candidate

        Raises:
            CredentialsError: when is not valid

        Returns:
            str: return the same last_name if it is valid
        """
        if not Helper.is_valid_name(last_name):
            raise CredentialsError("last name is not valid form")
        return last_name

    def set_user_id(self, user_id:int):
        """method for resetting the user_id (used in register process)

        Args:
            user_id (int): user_id of the User
        """
        self.__user_id = self.check_user_id_valid(user_id)

    def __str__(self) -> str:
        """Returns a short string representation of the User object

        Returns:
            str: Users first name and last name in a str-object
        """
        return f"{self.__first_name} {self.__last_name}"

    def __repr__(self) -> str:
        """Returns a longer string representation of the User object

        Returns:
            str: User id, username, first name and last name in a multi-line str-object
        """
        return f"""<User>:
            id: {self.__user_id},
            username: {self.__username},
            first_name: {self.__first_name},
            last_name: {self.__last_name}"""
