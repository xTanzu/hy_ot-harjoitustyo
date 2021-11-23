import unittest
from repositories.user_repository import User_Repository

class TestUser_Repository(unittest.TestCase):
    
    def setUp(self):
        self.test_user_repository = User_Repository("sqlite3_in_memory")
    
    def test_legal_insert_new_user_is_succesful(self):
        username = "testUsername"
        password = "abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+="
        first_name = "Taneli"
        last_name = "Härkönen"
        result = self.test_user_repository.insert_new_user(username, password, first_name, last_name)
        self.assertTrue(result)
    
    def test_illegal_insert_new_user_is_not_succesful(self):
        username = "testUsername,"
        password = "syntymäpäivä123"
        first_name = "6testFirstName"
        last_name = "6testLastName"
        result = self.test_user_repository.insert_new_user(username, password, first_name, last_name)
        self.assertFalse(result)
    
    def test_illegal_insert_new_user_with_allready_existing_username_is_not_succesful(self):
        username = "testUsername"
        password = "abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+="
        first_name = "Testerfirstname"
        last_name = "Testerlastname"
        result = self.test_user_repository.insert_new_user(username, password, first_name, last_name)
        self.assertTrue(result)
        username2 = "testUsername"
        password2 = "abcABC123_~!"
        first_name2 = "Testerfirstname2"
        last_name2 = "Testerlastname2"
        result = self.test_user_repository.insert_new_user(username2, password2, first_name2, last_name2)
        self.assertFalse(result)
    
    def test_legal_insert_new_user_exists(self):
        username = "testUsername"
        password = "abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+="
        first_name = "Taneli"
        last_name = "Härkönen"
        self.test_user_repository.insert_new_user(username, password, first_name, last_name)
        self.assertTrue(self.test_user_repository.username_exists("testUsername"))
    
    def test_illegal_insert_new_user_does_not_exist(self):
        username = "testUsername,"
        password = "syntymäpäivä123"
        first_name = "6testFirstName"
        last_name = "6testLastName"
        self.test_user_repository.insert_new_user(username, password, first_name, last_name)
        self.assertFalse(self.test_user_repository.username_exists("testUsername"))
    
    def test_legal_insert_new_user_is_found(self):
        username = "testUsername"
        password = "abcABC123_~!"
        first_name = "Testerfirstname"
        last_name = "Testerlastname"
        self.test_user_repository.insert_new_user(username, password, first_name, last_name)
        testuser = self.test_user_repository.get_user_by_username("testUsername")
        self.assertEqual(testuser.user_id, 1)
        self.assertEqual(testuser.username, "testUsername")
        self.assertEqual(testuser.first_name, "Testerfirstname")
        self.assertEqual(testuser.last_name, "Testerlastname")
    
    def test_legal_insert_new_user_correct_password_is_matching(self):
        username = "testUsername"
        password = "complicated_password_abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+="
        first_name = "Testerfirstname"
        last_name = "Testerlastname"
        self.test_user_repository.insert_new_user(username, password, first_name, last_name)
        self.assertTrue(self.test_user_repository.username_password_match(username, password))
    
    def test_legal_insert_new_user_incorrect_password_is_not_matching(self):
        username = "testUsername"
        password = "complicated_password_abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+="
        first_name = "Testerfirstname"
        last_name = "Testerlastname"
        self.test_user_repository.insert_new_user(username, password, first_name, last_name)
        self.assertTrue(self.test_user_repository.username_password_match(username, password))
        self.assertFalse(self.test_user_repository.username_password_match(username, "complicated_password_abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+=w"))

    def test_legal_insert_new_user_incorrect_user_correct_password_is_not_matching(self):
        username = "testUsername"
        password = "complicated_password_abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+="
        first_name = "Testerfirstname"
        last_name = "Testerlastname"
        self.test_user_repository.insert_new_user(username, password, first_name, last_name)
        self.assertTrue(self.test_user_repository.username_password_match(username, password))
        self.assertFalse(self.test_user_repository.username_password_match("wrongusername", password))
