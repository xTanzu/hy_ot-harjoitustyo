import tkinter
from tkinter.constants import END

from ui.pages.page import Page
import ui.pages.user_main_page as user_main_page

import entities.clique as clique

from config import ENTRY_FIELD_WIDTH

class CreateCliquePage(Page):
    """Class for the create clique page

    Args:
        Page: Inherits the Page base-class
    """

    def __init__(self, *args, **kwargs):
        """Constructor of the CreateCliquePage class
        """
        super().__init__(*args, **kwargs)

        # Define Frames
        create_clique_frame = self.set_up_create_clique_frame()

        # Position Frames
        create_clique_frame.grid(row=0, column=0)

    def set_up_create_clique_frame(self) -> tkinter.Frame:
        """Set up the frame for creating the clique
            Contains the required input fields and buttons

        Returns:
            tkinter.Frame: A tkinter.Frame-object
        """
        frame = tkinter.Frame(self)

        def add_clique_pressed():
            """Functionality what happens when the "Add Clique" button is pressed
            """
            clique_name = clique_name_entry.get()
            clique_description = clique_description_entry.get()
            clique_head_user = self.controller.user_service.get_current_user()
            if not self.controller.clique_service.create_clique(clique_name, clique_description, clique_head_id):
                error_label["text"] = "Bad clique name or description"
                return
            created_clique = self.controller.clique_service.get_latest_clique_by_head_id(clique_head_id)
            error_label["text"] = f"Clique '{created_clique.clique_name[:20]}{'...' if len(created_clique.clique_name) > 20 else ''}' created"
            clique_name_entry.delete(0, END)
            clique_description_entry.delete(0, END)
            self.clique_created_succesful(created_clique)

        # Define Labels
        clique_name_label = tkinter.Label(self, text="clique name:")
        clique_description_label = tkinter.Label(self, text="description:")
        error_label = tkinter.Label(self, text="")

        # Define entries
        clique_name_entry = tkinter.Entry(self, width=ENTRY_FIELD_WIDTH)
        clique_description_entry = tkinter.Entry(self, width=ENTRY_FIELD_WIDTH)

        # Define Buttons
        add_clique_button = tkinter.Button(self, text="Add Clique", command=add_clique_pressed)
        back_button = tkinter.Button(self, text="Back", command=lambda: self.controller.switch_page_to(user_main_page.UserMainPage))

        # Position Widgets
        clique_name_label.grid(row=0, column=0, sticky="W")
        clique_name_entry.grid(row=1, column=0)
        clique_description_label.grid(row=2, column=0, sticky="W")
        clique_description_entry.grid(row=3, column=0)
        error_label.grid(row=4, column=0, sticky="W")
        back_button.grid(row=5, column=0, sticky="W")
        add_clique_button.grid(row=5, column=0, sticky="E")

        return frame
    
    def clique_created_succesful(self, created_clique:clique.Clique):
        """Functionality what happens when the Clique has been created
        """
        info_label2 = tkinter.Label(self, text="Coming the possibility to move to add members")
        info_label2.grid(row=6, column=0)
        print(created_clique)
