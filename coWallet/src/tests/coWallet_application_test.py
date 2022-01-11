import unittest
from application.cowallet_application import CoWalletApplication

from utils.error import CredentialsError

class TestCoWalletApplication(unittest.TestCase):

    def setUp(self):
        self.test_cowallet_application1 = CoWalletApplication("sqlite3_in_memory")
        self.test_cowallet_application2 = CoWalletApplication("sqlite3_in_memory")

    def tearDown(self):
        self.test_cowallet_application1.disconnect_db()
        self.test_cowallet_application2.disconnect_db()

    def test_created_user_is_able_to_login(self):
        user_info = (
            "testUsername",
            "testPassword1!",
            "testPassword1!",
            "testfirstname",
            "testlastname"
        )
        user = self.test_cowallet_application1.create_user(*user_info)
        self.assertTrue(user)
        login_user = self.test_cowallet_application1.get_current_user()
        self.assertEqual(login_user, user)
        self.test_cowallet_application1.logout()
        login_result = self.test_cowallet_application1.login(user_info[0], user_info[1])
        self.assertTrue(login_result)

    def test_not_created_user_is_not_able_to_login(self):
        login_info = ("randomusername", "randompassword")
        result = self.test_cowallet_application1.login(*login_info)
        self.assertFalse(result)

    def test_wrong_form_username_create_user_raises_credentialserror(self):
        user_info = [
            "",
            "testPassword1!",
            "testPassword1!",
            "testfirstname",
            "testlastname"
        ]
        self.assertRaises(CredentialsError, lambda: self.test_cowallet_application1.create_user(*user_info))
        user_info[0] = " "
        self.assertRaises(CredentialsError, lambda: self.test_cowallet_application1.create_user(*user_info))
        user_info[0] = """",/<>\\`{|}"""
        self.assertRaises(CredentialsError, lambda: self.test_cowallet_application1.create_user(*user_info))
        user_info[0] = "aaaa"
        self.assertRaises(CredentialsError, lambda: self.test_cowallet_application1.create_user(*user_info))
        user_info[0] = "".join(["a" for i in range(201)])
        self.assertRaises(CredentialsError, lambda: self.test_cowallet_application1.create_user(*user_info))
        user_info[0] = "!aaaaaa"
        self.assertRaises(CredentialsError, lambda: self.test_cowallet_application1.create_user(*user_info))
        user_info[0] = """!()-.?[]_'~;:!@#$%^&*+=0123456789"""
        self.assertRaises(CredentialsError, lambda: self.test_cowallet_application1.create_user(*user_info))

    def test_wrong_form_password_create_user_raises_credentialserror(self):
        user_info = [
            "testusername",
            "",
            "",
            "testfirstname",
            "testlastname"
        ]
        self.assertRaises(CredentialsError, lambda: self.test_cowallet_application1.create_user(*user_info))
        user_info[1] = " "
        user_info[2] = " "
        self.assertRaises(CredentialsError, lambda: self.test_cowallet_application1.create_user(*user_info))
        user_info[1] = """",/<>\\`{|}"""
        user_info[2] = """",/<>\\`{|}"""
        self.assertRaises(CredentialsError, lambda: self.test_cowallet_application1.create_user(*user_info))
        user_info[1] = "aaaa"
        user_info[2] = "aaaa"
        self.assertRaises(CredentialsError, lambda: self.test_cowallet_application1.create_user(*user_info))
        user_info[1] = "".join(["a" for i in range(201)])
        user_info[2] = "".join(["a" for i in range(201)])
        self.assertRaises(CredentialsError, lambda: self.test_cowallet_application1.create_user(*user_info))
        user_info[1] = "!aaaaaa"
        user_info[2] = "!aaaaaa"
        self.assertRaises(CredentialsError, lambda: self.test_cowallet_application1.create_user(*user_info))
        user_info[1] = """ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+="""
        user_info[2] = """ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+="""
        self.assertRaises(CredentialsError, lambda: self.test_cowallet_application1.create_user(*user_info))
        user_info[1] = """abcdefghijklmnopqrstuvwxyzåäö0123456789!()-.?[]_'~;:!@#$%^&*+="""
        user_info[2] = """abcdefghijklmnopqrstuvwxyzåäö0123456789!()-.?[]_'~;:!@#$%^&*+="""
        self.assertRaises(CredentialsError, lambda: self.test_cowallet_application1.create_user(*user_info))
        user_info[1] = """abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ!()-.?[]_'~;:!@#$%^&*+="""
        user_info[2] = """abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ!()-.?[]_'~;:!@#$%^&*+="""
        self.assertRaises(CredentialsError, lambda: self.test_cowallet_application1.create_user(*user_info))
        user_info[1] = """abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789"""
        user_info[2] = """abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789"""
        self.assertRaises(CredentialsError, lambda: self.test_cowallet_application1.create_user(*user_info))

    def test_wrong_form_first_name_create_user_raises_credentialserror(self):
        user_info = [
            "testusername",
            "testPassword1!",
            "testPassword1!",
            "",
            "testlastname"
        ]
        self.assertRaises(CredentialsError, lambda: self.test_cowallet_application1.create_user(*user_info))
        user_info[3] = " "
        self.assertRaises(CredentialsError, lambda: self.test_cowallet_application1.create_user(*user_info))
        user_info[3] = """",/<>\\`{|}"""
        self.assertRaises(CredentialsError, lambda: self.test_cowallet_application1.create_user(*user_info))
        user_info[3] = "".join(["a" for i in range(201)])
        self.assertRaises(CredentialsError, lambda: self.test_cowallet_application1.create_user(*user_info))
        user_info[3] = "!aaaaaa"

    def test_wrong_form_last_name_create_user_raises_credentialserror(self):
        user_info = [
            "testusername",
            "testPassword1!",
            "testPassword1!",
            "testfirstname",
            ""
        ]
        self.assertRaises(CredentialsError, lambda: self.test_cowallet_application1.create_user(*user_info))
        user_info[4] = " "
        self.assertRaises(CredentialsError, lambda: self.test_cowallet_application1.create_user(*user_info))
        user_info[4] = """",/<>\\`{|}"""
        self.assertRaises(CredentialsError, lambda: self.test_cowallet_application1.create_user(*user_info))
        user_info[4] = "".join(["a" for i in range(201)])
        self.assertRaises(CredentialsError, lambda: self.test_cowallet_application1.create_user(*user_info))
        user_info[4] = "!aaaaaa"

    def test_create_same_user_twice_raises_credentialserror(self):
        user_info = [
            "testusername",
            "testPassword1!",
            "testPassword1!",
            "testfirstname",
            "testlastname"
        ]
        self.assertTrue(self.test_cowallet_application1.create_user(*user_info))
        self.assertRaises(CredentialsError, lambda: self.test_cowallet_application2.create_user(*user_info))

    def test_create_user_passwords_not_matching_raises_credentialserror(self):
        user_info = [
            "testusername",
            "testPassword1!",
            "testPassword2!",
            "testfirstname",
            "testlastname"
        ]
        self.assertRaises(CredentialsError, lambda: self.test_cowallet_application1.create_user(*user_info))

    def test_logged_in_user_is_the_current_user_and_logged_out_is_none(self):
        user_info = [
            "testUsername",
            "testPassword1!",
            "testPassword1!",
            "testfirstname",
            "testlastname"
        ]
        user = self.test_cowallet_application1.create_user(*user_info)
        result = self.test_cowallet_application2.login(*user_info[:2])
        self.assertTrue(result)
        current_user1 = self.test_cowallet_application1.get_current_user()
        current_user2 = self.test_cowallet_application2.get_current_user()
        self.assertEqual(current_user1, user)
        self.assertEqual(current_user2, user)
        self.test_cowallet_application1.logout()
        self.test_cowallet_application2.logout()
        self.assertIsNone(self.test_cowallet_application1.get_current_user())
        self.assertIsNone(self.test_cowallet_application2.get_current_user())

    def test_created_username_is_not_available(self):
        user_info = [
            "testUsername",
            "testPassword1!",
            "testPassword1!",
            "testfirstname",
            "testlastname"
        ]
        self.test_cowallet_application1.create_user(*user_info)
        result = self.test_cowallet_application2.username_available(user_info[0])
        self.assertFalse(result)

    def test_not_created_username_is_available(self):
        username = "testUsername"
        result = self.test_cowallet_application1.username_available(username)
        self.assertTrue(result)

    def test_legal_create_user_and_clique_are_succesful_and_found(self):
        user_info = ("testUsername", "testPassword1!", "testPassword1!", "testFirstName", "testLastName")
        user = self.test_cowallet_application1.create_user(*user_info)
        self.assertTrue(user)
        clique_info = ("Test Clique Name", "test clique, description")
        clique = self.test_cowallet_application1.create_clique(*clique_info)
        self.assertTrue(clique)
        clique_tuple = (clique.clique_name, clique.description, clique.head_user)
        self.assertEqual(clique_tuple, clique_info + (user,))
        print(self.test_cowallet_application1.get_current_user())
        self.test_cowallet_application1.update_mbr_cliques()
        cliques = self.test_cowallet_application1.get_mbr_cliques()
        self.assertEqual(len(cliques), 1)
        self.assertEqual(cliques[0], clique)

    def test_create_user_and_illegal_clique_raises_credentialserror_and_is_not_found(self):
        user_info = ("testUsername", "testPassword1!", "testPassword1!", "testFirstName", "testLastName")
        user = self.test_cowallet_application1.create_user(*user_info)
        self.assertTrue(user)
        clique_info = (5, "test clique description")
        self.assertRaises(CredentialsError, lambda: self.test_cowallet_application1.create_clique(*clique_info))
        self.test_cowallet_application1.update_mbr_cliques()
        cliques = self.test_cowallet_application1.get_mbr_cliques()
        self.assertEqual(len(cliques), 0)
