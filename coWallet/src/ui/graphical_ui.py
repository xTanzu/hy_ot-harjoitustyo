import tkinter
from tkinter.constants import E

from application.cowallet_application import CoWalletApplication

from ui.pages.sign_in_page import SignInPage
from ui.pages.register_page import RegisterPage
from ui.pages.user_main_page import UserMainPage
from ui.pages.create_clique_page import CreateCliquePage
from ui.pages.clique_page import CliquePage
import ui.pages.page as page


class MainTkFrame(tkinter.Tk):
    """Class of the Ui that acts as the main container for other elements.
        Acts as a controller and a parent for child pages

    Args:
        tkinter: Tkinter framework object
    """

    def __init__(self, app_logic:CoWalletApplication, *args, **kwargs):
        """Constructor of the MainTkFrame class
            sets the main container, constructs and shows the first page

        Args:
            user_service (UserService): user service of the application.
                Is partly resposible for the application logic (User side)

            clique_service (CliqueService): clique service of the application.
                Is partly resposible for the application logic (Clique side)
        """        
        super().__init__(*args, **kwargs)
        self.app_logic = app_logic
        self.title("coWallet")
        self.minsize(300,300)
        self.container = tkinter.Frame(self, padx=20, pady=20)
        self.container.pack(fill="both", expand=True)
        self.container.columnconfigure(0, weight=1)
        self.container.rowconfigure(0, weight=1)

        self.pages = {}
        self.usable_pages = [SignInPage, RegisterPage, UserMainPage, CreateCliquePage, CliquePage]
        self.switch_page_to(SignInPage)
    
    def construct_page(self, usable_page:type, **kwargs) -> page.Page:
        """Contruct a given page, and saves it for later use

        Args:
            usable_page (type): Class of the page that is to be constructed

        Raises:
            NameError: If a given page allready exists

        Returns:
            page.Page: A reference to the contructer Page-object
        """
        if usable_page in self.pages:
            raise NameError(f"Page {usable_page.__name__} allready exists, can't construct it")
        page = usable_page(name=usable_page.__name__, parent=self.container, controller=self, **kwargs)
        page.grid(row=0, column=0, sticky="news")
        return page
    
    def switch_page_to(self, page:type, **kwargs):
        """Changes the current page to the given one
            If Page is not yet created, it is constructed

        Args:
            page (type): A Page object is wanted to be switched to

        Raises:
            NameError: If the given page is not defined a usable.
                Add the page-class to self.usable_pages if required
        """
        user = self.app_logic.get_current_user()
        page_instance_name = f"{page.__name__}{'_'+str(user.user_id) if user is not None else ''}{'_'+str(kwargs.pop('page_id')) if 'page_id' in kwargs else ''}"
        if page_instance_name not in self.pages:
            if page not in self.usable_pages:
                error_msg = f"Page {page.__name__} is not usable, can't switch to it"
                raise NameError(error_msg)
            print(page_instance_name)
            self.pages[page_instance_name] = self.construct_page(page, **kwargs)
        self.pages[page_instance_name].show(**kwargs)
        self.update()


class GraphicalUi:
    """The class that gathers all the resources and starts the user interface
    """

    def __init__(self, db_type:str = None, db_path:str = None):
        """Constructor of the GraphicalUi-class

        Args:
            db_type (str, optional): Where to save db-file, either 'sqlite3_in_memory' or
                'sqlite3_file'. Defaults to 'sqlite3_file' (from config.py).

            db_path (str, optional): path where to save db-file. When
                db_type == 'sqlite3_in_memory', then has no effect.
                Defaults to "data/data.db" (from config.py).
        """
        self.__app_logic = CoWalletApplication(db_type, db_path)
        self.__mainFrame = MainTkFrame(self.__app_logic)
    
    def start_ui(self):
        """function that starts the confiqured user interface
        """
        self.__mainFrame.mainloop()
