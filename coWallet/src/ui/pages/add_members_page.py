from cgitb import text
import tkinter

from ui.pages.page import Page
import ui.pages.clique_page as clique_page

from entities.user import User
from entities.clique import Clique

from utils.config import *

class AddMembersPage(Page):
    """Class for the add members page

    Args:
        Page: Inherits the Page base class
    """

    def __init__(self, *args, **kwargs):
        """Constructor of the AddMembersPage class
        """        
        self.clique:Clique = kwargs.pop('clique')
        super().__init__(*args, **kwargs)

        self.frames = {}
        self.frame_info = {
            "clique_info": {
                "set_up_method": self.set_up_clique_info_frame,
                "pack_params": {"side":"top", "fill":"x", "expand":False, "pady":PADDING_CONST}
                },
            "clique_member_list": {
                "set_up_method": self.set_up_clique_member_list_frame,
                "pack_params": {"side":"top", "fill":"both", "expand":True, "pady":PADDING_CONST}
                },
            "search_members_list": {
                "set_up_method": self.set_up_search_members_list_frame,
                "pack_params": {"side":"bottom", "fill":"x", "expand":False, "pady":PADDING_CONST}
                }
        }

    def construct_frames(self):
        """Construct the frames of the page. Initialize all frames, 
        get new content to updatable frames or get new and update existing 
        content on updatable frames.
        """        

        def unpack_frames():
            [frame.pack_forget() for frame in self.frames.values()]

        def initialize_frames():
            self.frames.clear()
            self.frames = {frame_name : info["set_up_method"]() for frame_name, info in self.frame_info.items()}

        def reconstruct_updatable_frames():
            for frame_name in ("clique_info", "clique_member_list", "search_members_list"):
                self.frames[frame_name] = self.frame_info[frame_name]["set_up_method"]()

        def pack_frames():
            [self.frames[frame_name].pack(**info["pack_params"]) for frame_name, info in self.frame_info.items()]

        # Unpack
        unpack_frames()

        # Define
        if len(self.frames) == 0:
            initialize_frames()
        else:
            reconstruct_updatable_frames()

        # Pack
        pack_frames()

    def set_up_clique_info_frame(self) -> tkinter.Frame:
        """Set up the frame to display general clique info 

        Returns:
            tkinter.Frame: A tkinter.Frame-object
        """
        frame = tkinter.Frame(self)
        frame.columnconfigure(0, weight=8)
        frame.columnconfigure(1, weight=1)
        for row in range(3):
            frame.rowconfigure(row, weight=1)
        
        # Define Labels
        capped_clique_name = self.clique.clique_name if len(self.clique.clique_name)<=16 else self.clique.clique_name[:14]+'...'
        clique_name_label = tkinter.Label(frame, text=capped_clique_name, font=self.font.H2_FONT)
        member_amount = len(self.clique.members)
        clique_member_amount_label = tkinter.Label(frame, text=f"{member_amount} {'member' if member_amount == 1 else 'members'}", font=self.font.SMALL_TEXT_FONT)
        head_Label = tkinter.Label(frame, text="Head:", font=self.font.SMALL_TEXT_FONT)
        fullname = str(self.clique.head_user)
        capped_fullname = fullname if len(fullname)<=25 else fullname[:23]+'...'
        head_fullname_label = tkinter.Label(frame, text=capped_fullname, font=self.font.NORMAL_BOLD_TEXT_FONT)
        username = self.clique.head_user.username
        capped_username = f"{username if len(username)<=20 else username[:18]+'...'} {'(you)' if self.clique.head_user == self.controller.app_logic.get_current_user() else ''}"
        head_username_label = tkinter.Label(frame, text=capped_username, font=self.font.SMALL_TEXT_FONT)

        # Position widgets
        clique_name_label.grid(row=0, column=0, sticky="W", rowspan=2)
        clique_member_amount_label.grid(row=2, column=0, sticky="W")
        head_Label.grid(row=0, column=1, sticky="W")
        head_fullname_label.grid(row=1, column=1, sticky="W")
        head_username_label.grid(row=2, column=1, sticky="W")

        return frame

    def set_up_clique_member_list_frame(self) -> tkinter.Frame:
        frame = tkinter.Frame(self)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        def update_member_list():
            self.controller.app_logic.update_clique_members(self.clique)
            members = self.clique.members
            for member in members:
                fullname = str(member)
                capped_fullname = f"{fullname if len(fullname)<=25 else fullname[:23] + '...'}"
                username = str(member.username)
                capped_username = f"{username if len(username)<=25 else username[:23] + '...'}"
                members_listbox.insert(tkinter.END, f"{capped_fullname}   ({capped_username})")

        def remove_member():
            print("remove")

        # Define Labels
        members_label = tkinter.Label(frame, text="members:")

        # Define Listbox
        members_scrollbar = tkinter.Scrollbar(frame, orient="vertical")
        members_listbox = tkinter.Listbox(frame, height=5, yscrollcommand=members_scrollbar.set)
        members_scrollbar.config(command=members_listbox.yview)
        update_member_list()

        # Define Buttons
        remove_member_button = tkinter.Button(frame, text="Remove member", command=remove_member)

        # Position widgets
        members_label.grid(row=0, column=0, sticky="W")
        members_listbox.grid(row=1, column=0, sticky="NEWS")
        members_scrollbar.grid(row=1, column=1, sticky="NS")
        remove_member_button.grid(row=2, column=0, sticky="W")

        return frame

    def set_up_search_members_list_frame(self) -> tkinter.Frame:
        frame = tkinter.Frame(self)
        label = tkinter.Label(frame, text="Search members list")

        # Define Buttons
        back_button = tkinter.Button(frame, text="Back", command=lambda: self.controller.switch_page_to(clique_page.CliquePage, page_id=self.clique.clique_id, clique=self.clique), width=BUTTON_WIDTH-8)

        label.pack()
        back_button.pack() # MUUTA NÄÄ GRIDIKSI!!!
        return frame

    def show(self):
        self.construct_frames()
        return super().show()


# Jatka set_up_clique_member_list_frame loppuun
# Aloita set_up_search_members_list_frame (vaatii jäsenien etsimistoiminnon logiikalta)