import tkinter

from ui.pages.page import Page
import ui.pages.user_main_page as user_main_page

# from entities.user import User
from entities.clique import Clique

from utils.config import *

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

        self.frames = {}
        self.frame_info = {
            "clique_info": {
                "set_up_method": self.set_up_clique_info_frame,
                "pack_params": {"side":"top", "fill":"x", "expand":False, "pady":PADDING_CONST}
                },
            "clique_financial_info": {
                "set_up_method": self.set_up_clique_financial_info_frame,
                "pack_params": {"side":"top", "fill":"both", "expand":True, "pady":PADDING_CONST}
                },
            "clique_payment_controls": {
                "set_up_method": self.set_up_clique_payment_controls_frame,
                "pack_params": {"side":"bottom", "fill":"x", "expand":False, "pady":PADDING_CONST}
                }
        }

    def construct_frames(self):
        """Construct the frames of the page. Initialize frames all frames, 
        get new content to updatable frames or get new and update existing 
        content on updatable frames.
        """        

        def unpack_frames():
            [frame.pack_forget() for frame in self.frames.values()]

        def initialize_frames():
            self.frames.clear()
            self.frames = {frame_name : info["set_up_method"]() for frame_name, info in self.frame_info.items()}

        def reconstruct_updatable_frames():
            for frame_name in ("clique_info", "clique_financial_info"):
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
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        def add_members_pressed():
            print("Add members pressed. Do something!!")

        # Define Labels
        capped_clique_name = self.clique.clique_name if len(self.clique.clique_name)<=16 else self.clique.clique_name[:14]+'...'
        clique_name_label = tkinter.Label(frame, text=capped_clique_name, font=self.font.H2_FONT)
        member_amount = len(self.clique.members)
        clique_member_amount_label = tkinter.Label(frame, text=f"{member_amount} {'member' if member_amount == 1 else 'members'}", font=self.font.NORMAL_TEXT_FONT)

        # Define Buttons
        add_members_button = tkinter.Button(frame, text="Add members", command=add_members_pressed)

        # Position widgets
        clique_name_label.grid(row=0, column=0, sticky="W")# rowspan=2,
        clique_member_amount_label.grid(row=1, column=0, sticky="W")
        add_members_button.grid(row=0, column=1, sticky="E")

        return frame

    def set_up_clique_financial_info_frame(self) -> tkinter.Frame:
        frame = tkinter.Frame(self)
        frame.config(highlightbackground=HIGHLIGHT_COLOR, highlightthickness=HIGHLIGHT_THICKNESS, padx=2*PADDING_CONST, pady=2*PADDING_CONST)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=2, minsize=4*PADDING_CONST)
        frame.columnconfigure(2, weight=1)
        frame.rowconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)
        frame.rowconfigure(2, weight=8)
        frame.rowconfigure(3, weight=1)
        frame.rowconfigure(4, weight=1)

        # Define Labels
        clique_data = self.controller.app_logic.get_personal_clique_data(self.clique)
        clique_purchases_label = tkinter.Label(frame, text="purchases:", font=self.font.SMALL_TEXT_FONT)
        clique_purchases_amount = tkinter.Label(frame, text=f"{clique_data[0]:.2f}€", font=self.font.H1_FONT)
        clique_cut_label = tkinter.Label(frame, text="your cut:", font=self.font.SMALL_TEXT_FONT)
        clique_cut_amount = tkinter.Label(frame, text=f"{clique_data[1]:.2f}€", font=self.font.H1_FONT)
        clique_paid_label = tkinter.Label(frame, text="paid:", font=self.font.SMALL_TEXT_FONT)
        clique_paid_amount = tkinter.Label(frame, text=f"{clique_data[2]:.2f}€", font=self.font.H1_FONT)
        clique_claim_label = tkinter.Label(frame, text="claim:", font=self.font.SMALL_TEXT_FONT)
        clique_claim_amount = tkinter.Label(frame, text=f"{clique_data[3]:.2f}€", font=self.font.H1_FONT)

        # Position widgets
        clique_purchases_label.grid(row=0, column=0, sticky="W")
        clique_purchases_amount.grid(row=1, column=0, sticky="W")
        clique_cut_label.grid(row=0, column=2, sticky="W")
        clique_cut_amount.grid(row=1, column=2, sticky="W")
        clique_paid_label.grid(row=3, column=0, sticky="W")
        clique_paid_amount.grid(row=4, column=0, sticky="W")
        clique_claim_label.grid(row=3, column=2, sticky="W")
        clique_claim_amount.grid(row=4, column=2, sticky="W")

        return frame

    def set_up_clique_payment_controls_frame(self) -> tkinter.Frame:
        frame = tkinter.Frame(self)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)
        frame.columnconfigure(3, weight=1)

        def validate_description(P:str) -> bool:
            if len(P) > 40:
                return False
            return True

        def validate_total(P:str) -> bool:
            if P == "":
                return True
            try:
                float(P)
                parts = P.split(".")
                if len(parts[0]) > 5:
                    return False
                elif len(parts) > 1 and len(parts[1]) > 2:
                    return False
                return True
            except:
                return False

        def add_transaction_pressed():
            transaction_type = transaction_val.get()
            transaction_type = 0
            transaction_description = description_entry.get()
            description_entry.delete(0, "end")
            transaction_total = total_entry.get()
            total_entry.delete(0, "end")
            print(f"Add transaction: \n{transaction_type}\n{transaction_description}\n{transaction_total}")

        # Define Labels
        transaction_label = tkinter.Label(frame, text="transaction:", font=self.font.NORMAL_TEXT_FONT)
        description_label = tkinter.Label(frame, text="description:", font=self.font.NORMAL_TEXT_FONT)
        total_label = tkinter.Label(frame, text="total amount:", font=self.font.NORMAL_TEXT_FONT)

        # Define Entries
        transaction_options = ["Purchase", "Payment"]
        transaction_val = tkinter.StringVar()
        transaction_val.set("Select")
        transaction_dropdown = tkinter.OptionMenu(frame, transaction_val, *transaction_options)
        transaction_dropdown.config(width=BUTTON_WIDTH)
        vcmd_description = (self.register(validate_description), '%P')#, '%S')
        description_entry = tkinter.Entry(frame, validate='key', validatecommand=vcmd_description, width=BUTTON_WIDTH+7)
        vcmd_total = (self.register(validate_total), '%P')#, '%S')
        total_entry = tkinter.Entry(frame, validate='key', validatecommand=vcmd_total, width=BUTTON_WIDTH+7)

        # Define Buttons
        back_button = tkinter.Button(frame, text="Back", command=lambda: self.controller.switch_page_to(user_main_page.UserMainPage), width=BUTTON_WIDTH-8)
        add_transaction_button = tkinter.Button(frame, text="Add transaction", command=add_transaction_pressed, width=BUTTON_WIDTH+2)

        # Position widgets
        transaction_label.grid(row=0, column=0, sticky="W", padx=PADDING_CONST, pady=PADDING_CONST_SMALL)
        transaction_dropdown.grid(row=0, column=1, columnspan=2, sticky="E", padx=PADDING_CONST, pady=PADDING_CONST_SMALL)
        description_label.grid(row=1, column=0, sticky="W", padx=PADDING_CONST, pady=PADDING_CONST_SMALL)
        description_entry.grid(row=1, column=1, columnspan=2, sticky="E", padx=PADDING_CONST, pady=PADDING_CONST_SMALL)
        total_label.grid(row=2, column=0, sticky="W", padx=PADDING_CONST, pady=PADDING_CONST_SMALL)
        total_entry.grid(row=2, column=1, columnspan=2, sticky="E", padx=PADDING_CONST, pady=PADDING_CONST_SMALL)
        back_button.grid(row=3, column=0, sticky="W", padx=PADDING_CONST, pady=PADDING_CONST)
        add_transaction_button.grid(row=3, column=1, columnspan=2, sticky="E", padx=PADDING_CONST, pady=PADDING_CONST)

        return frame

    def show(self):
        self.construct_frames()
        return super().show()
