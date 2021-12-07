import unittest
from repositories.user_repository import UserRepository
from repositories.clique_repository import CliqueRepository

class TestCliqueRepository(unittest.TestCase):

    def setUp(self):
        self.test_user_repository = UserRepository("sqlite3_in_memory")
        self.test_clique_repository = CliqueRepository("sqlite3_in_memory")

    def tearDown(self):
        self.test_user_repository.disconnect_db()
        self.test_clique_repository.disconnect_db()

    def test_legal_insert_new_user_and_clique_is_succesful(self):
        user_info = ("testUsername", "testPassword1!", "testFirstName", "testLastName")
        succesful = self.test_user_repository.insert_new_user(*user_info)
        self.assertTrue(succesful)
        clique_info = ("Test Clique Name", "test clique, description", 1)
        succesful = self.test_clique_repository.insert_new_clique(*clique_info)
        self.assertTrue(succesful)
    
    def test_illegal_insert_new_user_and_clique_is_not_succesful(self):
        user_info = ("testUsername", "testPassword1!", "testFirstName", "testLastName")
        succesful = self.test_user_repository.insert_new_user(*user_info)
        self.assertTrue(succesful)
        clique_info = ("", "test clique description", 1)
        succesful = self.test_clique_repository.insert_new_clique(*clique_info)
        self.assertFalse(succesful)
