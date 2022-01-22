import unittest
from repositories.user_repository import UserRepository
from repositories.clique_repository import CliqueRepository
from entities.user import User
from entities.clique import Clique
# from utils.error import CredentialsError

from random import randint

class TestCliqueRepository(unittest.TestCase):

    def setUp(self):
        self.test_user_repository = UserRepository("sqlite3_in_memory")
        self.test_clique_repository = CliqueRepository("sqlite3_in_memory")

    def tearDown(self):
        self.test_user_repository.disconnect_db()
        self.test_clique_repository.disconnect_db()

    def test_new_user_has_no_cliques(self):
        user1_info = ("testUsername1", "testPassword1!", "testPassword1!", "testFirstName1", "testLastName1")
        user1 = self.test_user_repository.insert_new_user(*user1_info)
        self.assertTrue(user1)
        result1:list = self.test_clique_repository.get_cliques_by_member(user1, self.test_user_repository)
        self.assertEqual(len(result1), 0)
    
    def test_added_cliques_are_found_by_its_head_user_and_by_its_members_even_after_forget_cliques(self):
        user1_info = ("testUsername1", "testPassword1!", "testPassword1!", "testFirstName1", "testLastName1")
        user1 = self.test_user_repository.insert_new_user(*user1_info)
        self.assertTrue(user1)
        result1:list = self.test_clique_repository.get_cliques_by_member(user1, self.test_user_repository)
        self.assertEqual(len(result1), 0)
        cliques = []
        for i in range(1,101):
            clique_info = (f"clique{i}Name", f"clique{i} description", user1)
            clique = self.test_clique_repository.insert_new_clique(*clique_info)
            self.assertTrue(clique)
            cliques.append(clique)
            result:list = self.test_clique_repository.get_cliques_by_member(user1, self.test_user_repository)
            self.assertEqual(len(result), i)
        user2_info = ("testUsername2", "testPassword2!", "testPassword2!", "testFirstName2", "testLastName2")
        user2 = self.test_user_repository.insert_new_user(*user2_info)
        self.assertTrue(user2)
        result2:list = self.test_clique_repository.get_cliques_by_member(user2, self.test_user_repository)
        self.assertEqual(len(result2), 0)
        for clique in cliques:
            self.test_clique_repository.insert_new_member(clique, user2)
        result3:list = self.test_clique_repository.get_cliques_by_member(user2, self.test_user_repository)
        self.assertEqual(len(result3), 100)
        i = 1
        for clique in result3:
            self.assertEqual(clique.clique_id, i)
            i += 1
        self.test_clique_repository.forget_cliques()
        result4:list = self.test_clique_repository.get_cliques_by_member(user1, self.test_user_repository)
        self.assertEqual(len(result4), 100)
        result5:list = self.test_clique_repository.get_cliques_by_member(user2, self.test_user_repository)
        self.assertEqual(len(result5), 100)

    def test_insert_new_clique_with_nonexist_head_user_raises_memoryerror(self):
        user_info = (1, "fakeUsername", "fakeFirstName", "fakeLastName")
        user = User(*user_info)
        clique_info = ("cliqueName", "clique description", user)
        self.assertRaises(MemoryError, lambda: self.test_clique_repository.insert_new_clique(*clique_info))

    def test_insert_new_member_with_nonexistent_parameter_not_succesful(self):
        real_user_info = ("realUsername", "Password1!", "Password1!", "realFirstName", "realLastName")
        fake_user_info = (2, "fakeUsername", "fakeFirstName", "fakeLastName")
        real_user = self.test_user_repository.insert_new_user(*real_user_info)
        fake_user = User(*fake_user_info)
        self.assertTrue(real_user)
        real_clique_info = ("realCliqueName", "real clique description", real_user)
        fake_clique_info = (2, "fakeCliqueName", "fake clique description", fake_user)
        real_clique = self.test_clique_repository.insert_new_clique(*real_clique_info)
        fake_clique = Clique(*fake_clique_info)
        self.assertTrue(real_clique)
        succesful1 = self.test_clique_repository.insert_new_member(real_clique, real_user)
        self.assertFalse(succesful1) # Klikin omistaja on jo jäsen
        succesful2 = self.test_clique_repository.insert_new_member(real_clique, fake_user)
        self.assertFalse(succesful2) # Käyttäjää ei ole
        succesful3 = self.test_clique_repository.insert_new_member(fake_clique, real_user)
        self.assertFalse(succesful3) # Klikkiä ei ole
        succesful4 = self.test_clique_repository.insert_new_member(fake_clique, fake_user)
        self.assertFalse(succesful4) # Klikkiä eikä käyttäjää ole

    def test_insert_new_transaction_is_succesful(self):
        user_info = ("testUsername1", "testPassword1!", "testPassword1!", "testFirstName1", "testLastName1")
        user = self.test_user_repository.insert_new_user(*user_info)
        self.assertTrue(user)
        clique_info = ("CliqueName", "clique description", user)
        clique = self.test_clique_repository.insert_new_clique(*clique_info)
        self.assertTrue(clique)
        transaction_info1 = ('2020-01-01 00:00:00', 0, user, clique, 100)
        success1 = self.test_clique_repository.insert_new_transaction(*transaction_info1)
        self.assertTrue(success1)
        transaction_info2 = ('2020-01-01 00:00:01', 'withdraw', user, clique, 50)
        success2 = self.test_clique_repository.insert_new_transaction(*transaction_info2)
        self.assertTrue(success2)

    def test_insert_illegal_transaction_is_not_succesful(self):
        user_info = ("testUsername1", "testPassword1!", "testPassword1!", "testFirstName1", "testLastName1")
        user = self.test_user_repository.insert_new_user(*user_info)
        self.assertTrue(user)
        clique_info = ("CliqueName", "clique description", user)
        clique = self.test_clique_repository.insert_new_clique(*clique_info)
        self.assertTrue(clique)
        transaction_info1 = ('2020-01-01 00:00:00', 3, user, clique, -100)
        self.assertRaises(ValueError, lambda: self.test_clique_repository.insert_new_transaction(*transaction_info1))
        transaction_info2 = ('2020-01-01 00:00:00', 'withdrew', user, clique, -50.5)
        self.assertRaises(ValueError, lambda: self.test_clique_repository.insert_new_transaction(*transaction_info2))

    def test_get_all_transactions_by_clique_is_succesful(self):
        users = []
        for i in range(100):
            user_info = (f"testUsername{i}", f"testPassword{i}!", f"testPassword{i}!", f"testFirstName{i}", f"testLastName{i}")
            users.append(self.test_user_repository.insert_new_user(*user_info))
            self.assertTrue(users[i])
        clique_info = ("CliqueName", "clique description", users[0])
        clique = self.test_clique_repository.insert_new_clique(*clique_info)
        self.assertTrue(clique)
        for user in users:
            for i in range(100):
                self.test_clique_repository.insert_new_transaction('2020-01-01 00:00:00', 0, user, clique, randint(1,10000))
        transactions = self.test_clique_repository.get_all_transactions_by_clique(clique, self.test_user_repository)
        user = None
        user_indx = -1
        for i, transaction in enumerate(transactions):
            if transaction[2] != user:
                user = transaction[2]
                user_indx += 1
            self.assertEqual(transaction[1:3], (0, users[user_indx]))
        
































   # def test_after_forget_cliques_fetch_cliques_from_dbao_and_still_gettable(self):
    #     user1_info = ("testUsername1", "testPassword1!", "testPassword1!", "testFirstName1", "testLastName1")
    #     user1 = self.test_user_repository.insert_new_user(*user1_info)
    #     self.assertTrue(user1)






    # def test_legal_insert_new_user_and_clique_are_succesful_and_found(self):
    #     user1_info = {
    #     "username": "testUsername",
    #     "password": "testPassword1!",
    #     "first_name": "testFirstName",
    #     "last_name": "testLastName"
    #     }
    #     test_user1 = User(0, user1_info["username"], user1_info["first_name"], user1_info["last_name"])
    #     user_id_1 = self.test_user_repository.insert_new_user(test_user1, user1_info["password"])
    #     self.assertTrue(user_id_1)
    #     test_user1.set_user_id(user_id_1)
    #     clique1_info = (0, "Test Clique Name", "test clique, description", 1)
    #     clique1 = Clique(*clique1_info)
    #     clique_id_1 = self.test_clique_repository.insert_new_clique(clique1)
    #     #clique1.set_clique_id(clique_id_1)
    #     self.assertTrue(clique_id_1)
    #     clique1 = self.test_clique_repository.get_cliques_by_head_id(1)[0]
    #     clique1_tuple = (clique1.clique_name, clique1.description, clique1.head_id)
    #     self.assertEqual(clique1_tuple, clique1_info[1:])
    #     clique1 = self.test_clique_repository.get_latest_clique_by_head_id(1)
    #     clique1_tuple = (clique1.clique_name, clique1.description, clique1.head_id)
    #     self.assertEqual(clique1_tuple, clique1_info[1:])
    #     clique2_info = (0, "Test Clique 2 Name", "test clique 2, description", 1)
    #     clique2 = Clique(*clique2_info)
    #     clique_id_2 = self.test_clique_repository.insert_new_clique(clique2)
    #     #clique2.set_clique_id(clique_id_2)
    #     self.assertTrue(clique_id_2)
    #     cliques = self.test_clique_repository.get_cliques_by_head_id(1)
    #     clique1_tuple = (cliques[0].clique_name, cliques[0].description, cliques[0].head_id)
    #     clique2_tuple = (cliques[1].clique_name, cliques[1].description, cliques[1].head_id)
    #     self.assertEqual((clique1_tuple, clique2_tuple), (clique1_info[1:], clique2_info[1:]))
    #     clique2 = self.test_clique_repository.get_latest_clique_by_head_id(1)
    #     clique2_tuple = (clique2.clique_name, clique2.description, clique2.head_id)
    #     self.assertEqual(clique2_tuple, clique2_info[1:])
    #     user2_info = {
    #     "username": "testUser2name",
    #     "password": "testPassword2!",
    #     "first_name": "testFirstName2",
    #     "last_name": "testLastName2"
    #     }
    #     test_user2 = User(0, user2_info["username"], user2_info["first_name"], user2_info["last_name"])
    #     user_id_2 = self.test_user_repository.insert_new_user(test_user2, user2_info["password"])
    #     self.assertTrue(user_id_2)
    #     clique3_info = (0, "Test Clique 3 Name", "test clique 3, description", 2)
    #     clique3 = Clique(*clique3_info)
    #     clique_id_3 = self.test_clique_repository.insert_new_clique(clique3)
    #     #clique3.set_clique_id(clique_id_3)
    #     self.assertTrue(clique_id_3)
    #     clique3 = self.test_clique_repository.get_cliques_by_head_id(2)[0]
    #     clique3_tuple = (clique3.clique_name, clique3.description, clique3.head_id)
    #     self.assertEqual(clique3_tuple, clique3_info[1:])
    #     clique3 = self.test_clique_repository.get_latest_clique_by_head_id(2)
    #     clique3_tuple = (clique3.clique_name, clique3.description, clique3.head_id)
    #     self.assertEqual(clique3_tuple, clique3_info[1:])

    # def test_illegal_insert_new_user_and_clique_arent_succesful_nor_found(self):
    #     # user1_info = {
    #     # "username": "testUsername",
    #     # "password": "testPassword1!",
    #     # "first_name": "testFirstName",
    #     # "last_name": "testLastName"
    #     # }
    #     # test_user1 = User(0, user1_info["username"], user1_info["first_name"], user1_info["last_name"])
    #     # user1_id = self.test_user_repository.insert_new_user(test_user1, user1_info["password"])
    #     # self.assertTrue(user1_id)
    #     # clique1_info = (0, "", "test clique description", 1)
    #     # self.assertRaises(CredentialsError, lambda: Clique(*clique1_info))
    #     clique1_id = self.test_clique_repository.insert_new_clique(None)
    #     self.assertIsNone(clique1_id)
    #     cliques = self.test_clique_repository.get_cliques_by_head_id(1)
    #     self.assertEqual(len(cliques), 0)

    # def test_insert_new_user_as_member_are_findable_by_member_id(self):
    #     user1_info = {
    #     "username": "testUsername",
    #     "password": "testPassword1!",
    #     "first_name": "testFirstName",
    #     "last_name": "testLastName"
    #     }
    #     test_user1 = User(0, user1_info["username"], user1_info["first_name"], user1_info["last_name"])
    #     user_id_1 = self.test_user_repository.insert_new_user(test_user1, user1_info["password"])
    #     self.assertTrue(user_id_1)
    #     clique1_info = (0, "testClique1", "test clique 1 description", 1)
    #     clique1 = Clique(*clique1_info)
    #     clique1_id = self.test_clique_repository.insert_new_clique(clique1)
    #     self.assertTrue(clique1_id)
    #     clique2_info = (0, "testClique2", "test clique 2 description", 1)
    #     clique2 = Clique(*clique2_info)
    #     clique2_id = self.test_clique_repository.insert_new_clique(clique2)
    #     self.assertTrue(clique2_id)
    #     clique3_info = (0, "testClique3", "test clique 3 description", 1)
    #     clique3 = Clique(*clique3_info)
    #     clique3_id = self.test_clique_repository.insert_new_clique(clique3)
    #     self.assertTrue(clique3_id)
    #     succesful5 = self.test_clique_repository.insert_new_member(1,1)
    #     succesful6 = self.test_clique_repository.insert_new_member(1,2)
    #     succesful7 = self.test_clique_repository.insert_new_member(1,3)
    #     self.assertTrue(succesful5)
    #     self.assertTrue(succesful6)
    #     self.assertTrue(succesful7)
    #     cliques_found:list = self.test_clique_repository.get_cliques_by_member_id(1)
    #     clique_infos = [(1,) + clique1_info[1:], (2,) + clique2_info[1:], (3,) + clique3_info[1:]]
    #     for i in range(3):
    #         clique_found_i_info = (cliques_found[i].clique_id, cliques_found[i].clique_name, cliques_found[i].description, cliques_found[i].head_id)
    #         self.assertEqual(clique_found_i_info, clique_infos[i])
