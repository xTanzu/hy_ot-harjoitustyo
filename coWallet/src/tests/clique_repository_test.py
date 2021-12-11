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

    def test_new_user_has_no_cliques(self):
        user1_info = ("testUsername", "testPassword1!", "testFirstName", "testLastName")
        succesful1 = self.test_user_repository.insert_new_user(*user1_info)
        self.assertTrue(succesful1)
        result1:list = self.test_clique_repository.get_cliques_by_head_id(1)
        self.assertEqual(len(result1), 0)
        result2:tuple = self.test_clique_repository.get_latest_clique_by_head_id(1)
        self.assertIsNone(result2)

    def test_legal_insert_new_user_and_clique_are_succesful_and_found(self):
        user1_info = ("testUsername", "testPassword1!", "testFirstName", "testLastName")
        succesful1 = self.test_user_repository.insert_new_user(*user1_info)
        self.assertTrue(succesful1)
        clique1_info = ("Test Clique Name", "test clique, description", 1)
        succesful2 = self.test_clique_repository.insert_new_clique(*clique1_info)
        self.assertTrue(succesful2)
        clique1 = self.test_clique_repository.get_cliques_by_head_id(1)[0]
        clique1_tuple = (clique1.clique_name, clique1.description, clique1.head_id)
        self.assertEqual(clique1_tuple, clique1_info)
        clique1 = self.test_clique_repository.get_latest_clique_by_head_id(1)
        clique1_tuple = (clique1.clique_name, clique1.description, clique1.head_id)
        self.assertEqual(clique1_tuple, clique1_info)
        clique2_info = ("Test Clique 2 Name", "test clique 2, description", 1)
        succesful2 = self.test_clique_repository.insert_new_clique(*clique2_info)
        self.assertTrue(succesful2)
        cliques = self.test_clique_repository.get_cliques_by_head_id(1)
        clique1_tuple = (cliques[0].clique_name, cliques[0].description, cliques[0].head_id)
        clique2_tuple = (cliques[1].clique_name, cliques[1].description, cliques[1].head_id)
        self.assertEqual((clique1_tuple, clique2_tuple), (clique1_info, clique2_info))
        clique2 = self.test_clique_repository.get_latest_clique_by_head_id(1)
        clique2_tuple = (clique2.clique_name, clique2.description, clique2.head_id)
        self.assertEqual(clique2_tuple, clique2_info)
        user2_info = ("testUsername2", "testPassword2!", "testFirstName2", "testLastName2")
        succesful3 = self.test_user_repository.insert_new_user(*user2_info)
        self.assertTrue(succesful3)
        clique3_info = ("Test Clique 3 Name", "test clique 3, description", 2)
        succesful4 = self.test_clique_repository.insert_new_clique(*clique3_info)
        self.assertTrue(succesful4)
        clique3 = self.test_clique_repository.get_cliques_by_head_id(2)[0]
        clique3_tuple = (clique3.clique_name, clique3.description, clique3.head_id)
        self.assertEqual(clique3_tuple, clique3_info)
        clique3 = self.test_clique_repository.get_latest_clique_by_head_id(2)
        clique3_tuple = (clique3.clique_name, clique3.description, clique3.head_id)
        self.assertEqual(clique3_tuple, clique3_info)

    
    def test_illegal_insert_new_user_and_clique_arent_succesful_nor_found(self):
        user_info = ("testUsername", "testPassword1!", "testFirstName", "testLastName")
        succesful = self.test_user_repository.insert_new_user(*user_info)
        self.assertTrue(succesful)
        clique_info = ("", "test clique description", 1)
        succesful = self.test_clique_repository.insert_new_clique(*clique_info)
        self.assertFalse(succesful)
        cliques = self.test_clique_repository.get_cliques_by_head_id(1)
        self.assertEqual(len(cliques), 0)
