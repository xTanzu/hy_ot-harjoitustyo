import unittest
from repositories.user_repository import UserRepository
from entities.user import User

class TestUserRepository(unittest.TestCase):

    def setUp(self):
        self.test_user_repository = UserRepository("sqlite3_in_memory")

    def tearDown(self):
        self.test_user_repository.disconnect_db()

    # def test_legal_insert_new_user_is_succesful(self):
    #     username = "testUsername"
    #     password = "abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+="
    #     first_name = "Taneli"
    #     last_name = "Härkönen"
    #     test_user = User(0, username, first_name, last_name)
    #     user_id = self.test_user_repository.insert_new_user(test_user, password)
    #     self.assertEqual(user_id, 1)

    # def test_illegal_insert_new_user_with_allready_existing_username_is_not_succesful(self):
    #     username = "testUsername"
    #     password = "abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+="
    #     first_name = "Testerfirstname"
    #     last_name = "Testerlastname"
    #     test_user1 = User(0, username, first_name, last_name)
    #     user1_id = self.test_user_repository.insert_new_user(test_user1, password)
    #     self.assertEqual(user1_id, 1)
    #     username2 = "testUsername"
    #     password2 = "abcABC123_~!"
    #     first_name2 = "Testerfirstname2"
    #     last_name2 = "Testerlastname2"
    #     test_user2 = User(0, username2, first_name2, last_name2)
    #     user2_id = self.test_user_repository.insert_new_user(test_user2, password2)
    #     self.assertIsNone(user2_id)

    # def test_legal_insert_new_user_exists(self):
    #     username = "testUsername"
    #     password = "abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+="
    #     first_name = "Taneli"
    #     last_name = "Härkönen"
    #     test_user = User(0, username, first_name, last_name)
    #     self.test_user_repository.insert_new_user(test_user, password)
    #     self.assertTrue(self.test_user_repository.username_exists("testUsername"))

    # def test_legal_insert_new_user_is_found(self):
    #     username = "testUsername"
    #     password = "abcABC123_~!"
    #     first_name = "Testerfirstname"
    #     last_name = "Testerlastname"
    #     test_user = User(0, username, first_name, last_name)
    #     self.test_user_repository.insert_new_user(test_user, password)
    #     testuser = self.test_user_repository.get_user_by_username("testUsername")
    #     self.assertEqual(testuser.user_id, 1)
    #     self.assertEqual(testuser.username, "testUsername")
    #     self.assertEqual(testuser.first_name, "Testerfirstname")
    #     self.assertEqual(testuser.last_name, "Testerlastname")

    # def test_legal_insert_new_user_correct_password_is_matching(self):
    #     username = "testUsername"
    #     password = "complicated_password_abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+="
    #     first_name = "Testerfirstname"
    #     last_name = "Testerlastname"
    #     test_user = User(0, username, first_name, last_name)
    #     self.test_user_repository.insert_new_user(test_user, password)
    #     self.assertTrue(self.test_user_repository.username_password_match(username, password))

    # def test_legal_insert_new_user_incorrect_password_is_not_matching(self):
    #     username = "testUsername"
    #     password = "complicated_password_abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+="
    #     first_name = "Testerfirstname"
    #     last_name = "Testerlastname"
    #     test_user = User(0, username, first_name, last_name)
    #     self.test_user_repository.insert_new_user(test_user, password)
    #     self.assertTrue(self.test_user_repository.username_password_match(username, password))
    #     self.assertFalse(self.test_user_repository.username_password_match(username, "complicated_password_abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+=w"))

    # def test_legal_insert_new_user_incorrect_user_correct_password_is_not_matching(self):
    #     username = "testUsername"
    #     password = "complicated_password_abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+="
    #     first_name = "Testerfirstname"
    #     last_name = "Testerlastname"
    #     test_user = User(0, username, first_name, last_name)
    #     self.test_user_repository.insert_new_user(test_user, password)
    #     self.assertTrue(self.test_user_repository.username_password_match(username, password))
    #     self.assertFalse(self.test_user_repository.username_password_match("wrongusername", password))

    def test_get_users_by_user_id_list(self):
        for i in range(1,50):
            self.test_user_repository.insert_new_user(f"username{i}", "Password1!", "Password1!", f"firstname{i}", f"lastname{i}")
        self.test_user_repository.forget_users()
        for i in range(50,101):
            self.test_user_repository.insert_new_user(f"username{i}", "Password1!", "Password1!", f"firstname{i}", f"lastname{i}")
        users = self.test_user_repository.get_users_by_user_id_list([i for i in range(1,101)])
        self.assertEqual(len(users), 100)
        i = 1
        for user in users:
            self.assertEqual(user.user_id, i)
            self.assertEqual(user.username, f"username{i}")
            self.assertEqual(user.first_name, f"firstname{i}")
            self.assertEqual(user.last_name, f"lastname{i}")
            i += 1
