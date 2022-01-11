import tkinter
from entities.user import User

from ui.pages.page import Page
import ui.pages.user_main_page as user_main_page

from entities.clique import Clique

class CliquePage(Page):
    """Class for the clique page

    Args:
        Page: Inherits the Page base-class
    """

    def __init__(self, *args, **kwargs):
        """Constructor of the CliquePage class
        """
        self.clique:Clique = kwargs.pop("clique")
        super().__init__(*args, **kwargs)

        # Define Frames

        # Define Buttons

        # Position Frames

        label = tkinter.Label(self, text=str(self.clique))
        user:User = self.controller.app_logic.get_current_user()
        back_button = tkinter.Button(self, text="back", command=lambda: self.controller.switch_page_to(user_main_page.UserMainPage))
        label.pack()
        back_button.pack()











# Luo ensin perustoiminnot niin, että klikkilista päivitetään aina tarvittaessa, ja että on myös nappi päivittää itse!