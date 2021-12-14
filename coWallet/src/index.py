#from ui.text_ui import TextUi
from ui.graphical_ui import GraphicalUi

# from dbaos.clique_dbao import CliqueDbao
# from repositories.clique_repository import CliqueRepository

def main():
    #user_interface = TextUi()#"sqlite3_in_memory")
    user_interface = GraphicalUi("sqlite3_in_memory")
    #user_interface = GraphicalUi("sqlite3_file")
    user_interface.start_ui()

    # repo = CliqueRepository()
    # cliques = repo.get_cliques_by_head_id(1)
    # print(cliques)

main()
