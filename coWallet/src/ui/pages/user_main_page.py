import tkinter

from ui.pages.page import Page
import ui.pages.create_clique_page as create_clique_page
import ui.pages.sign_in_page as sign_in_page
import ui.pages.clique_page as clique_page

from entities.clique import Clique

from config import PADDING_CONST

class UserMainPage(Page):
    """Class for the user main page

    Args:
        Page: Inherits the Page base-class
    """

    def __init__(self, *args, **kwargs):
        """Constructor of the UserMainPage class
        """
        super().__init__(*args, **kwargs)

        # Define Frames
        self.personal_account_info_frame = self.set_up_personal_account_info_frame()
        self.handle_account_balance_frame = self.set_up_handle_account_balance_frame()
        self.cliques_list_frame = self.set_up_cliques_list_frame()

        # Define Buttons
        add_clique_button_frame = self.set_up_add_clique_frame()

        # Position Frames
        self.personal_account_info_frame.pack(side="top", fill="x", expand=False, pady=PADDING_CONST)
        self.handle_account_balance_frame.pack(side="top", fill="x", expand=False, pady=PADDING_CONST)
        self.cliques_list_frame.pack(side="top", fill="both", expand=True, pady=PADDING_CONST)
        add_clique_button_frame.pack(side="bottom", fill="x", expand=False, pady=PADDING_CONST)
    
    def set_up_personal_account_info_frame(self) -> tkinter.Frame:
        """Set up the frame to display personal account info

        Returns:
            tkinter.Frame: A tkinter.Frame-object
        """
        frame = tkinter.Frame(self)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        def sign_out_pressed():
            self.controller.app_logic.logout()
            self.controller.switch_page_to(sign_in_page.SignInPage)

        # Define Labels
        full_name_label = tkinter.Label(frame, text=str(self.controller.app_logic.get_current_user()))
        self.account_balance_label = tkinter.Label(frame, text=str(self.controller.app_logic.get_current_user().balance))

        # Define Buttons
        sign_out_button = tkinter.Button(frame, text="Sign Out", command=sign_out_pressed)

        # Position Widgets
        full_name_label.grid(row=0, column=0, sticky="W")
        sign_out_button.grid(row=0, column=1, sticky="E")
        self.account_balance_label.grid(row=1, column=0, sticky="W")

        return frame
    
    def set_up_handle_account_balance_frame(self) -> tkinter.Frame:
        """Set up the frame for topping up and withdrawing funds to/from account

        Returns:
            tkinter.Frame: A tkinter.Frame-object
        """
        frame = tkinter.Frame(self)

        def top_up_pressed():
            """Functionality what happens when the "Top Up" button is pressed
            """            
            pass

        def withdraw_pressed():
            """Functionality what happens when the "Withdraw" button is pressed
            """
            pass

        # Define Buttons
        top_up_button = tkinter.Button(frame, text="Top Up", command=top_up_pressed)
        withdraw_button = tkinter.Button(frame, text="Withdraw", command=withdraw_pressed)

        # Define Entries
        amount_Entry = tkinter.Entry(frame, width=10)

        # Position Widgets
        amount_Entry.pack(side="left", fill="y", expand=False)
        withdraw_button.pack(side="right", fill="y", expand=False)
        top_up_button.pack(fill="y", expand=True)

        return frame

    def set_up_cliques_list_frame(self) -> tkinter.Frame:
        """Set up the frame for the list of cliques

        Returns:
            tkinter.Frame: A tkinter.Frame-object
        """
        frame = tkinter.Frame(self)

        def clique_item_pressed(clique:Clique):
            self.controller.switch_page_to(clique_page.CliquePage, page_id=clique.clique_id, clique=clique)

        def generate_clique_frame_array() -> (list("tkinter.Frame")):
            self.controller.app_logic.update_mbr_cliques()
            users_cliques = self.controller.app_logic.get_mbr_cliques()
            clique_frames = []
            for clique in users_cliques:
                def clique_click_event_handler(event, arg=clique):
                    clique_item_pressed(arg)
                clique_frame = tkinter.Frame(frame)
                clique_frame.bind('<Button-1>', clique_click_event_handler)
                clique_label = tkinter.Label(clique_frame, text=str(clique), padx=PADDING_CONST, pady=PADDING_CONST)
                clique_label.bind('<Button-1>', clique_click_event_handler)
                clique_personal_balance = self.controller.app_logic.get_clique_personal_balance(clique)
                balance_label = tkinter.Label(clique_frame, text=clique_personal_balance, padx=PADDING_CONST, pady=PADDING_CONST)
                balance_label.bind('<Button-1>', clique_click_event_handler)
                balance_label.pack(side="right", fill="y", expand=False)
                clique_label.pack(side="left", fill="y", expand=False)
                clique_frames.append(clique_frame)
            return clique_frames

        clique_frame_array:list(tkinter.Frame) = generate_clique_frame_array()

        # Position Widgets
        [frame.pack(side="top", fill="x", expand=False) for frame in clique_frame_array]

        return frame

    def set_up_add_clique_frame(self) -> tkinter.Frame:
        """Set up the frame for the clique adding functionality

        Returns:
            tkinter.Frame: A tkinter.Frame-object
        """
        frame = tkinter.Frame(self)
        add_clique_button = tkinter.Button(frame, text="Add Clique", pady=PADDING_CONST, command=lambda: self.controller.switch_page_to(create_clique_page.CreateCliquePage))
        add_clique_button.pack(side="top", fill="x", expand=False)
        return frame
