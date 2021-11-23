from repositories.user_repository import User_Repository

class User_Service:

    def __init__(self):
        self.user = None
    
    def login(self, username:str, password:str) -> bool:
        pass