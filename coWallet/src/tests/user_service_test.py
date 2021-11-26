import unittest
from services.user_service import UserService, CredentialsError

class TestUserService(unittest.TestCase):

    def setUp(self):
        self.test_user_service = UserService("sqlite3_in_memory")
    
    def test_created_user_is_able_to_login(self):
        username = "testUsername"
        password = "testPassword1!"
        first_name = "testfirstname"
        last_name = "testlastname"
        self.test_user_service.create_user(username, password, first_name, last_name)
        result = self.test_user_service.login(username, password)
        self.assertTrue(result)
    
    def test_not_created_user_is_not_able_to_login(self):
        username = "randomusername"
        password = "randompassword"
        result = self.test_user_service.login(username, password)
        self.assertFalse(result)
    
    def test_wrong_form_username_create_user_raises_credentialserror(self):
        username = ""
        password = "testPassword1!"
        first_name = "testfirstname"
        last_name = "testlastname"
        self.assertRaises(CredentialsError, lambda: self.test_user_service.create_user(username, password, first_name, last_name))
        username = " "
        self.assertRaises(CredentialsError, lambda: self.test_user_service.create_user(username, password, first_name, last_name))
        username = """",/<>\\`{|}"""
        self.assertRaises(CredentialsError, lambda: self.test_user_service.create_user(username, password, first_name, last_name))
        username = "aaaa"
        self.assertRaises(CredentialsError, lambda: self.test_user_service.create_user(username, password, first_name, last_name))
        username = "".join(["a" for i in range(201)])
        self.assertRaises(CredentialsError, lambda: self.test_user_service.create_user(username, password, first_name, last_name))
        username = "!aaaaaa"
        self.assertRaises(CredentialsError, lambda: self.test_user_service.create_user(username, password, first_name, last_name))
        username = """!()-.?[]_'~;:!@#$%^&*+=0123456789"""
        self.assertRaises(CredentialsError, lambda: self.test_user_service.create_user(username, password, first_name, last_name))

    def test_wrong_form_password_create_user_raises_credentialserror(self):
        username = "testusername"
        password = ""
        first_name = "testfirstname"
        last_name = "testlastname"
        self.assertRaises(CredentialsError, lambda: self.test_user_service.create_user(username, password, first_name, last_name))
        password = " "
        self.assertRaises(CredentialsError, lambda: self.test_user_service.create_user(username, password, first_name, last_name))
        password = """",/<>\\`{|}"""
        self.assertRaises(CredentialsError, lambda: self.test_user_service.create_user(username, password, first_name, last_name))
        password = "aaaa"
        self.assertRaises(CredentialsError, lambda: self.test_user_service.create_user(username, password, first_name, last_name))
        password = "".join(["a" for i in range(201)])
        self.assertRaises(CredentialsError, lambda: self.test_user_service.create_user(username, password, first_name, last_name))
        password = "!aaaaaa"
        self.assertRaises(CredentialsError, lambda: self.test_user_service.create_user(username, password, first_name, last_name))
        password = """ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+="""
        self.assertRaises(CredentialsError, lambda: self.test_user_service.create_user(username, password, first_name, last_name))
        password = """abcdefghijklmnopqrstuvwxyzåäö0123456789!()-.?[]_'~;:!@#$%^&*+="""
        self.assertRaises(CredentialsError, lambda: self.test_user_service.create_user(username, password, first_name, last_name))
        password = """abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ!()-.?[]_'~;:!@#$%^&*+="""
        self.assertRaises(CredentialsError, lambda: self.test_user_service.create_user(username, password, first_name, last_name))
        password = """abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789"""
        self.assertRaises(CredentialsError, lambda: self.test_user_service.create_user(username, password, first_name, last_name))
    
    def test_wrong_form_first_name_create_user_raises_credentialserror(self):
        username = "testusername"
        password = "testPassword1!"
        first_name = ""
        last_name = "testlastname"
        self.assertRaises(CredentialsError, lambda: self.test_user_service.create_user(username, password, first_name, last_name))
        first_name = " "
        self.assertRaises(CredentialsError, lambda: self.test_user_service.create_user(username, password, first_name, last_name))
        first_name = """",/<>\\`{|}"""
        self.assertRaises(CredentialsError, lambda: self.test_user_service.create_user(username, password, first_name, last_name))
        first_name = "".join(["a" for i in range(201)])
        self.assertRaises(CredentialsError, lambda: self.test_user_service.create_user(username, password, first_name, last_name))
        first_name = "!aaaaaa"
    
    def test_wrong_form_last_name_create_user_raises_credentialserror(self):
        username = "testusername"
        password = "testPassword1!"
        first_name = "testfirstname"
        last_name = ""
        self.assertRaises(CredentialsError, lambda: self.test_user_service.create_user(username, password, first_name, last_name))
        last_name = " "
        self.assertRaises(CredentialsError, lambda: self.test_user_service.create_user(username, password, first_name, last_name))
        last_name = """",/<>\\`{|}"""
        self.assertRaises(CredentialsError, lambda: self.test_user_service.create_user(username, password, first_name, last_name))
        last_name = "".join(["a" for i in range(201)])
        self.assertRaises(CredentialsError, lambda: self.test_user_service.create_user(username, password, first_name, last_name))
        last_name = "!aaaaaa"

    def test_create_same_user_twice_raises_credentialserror(self):
        username = "testusername"
        password = "testPassword1!"
        first_name = "testfirstname"
        last_name = "testlastname"
        self.assertTrue(self.test_user_service.create_user(username, password, first_name, last_name))
        self.assertRaises(CredentialsError, lambda: self.test_user_service.create_user(username, password, first_name, last_name))

    def test_logged_in_user_is_the_current_user_and_logged_out_is_none(self):
        username = "testUsername"
        password = "testPassword1!"
        first_name = "testfirstname"
        last_name = "testlastname"
        self.test_user_service.create_user(username, password, first_name, last_name)
        result = self.test_user_service.login(username, password)
        self.assertTrue(result)
        current_user = self.test_user_service.get_current_user()
        user_repr = f"<User> id: {1}, \
            username: {username}, \
            first_name: {first_name}, \
            last_name: {last_name}"
        self.assertEqual(repr(current_user), user_repr)
        self.test_user_service.logout()
        self.assertIsNone(self.test_user_service.get_current_user())
