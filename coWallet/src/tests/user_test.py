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
    
    def test_str_returns_full_name(self):
        self.assertEqual(str(self.test_user), "testFirstName testLastName")
    
    def test_repr_returns_full_info(self):
        repr_str = f"""<User>:
            id: 1234,
            username: testName,
            first_name: testFirstName,
            last_name: testLastName"""
        self.assertEqual(repr(self.test_user), repr_str)
