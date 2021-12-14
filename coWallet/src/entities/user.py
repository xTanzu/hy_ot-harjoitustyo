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
        self.__user_id = user_id
        self.__username = username
        self.__first_name = first_name
        self.__last_name = last_name
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
