class Clique:

    def __init__(self, clique_id:int, clique_name:str, description:str, head_id):
        self.__clique_id = clique_id
        self.__clique_name = clique_name
        self.__description = description
        self.__head_id = head_id

    @property
    def clique_id(self):
        return self.__clique_id

    @property
    def clique_name(self):
        return self.__clique_name

    @property
    def description(self):
        return self.__description

    @property
    def head_id(self):
        return self.__head_id

    def __str__(self) -> str:
        return f"{self.clique_name}: \
{self.description if len(self.description) <= 20 else (self.description[:18] + '...')}"

    def __repr__(self) -> str:
        return f"""<Clique-object>:
            id: {self.clique_id},
            name: {self.clique_name},
            description: {self.description[:100]},
            head_id: {self.head_id}
        """
