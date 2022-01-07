import unittest
from repositories.user_repository import UserRepository
from entities.user import User
from utils.error import CredentialsError

class TestUserRepository(unittest.TestCase):

    def setUp(self):
        self.test_user_repository = UserRepository("sqlite3_in_memory")

    def tearDown(self):
        self.test_user_repository.disconnect_db()

    def test_legal_insert_new_user_is_succesful(self):
        user_info = (
            "testUsername",
            "abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+=",
            "abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+=",
            "Taneli",
            "Härkönen"
        )
        user = self.test_user_repository.insert_new_user(*user_info)
        self.assertTrue(user)
        result = self.test_user_repository.get_users_by_user_ids(1)[0]
        self.assertEqual(result, user)

    def test_illegal_insert_new_user_with_allready_existing_username_is_not_succesful(self):
        user1_info = (
            "testUsername",
            "abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+=",
            "abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+=",
            "Testerfirstname",
            "Testerlastname"
        )
        user1 = self.test_user_repository.insert_new_user(*user1_info)
        self.assertTrue(user1)
        user2_info = (
            "testUsername",
            "abcABC123_~!",
            "abcABC123_~!",
            "Testerfirstname2",
            "Testerlastname2"
        )
        self.assertRaises(CredentialsError, lambda: self.test_user_repository.insert_new_user(*user2_info))

    def test_legal_insert_new_user_exists(self):
        user_info = (
            "testUsername",
            "abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+=",
            "abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+=",
            "Taneli",
            "Härkönen"
        )
        self.test_user_repository.insert_new_user(*user_info)
        self.assertTrue(self.test_user_repository.username_exists("testUsername"))

    def test_legal_insert_new_user_is_found(self):
        user_info = (
            "testUsername",
            "abcABC123_~!",
            "abcABC123_~!",
            "Testerfirstname",
            "Testerlastname"
        )
        self.test_user_repository.insert_new_user(*user_info)
        testuser = self.test_user_repository.get_user_by_username(user_info[0])
        self.assertEqual(testuser.user_id, 1)
        self.assertEqual(testuser.username, user_info[0])
        self.assertEqual(testuser.first_name, user_info[3])
        self.assertEqual(testuser.last_name, user_info[4])
        self.test_user_repository.forget_users()
        testuser = self.test_user_repository.get_user_by_username(user_info[0])
        self.assertEqual(testuser.user_id, 1)
        self.assertEqual(testuser.username, user_info[0])
        self.assertEqual(testuser.first_name, user_info[3])
        self.assertEqual(testuser.last_name, user_info[4])

    def test_legal_insert_new_user_correct_password_is_matching(self):
        user_info = (
            "testUsername",
            "complicated_password_abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+=",
            "complicated_password_abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+=",
            "Testerfirstname",
            "Testerlastname"
        )
        self.test_user_repository.insert_new_user(*user_info)
        self.assertTrue(self.test_user_repository.username_password_match(user_info[0], user_info[1]))

    def test_legal_insert_new_user_incorrect_password_is_not_matching(self):
        user_info = (
            "testUsername",
            "complicated_password_abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+=",
            "complicated_password_abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+=",
            "Testerfirstname",
            "Testerlastname"
        )
        self.test_user_repository.insert_new_user(*user_info)
        self.assertTrue(self.test_user_repository.username_password_match(user_info[0], user_info[1]))
        self.assertFalse(self.test_user_repository.username_password_match(user_info[0], "complicated_password_abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVYWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+="))

    def test_legal_insert_new_user_incorrect_user_correct_password_is_not_matching(self):
        user_info = (
            "testUsername",
            "complicated_password_abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+=",
            "complicated_password_abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+=",
            "Testerfirstname",
            "Testerlastname"
        )
        self.test_user_repository.insert_new_user(*user_info)
        self.assertTrue(self.test_user_repository.username_password_match(user_info[0], user_info[1]))
        self.assertFalse(self.test_user_repository.username_password_match("wrongusername", user_info[1]))

    def test_illegal_insert_new_user_invalid_arguments_raises_credentialserror(self):
        self.assertRaises(CredentialsError, lambda: self.test_user_repository.insert_new_user('.invalidusername', 'Password1!', 'Password1!', 'Firstname', 'Lastname'))
        self.assertRaises(CredentialsError, lambda: self.test_user_repository.insert_new_user('username', 'Password1!', 'Password1!', '.invalidFirstname', 'Lastname'))
        self.assertRaises(CredentialsError, lambda: self.test_user_repository.insert_new_user('username', 'Password1!', 'Password1!', 'Firstname', '.invalidLastname'))
        self.assertRaises(CredentialsError, lambda: self.test_user_repository.insert_new_user('username', '.invalidPassword1!', '.invalidPassword1!', 'Firstname', 'Lastname'))
        self.assertRaises(CredentialsError, lambda: self.test_user_repository.insert_new_user('username', 'Password1!', 'differentpassword', 'Firstname', 'Lastname'))

    def test_after_forget_users_fetch_users_from_dbao_and_still_gettable(self):
        user_info = (
            "Username",
            "Password1!",
            "Password1!",
            "Firstname",
            "Lastname"
        )
        user = self.test_user_repository.insert_new_user(*user_info)
        self.assertTrue(user)
        result = self.test_user_repository.get_users_by_user_ids(1)[0]
        self.assertEqual(result, user)
        self.test_user_repository.forget_users()
        result = self.test_user_repository.get_users_by_user_ids(1)[0]
        self.assertEqual(result, user)

    def test_get_users_by_user_ids(self):
        for i in range(1,50):
            self.test_user_repository.insert_new_user(f"username{i}", "Password1!", "Password1!", f"firstname{i}", f"lastname{i}")
        self.test_user_repository.forget_users()
        for i in range(50,101):
            self.test_user_repository.insert_new_user(f"username{i}", "Password1!", "Password1!", f"firstname{i}", f"lastname{i}")
        users = self.test_user_repository.get_users_by_user_ids(*[i for i in range(1,101)])
        self.assertEqual(len(users), 100)
        i = 1
        for user in users:
            self.assertEqual(user.user_id, i)
            self.assertEqual(user.username, f"username{i}")
            self.assertEqual(user.first_name, f"firstname{i}")
            self.assertEqual(user.last_name, f"lastname{i}")
            i += 1
