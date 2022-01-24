import unittest
from application.cowallet_application import CoWalletApplication
from random import randint
from math import ceil

from utils.error import CredentialsError
from utils.helper import Helper

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
        cliques = self.test_cowallet_application1.get_mbr_cliques()
        self.assertEqual(len(cliques), 1)
        self.assertEqual(cliques[0], clique)

    def test_create_user_and_illegal_clique_raises_credentialserror_and_is_not_found(self):
        user_info = ("testUsername", "testPassword1!", "testPassword1!", "testFirstName", "testLastName")
        user = self.test_cowallet_application1.create_user(*user_info)
        self.assertTrue(user)
        clique_info = (5, "test clique description")
        self.assertRaises(CredentialsError, lambda: self.test_cowallet_application1.create_clique(*clique_info))
        cliques = self.test_cowallet_application1.get_mbr_cliques(update=True)
        self.assertEqual(len(cliques), 0)

    def test_get_personal_clique_data(self):
        user_amount = 100
        purchases_per_user = 100
        users = []
        for i in range(user_amount//2):
            user_info = (f"testUsername{i}", f"testPassword{i}!", f"testPassword{i}!", f"testFirstName{i}", f"testLastName{i}")
            users.append((self.test_cowallet_application1.create_user(*user_info), user_info))
            self.assertTrue(users[i][0])
        for i in range(user_amount//2, user_amount):
            user_info = (f"testUsername{i}", f"testPassword{i}!", f"testPassword{i}!", f"testFirstName{i}", f"testLastName{i}")
            users.append((self.test_cowallet_application2.create_user(*user_info), user_info))
            self.assertTrue(users[i][0])
        self.test_cowallet_application1.logout()
        self.test_cowallet_application1.login(users[0][1][0], users[0][1][1])
        clique_info = ("Test Clique Name", "test clique, description")
        clique = self.test_cowallet_application1.create_clique(*clique_info)
        self.assertTrue(clique)
        self.test_cowallet_application1.logout()
        self.test_cowallet_application2.logout()
        purchases = {}
        letters = "abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789!()-.?[]_'~;:!@#$%^&*+="
        for user_nugget in users:
            user = user_nugget[0]
            user_info = user_nugget[1]
            self.test_cowallet_application1.login(user_info[0], user_info[1])
            self.test_cowallet_application1.insert_new_member(clique, user)
            purchases[user] = []
            for i in range(purchases_per_user):
                description = "".join([letters[randint(0,len(letters)-1)] for x in range(randint(10,60))])
                purcase_price = randint(1,10000)
                purchase = (description, purcase_price)
                purchases[user].append(purchase)
                success1 = self.test_cowallet_application1.insert_new_purchase(clique, description, purcase_price/100)
                self.assertTrue(success1)
            self.test_cowallet_application1.logout()
        total_purchase_sum = 0
        for user_nugget in users:
            user = user_nugget[0]
            for purchase in purchases[user]:
                total_purchase_sum += purchase[1]
        users_cut = ceil(total_purchase_sum / len(clique.members))    
        for user_nugget in users:
            user = user_nugget[0]
            user_info = user_nugget[1]
            self.test_cowallet_application1.login(user_info[0], user_info[1])
            users_purchases = sum([purchase[1] for purchase in purchases[user]])
            users_deposits = 0
            if users_purchases < users_cut:
                users_deposits = randint(1, users_cut - users_purchases)
                success2 = self.test_cowallet_application1.insert_new_deposit(clique, users_deposits/100)
                self.assertTrue(success2)
            users_paid = users_purchases + users_deposits
            users_withdrawn = 0 # Tänne vielä nostot myöhemmin
            users_entered_data = (total_purchase_sum / 100, users_purchases / 100, users_cut / 100, users_paid / 100, users_withdrawn / 100, (users_cut + users_withdrawn - users_paid) / 100)
            personal_clique_data = self.test_cowallet_application1.get_personal_clique_data(clique)
            self.assertEqual(personal_clique_data, users_entered_data)
            self.test_cowallet_application1.logout()
        #self.assertTrue(False)
        # Lisää tänne käyttäjille talletuksia ja tarkista niiden oikeellisuus myös!!

    def test_update_clique_members(self):
        users_per_application = 100
        app1_users = []
        for i in range(users_per_application):
            user_info = (f"testUsername{i}", f"testPassword{i}!", f"testPassword{i}!", f"testFirstName{i}", f"testLastName{i}")
            app1_users.append((self.test_cowallet_application1.create_user(*user_info), user_info))
            self.assertTrue(app1_users[-1][0])
        app2_users = []
        for i in range(users_per_application, 2*users_per_application):
            user_info = (f"testUsername{i}", f"testPassword{i}!", f"testPassword{i}!", f"testFirstName{i}", f"testLastName{i}")
            app2_users.append((self.test_cowallet_application1.create_user(*user_info), user_info))
            self.assertTrue(app2_users[-1][0])
        self.test_cowallet_application1.logout()
        self.test_cowallet_application2.logout()
        app1_users.sort()
        app2_users.sort()
        self.test_cowallet_application1.login(app1_users[0][1][0], app1_users[0][1][1])
        clique_info = ("Test Clique Name", "test clique, description")
        app1_clique = self.test_cowallet_application1.create_clique(*clique_info)
        self.assertTrue(app1_clique)
        for user_nugget in app1_users:
            self.test_cowallet_application1.insert_new_member(app1_clique, user_nugget[0])
        for i, member in enumerate(sorted(app1_clique.members)):
            self.assertEqual(member, app1_users[i][0])
        self.test_cowallet_application1.insert_new_member(app1_clique, app2_users[0][0])
        self.test_cowallet_application2.login(app2_users[0][1][0], app2_users[0][1][1])
        app2_clique = self.test_cowallet_application2.get_mbr_cliques()[0]
        self.assertEqual(len(app2_clique.members), 101)
        for user_nugget in app2_users:
            self.test_cowallet_application2.insert_new_member(app2_clique, user_nugget[0])
        self.assertEqual(len(app1_clique.members), 101)
        self.assertEqual(len(app2_clique.members), 200)
        self.test_cowallet_application1.update_clique_members(app1_clique)
        self.assertEqual(len(app1_clique.members), 200)
        self.assertEqual(len(app2_clique.members), 200)
        users = sorted(app1_users + app2_users)
        for i, member in enumerate(sorted(app1_clique.members)):
            self.assertEqual(member, users[i][0])
