class User:

    def __init__(self, user_id:int, username:str, password:str, first_name:str, last_name:str):
        self.__user_id = user_id
        self.__username = username
        self.__password = password
        self.__first_name = first_name
        self.__last_name = last_name
    
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
    
    def isValidPassword(self, tryPassword: str):
        return tryPassword == self.__password