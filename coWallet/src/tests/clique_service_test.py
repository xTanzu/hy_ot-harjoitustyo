import unittest
from services.user_service import UserService
from services.clique_service import CliqueService

class TestCliqueService(unittest.TestCase):
    
    def setUp(self):
        self.test_user_service = UserService("sqlite3_in_memory")
        self.test_clique_service = CliqueService("sqlite3_in_memory")

    def tearDown(self):
        self.test_user_service.disconnect_db()
        self.test_clique_service.disconnect_db()

    def test_legal_create_user_and_clique_are_succesful_and_found(self):
        user_info = ("testUsername", "testPassword1!", "testFirstName", "testLastName")
        succesful = self.test_user_service.create_user(*user_info)
        self.assertTrue(succesful)
        clique_info = ("Test Clique Name", "test clique, description", 1)
        succesful = self.test_clique_service.create_clique(*clique_info)
        self.assertTrue(succesful)
        clique = self.test_clique_service.get_cliques_by_head_id(1)[0]
        clique_tuple = (clique.clique_name, clique.description, clique.head_id)
        self.assertEqual(clique_tuple, clique_info)
        clique = self.test_clique_service.get_latest_clique_by_head_id(1)
        clique_tuple = (clique.clique_name, clique.description, clique.head_id)
        self.assertEqual(clique_tuple, clique_info)

    def test_illegal_create_user_and_clique_arent_succesful_nor_found(self):
        user_info = ("testUsername", "testPassword1!", "testFirstName", "testLastName")
        succesful = self.test_user_service.create_user(*user_info)
        self.assertTrue(succesful)
        clique_info = (5, "test clique description", 1)
        succesful = self.test_clique_service.create_clique(*clique_info)
        self.assertFalse(succesful)
        cliques = self.test_clique_service.get_cliques_by_head_id(1)
        self.assertEqual(len(cliques), 0)
        clique = self.test_clique_service.get_latest_clique_by_head_id(1)
        self.assertIsNone(clique)