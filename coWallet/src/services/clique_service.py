from typing import List

from entities.clique import Clique
from repositories.clique_repository import CliqueRepository

class CliqueService:

    def __init__(self, db_type:str = None, db_path:str = None):
        self.__clique_repository = CliqueRepository(db_type, db_path)

    def disconnect_db(self):
        self.__clique_repository.disconnect_db()

    def create_clique(self, clique_name:str, description:str, head_id:int) -> bool:
        return self.__clique_repository.insert_new_clique(clique_name, description, head_id)

    def get_cliques_by_head_id(self, head_id:int) -> List[Clique]:
        return self.__clique_repository.get_cliques_by_head_id(head_id)

    def get_latest_clique_by_head_id(self, head_id:int) -> Clique:
        return self.__clique_repository.get_latest_clique_by_head_id(head_id)
