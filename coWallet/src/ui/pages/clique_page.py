import tkinter

from ui.pages.page import Page
import ui.pages.user_main_page as user_main_page

# from entities.user import User
from entities.clique import Clique

from utils.config import *
from utils.helper import Helper

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
        for row in range(8):
            if (row + 1) % 3 == 0: # Joka kolmas rivi
                frame.rowconfigure(row, weight=6, minsize=2*PADDING_CONST)
            else:
                frame.rowconfigure(row, weight=1)
        

        # Define Labels
        clique_data = self.controller.app_logic.get_personal_clique_data(self.clique)
        cliques_purchases_label = tkinter.Label(frame, text="cliques purchases:", font=self.font.SMALL_TEXT_FONT)
        cliques_purchases_amount = tkinter.Label(frame, text=f"{clique_data[0]:.2f}€", font=self.font.H1_FONT)
        users_purchases_label = tkinter.Label(frame, text="users purchases:", font=self.font.SMALL_TEXT_FONT)
        users_purchases_amount = tkinter.Label(frame, text=f"{clique_data[1]:.2f}€", font=self.font.H1_FONT)
        users_cut_label = tkinter.Label(frame, text="users cut:", font=self.font.SMALL_TEXT_FONT)
        users_cut_amount = tkinter.Label(frame, text=f"{clique_data[2]:.2f}€", font=self.font.H1_FONT)
        users_paid_label = tkinter.Label(frame, text="users paid:", font=self.font.SMALL_TEXT_FONT)
        users_paid_amount = tkinter.Label(frame, text=f"{clique_data[3]:.2f}€", font=self.font.H1_FONT)
        users_withdrawn_label = tkinter.Label(frame, text="users withdrawn:", font=self.font.SMALL_TEXT_FONT)
        users_withdrawn_amount = tkinter.Label(frame, text=f"{clique_data[4]:.2f}€", font=self.font.H1_FONT)
        users_claim_label = tkinter.Label(frame, text="users claim:", font=self.font.SMALL_TEXT_FONT)
        users_claim_amount = tkinter.Label(frame, text=f"{clique_data[5]:.2f}€", font=self.font.H1_FONT)
        

        # Position widgets
        cliques_purchases_label.grid(   row=0, column=0, sticky="W")
        cliques_purchases_amount.grid(  row=1, column=0, sticky="W")
        users_purchases_label.grid(     row=0, column=2, sticky="W")
        users_purchases_amount.grid(    row=1, column=2, sticky="W")
        users_cut_label.grid(           row=3, column=0, sticky="W")
        users_cut_amount.grid(          row=4, column=0, sticky="W")
        users_paid_label.grid(          row=3, column=2, sticky="W")
        users_paid_amount.grid(         row=4, column=2, sticky="W")
        users_withdrawn_label.grid(     row=6, column=0, sticky="W")
        users_withdrawn_amount.grid(    row=7, column=0, sticky="W")
        users_claim_label.grid(         row=6, column=2, sticky="W")
        users_claim_amount.grid(        row=7, column=2, sticky="W")
     
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
            transaction_description = description_entry.get()
            transaction_total = total_entry.get()

            try:
                if transaction_type == transaction_options[0]:
                    # Make Purchase
                    Helper.is_valid_description(transaction_description)
                    transaction_total = Helper.convert_to_euro(transaction_total)
                    succesful = self.controller.app_logic.insert_new_purchase(self.clique, transaction_description, transaction_total)
                elif transaction_type == transaction_options[1]:
                    # Make Deposit
                    transaction_total = Helper.convert_to_euro(transaction_total)
                    succesful = self.controller.app_logic.insert_new_deposit(self.clique, transaction_total)
                elif transaction_type == transaction_options[2]:
                    # Make Withdraw
                    succesful = False
                else:
                    raise ValueError("Select a transaction-type")
            except ValueError as e:
                error_label["text"] = str(e)
                return

            if not succesful:
                error_label["text"] = "Transaction not succesful"
                return
            description_entry.delete(0, "end")
            total_entry.delete(0, "end")
            error_label["text"] = ""
            self.construct_frames()

        # Define Labels
        transaction_label = tkinter.Label(frame, text="transaction:", font=self.font.NORMAL_TEXT_FONT)
        description_label = tkinter.Label(frame, text="description:", font=self.font.NORMAL_TEXT_FONT)
        total_label = tkinter.Label(frame, text="total amount:", font=self.font.NORMAL_TEXT_FONT)
        error_label = tkinter.Label(frame, text="", font=self.font.SMALL_TEXT_FONT)

        # Define Entries
        transaction_options = ["Purchase", "Deposit", "Withdraw"]
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
        error_label.grid(row=3, column=1, columnspan=2, sticky="E", padx=PADDING_CONST, pady=PADDING_CONST_SMALL)
        back_button.grid(row=4, column=0, sticky="W", padx=PADDING_CONST, pady=PADDING_CONST)
        add_transaction_button.grid(row=4, column=1, columnspan=2, sticky="E", padx=PADDING_CONST, pady=PADDING_CONST)

        return frame

    def show(self):
        self.construct_frames()
        return super().show()
