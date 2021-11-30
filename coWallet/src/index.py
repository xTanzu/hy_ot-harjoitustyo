from ui.text_ui import TextUi
from ui.graphical_ui import GraphicalUi

def main():
    #user_interface = TextUi()#"sqlite3_in_memory")
    user_interface = GraphicalUi()#"sqlite3_in_memory")
    user_interface.start_ui()

main()
