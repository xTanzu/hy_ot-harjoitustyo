import unittest
from entities.user import User

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
