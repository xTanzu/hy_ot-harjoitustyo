import unittest
from entities.user import User
from utils.error import CredentialsError

class TestUser(unittest.TestCase):
    
    def setUp(self):
        self.test_user = User(1234, "testName", "testFirstName", "testLastName")
    
    def test_user_id_is_set(self):
        self.assertEqual(self.test_user.user_id, 1234)

    def test_username_is_set(self):
        self.assertEqual(self.test_user.username, "testName")
    
    def test_first_name_is_set(self):
        self.assertEqual(self.test_user.first_name, "testFirstName")
    
    def test_last_name_is_set(self):
        self.assertEqual(self.test_user.last_name, "testLastName")

    # def test_balance_is_set(self):
    #     #Tänne testiä
    #     self.assertTrue(False)

    def test_set_user_id_sets_user_id(self):
        username = "testUsername"
        first_name = "Taneli"
        last_name = "Härkönen"
        test_user = User(0, username, first_name, last_name)
        self.assertEqual(test_user.user_id, 0)
        test_user.set_user_id(100)
        self.assertEqual(test_user.user_id, 100)

    def test_illegal_set_user_id_does_raises_credentialserror(self):
        username = "testUsername"
        first_name = "Taneli"
        last_name = "Härkönen"
        test_user = User(0, username, first_name, last_name)
        self.assertEqual(test_user.user_id, 0)
        self.assertRaises(CredentialsError, lambda: test_user.set_user_id(-100))
        self.assertRaises(CredentialsError, lambda: test_user.set_user_id("k"))
        self.assertRaises(CredentialsError, lambda: test_user.set_user_id([1,2,3,4]))

    def test_str_returns_full_name(self):
        self.assertEqual(str(self.test_user), "testFirstName testLastName")

    def test_repr_returns_full_info(self):
        repr_str = f"User(1234,'testLastName','testFirstName','testName')"
        self.assertEqual(repr(self.test_user), repr_str)
