import unittest
from dbaos.user_dbao import User_DBAO

class TestUser_DBAO(unittest.TestCase):

    def setUp(self):
        self.test_user_dbao = User_DBAO("sqlite3_in_memory")
    
    def test_get_db_type_succesful(self):
        self.assertEqual(self.test_user_dbao.db_type, "sqlite3_in_memory")
    
    def test_get_db_path_succesful(self):
        self.assertEqual(self.test_user_dbao.db_path, ":memory:")
    
    def test_wrong_db_type_raises_value_error(self):
        self.assertRaises(ValueError, lambda: User_DBAO("wrong type"))
        self.assertRaises(ValueError, lambda: User_DBAO("sqlite3_no_destination"))
    
    def test_wrong_db_path_raises_connection_error(self):
        self.assertRaises(ConnectionError, lambda: User_DBAO("sqlite3_file", "folderthatdoesnotexist/data.db"))
    
    def test_inserted_user_can_be_found(self):
        username = "testUsername"
        password = "testPassword"
        first_name = "testFirstName"
        last_name = "testLastName"
        succesful = self.test_user_dbao.insert_new_user(username, password, first_name, last_name)
        self.assertTrue(succesful)
        result = self.test_user_dbao.find_user_by_username(username)
        self.assertEqual(result[1:], (username, password, first_name, last_name))
    
    def test_cannot_reinsert_user(self):
        username = "testUsername"
        password = "testPassword"
        first_name = "testFirstName"
        last_name = "testLastName"
        succesful = self.test_user_dbao.insert_new_user(username, password, first_name, last_name)
        self.assertTrue(succesful)
        succesful = self.test_user_dbao.insert_new_user(username, password, first_name, last_name)
        self.assertFalse(succesful)