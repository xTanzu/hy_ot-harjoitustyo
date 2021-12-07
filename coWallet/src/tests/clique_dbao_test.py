import unittest
from dbaos.user_dbao import UserDbao
from dbaos.clique_dbao import CliqueDbao

class TestCliqueDbao(unittest.TestCase):

    def setUp(self):
        self.test_clique_dbao = CliqueDbao("sqlite3_in_memory")
        self.test_user_dbao = UserDbao("sqlite3_in_memory")

    def tearDown(self):
        self.test_clique_dbao.disconnect()
        self.test_user_dbao.disconnect()

    def test_get_db_type_succesful(self):
        self.assertEqual(self.test_clique_dbao.db_type, "sqlite3_in_memory")

    def test_get_db_path_succesful(self):
        self.assertEqual(self.test_clique_dbao.db_path, "data/data.db")

    def test_wrong_db_type_raises_connection_error(self):
        self.assertRaises(ConnectionError, lambda: CliqueDbao("wrong type"))

    def test_wrong_db_path_raises_connection_error(self):
        self.assertRaises(ConnectionError, lambda: CliqueDbao("sqlite3_file", "folderthatdoesnotexist/data.db"))

    def test_clique_with_existing_head_can_be_inserted_and_found(self):
        user_info = ("testUsername", "testPassword", "testFirstName", "testLastName")
        succesful = self.test_user_dbao.insert_new_user(*user_info)
        self.assertTrue(succesful)
        clique_info = ("testCliqueName", "test clique description", 1)
        succesful = self.test_clique_dbao.insert_new_clique(*clique_info)
        self.assertTrue(succesful)
        result = self.test_clique_dbao.find_cliques_by_head_id(1)
        self.assertEqual(result, [(1,) + clique_info] )

    def test_clique_with_non_existing_head_cannot_be_inserted(self):
        clique_info = ("testCliqueName", "test clique description", 1)
        succesful = self.test_clique_dbao.insert_new_clique(*clique_info)
        self.assertFalse(succesful)
