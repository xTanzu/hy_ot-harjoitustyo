from typing import List

from entities.clique import Clique
from dbaos.clique_dbao import CliqueDbao
from utils.helper import Helper

class CliqueRepository:

    def __init__(self, db_type:str = None, db_path:str = None):
        self.__clique_dbao = CliqueDbao(db_type, db_path)

    def disconnect_db(self):
        self.__clique_dbao.disconnect()

    def insert_new_clique(self, clique_name:str, description:str, head_id:int) -> bool:
        if Helper.is_valid_name(clique_name) and Helper.is_valid_short_text(description) \
            and isinstance(head_id, int):
            return self.__clique_dbao.insert_new_clique(clique_name, description, head_id)
        return False

    def get_cliques_by_head_id(self, head_id:int) -> List[Clique]:
        cliques = self.__clique_dbao.find_cliques_by_head_id(head_id)
        return [Clique(*clique) for clique in cliques]

    def get_latest_clique_by_head_id(self, head_id:int) -> Clique:
        clique_info = self.__clique_dbao.find_latest_clique_by_head_id(head_id)
        if not clique_info:
            return None
        return Clique(*clique_info)