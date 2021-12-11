import tkinter

from services.user_service import UserService
from services.clique_service import CliqueService

from ui.pages.sign_in_page import SignInPage
from ui.pages.register_page import RegisterPage
from ui.pages.user_main_page import UserMainPage
from ui.pages.create_clique_page import CreateCliquePage
import ui.pages.page as page


class MainTkFrame(tkinter.Tk):

    def __init__(self, user_service:UserService, clique_service:CliqueService, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_service = user_service
        self.clique_service = clique_service
        self.container = tkinter.Frame()
        self.container.grid(row=0, column=0, sticky='nesw')
        self.pages = {}
        self.usable_pages = [SignInPage, RegisterPage, UserMainPage, CreateCliquePage]
        page = self.construct_page(self.usable_pages[0])
        page.show()
    
    def construct_page(self, usable_page:type) -> page.Page:
        if usable_page in self.pages:
            raise NameError(f"Page {usable_page.__name__} allready exists, can't construct it")
        page = usable_page(name=usable_page.__name__, parent=self.container, controller=self)
        page.grid(row=0, column=0, sticky="nsew")
        self.pages[type(page).__name__] = page
        return page
    
    def switch_page_to(self, page:type):
        if page not in self.pages:
            if page not in self.usable_pages:
                error_msg = f"Page {page.__name__} is not usable, can't switch to it"
                raise NameError(error_msg)
            self.construct_page(page)             
        self.pages[page.__name__].show()


class GraphicalUi:

    def __init__(self, db_type:str = None, db_path:str = None):
        self.__user_service = UserService(db_type, db_path)
        self.__clique_service = CliqueService(db_type, db_path)
        self.__mainFrame = MainTkFrame(self.__user_service, self.__clique_service)
    
    def start_ui(self):
        self.__mainFrame.mainloop()
