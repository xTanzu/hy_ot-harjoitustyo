import unittest
from dbaos.user_dbao import UserDbao

class TestUserDbao(unittest.TestCase):

    def setUp(self):
        self.test_user_dbao = UserDbao("sqlite3_in_memory")

    def tearDown(self):
        self.test_user_dbao.disconnect()

    def test_get_db_type_succesful(self):
        self.assertEqual(self.test_user_dbao.db_type, "sqlite3_in_memory")

    def test_get_db_path_succesful(self):
        self.assertEqual(self.test_user_dbao.db_path, "data/data.db")

    def test_wrong_db_type_raises_connection_error(self):
        self.assertRaises(ConnectionError, lambda: UserDbao("wrong type"))

    def test_wrong_db_path_raises_connection_error(self):
        self.assertRaises(ConnectionError, lambda: UserDbao("sqlite3_file", "folderthatdoesnotexist/data.db"))

    def test_inserted_user_can_be_found(self):
        username = "testUsername"
        password = "testPassword"
        first_name = "testFirstName"
        last_name = "testLastName"
        succesful = self.test_user_dbao.insert_new_user(username, password, first_name, last_name)
        self.assertTrue(succesful)
        result = self.test_user_dbao.find_user_by_username(username)
        self.assertEqual(result, (1,) + (username, first_name, last_name))
        result = self.test_user_dbao.find_password_by_username(username)
        self.assertEqual(result, (username, password))

    def test_cannot_reinsert_user(self):
        username = "testUsername"
        password = "testPassword"
        first_name = "testFirstName"
        last_name = "testLastName"
        succesful = self.test_user_dbao.insert_new_user(username, password, first_name, last_name)
        self.assertTrue(succesful)
        succesful = self.test_user_dbao.insert_new_user(username, password, first_name, last_name)
        self.assertFalse(succesful)

    def test_find_users_by_user_id_list(self):
        for i in range(1,101):
            user_info = [f"username{i}", "password", f"first_name{i}", f"last_name{i}"]
            self.test_user_dbao.insert_new_user(*user_info)
        result = self.test_user_dbao.find_users_by_user_id_list([i for i in range(1,101)])
        self.assertEqual(len(result), 100)
        self.assertEqual(result[0][0], 1)
        self.assertEqual(result[10][1], 'username11')
        self.assertEqual(result[50][2], 'first_name51')
        self.assertEqual(result[79][3], 'last_name80')
