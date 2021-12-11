import tkinter

from ui.pages.page import Page
import ui.pages.create_clique_page as create_clique_page

#from config import *

class UserMainPage(Page):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Define Frames
        self.cliques_list_frame = self.set_up_cliques_list_frame()

        # Position Frames
        self.cliques_list_frame.grid(row=1, column=0)

    def set_up_cliques_list_frame(self) -> tkinter.Frame:
        frame = tkinter.Frame(self)

        # Define Buttons
        add_clique_button = tkinter.Button(frame, text="Add Clique", command=lambda: self.controller.switch_page_to(create_clique_page.CreateCliquePage))

        # Position Buttons
        add_clique_button.grid(row=0, column=0)

        return frame
