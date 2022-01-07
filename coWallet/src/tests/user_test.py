import unittest
from entities.user import User
from entities.clique import Clique
from utils.error import CredentialsError
from random import shuffle


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

    def test_balance_is_set_initially(self):
        self.assertEqual(self.test_user.balance, 0)

    def test_illegal_user_arquments_raises_credentialserror(self):
        self.assertRaises(CredentialsError, lambda: User("k", "userName", "Firstname", "Lastname"))
        self.assertRaises(CredentialsError, lambda: User(0, ".illegalUserName", "Firstname", "Lastname"))
        self.assertRaises(CredentialsError, lambda: User(0, "userName", ".illegalFirstname", "Lastname"))
        self.assertRaises(CredentialsError, lambda: User(0, "userName", "Firstname", ".illegalLastname"))

    def test_set_user_id_sets_user_id(self):
        username = "testUsername"
        first_name = "Taneli"
        last_name = "Härkönen"
        test_user = User(0, username, first_name, last_name)
        self.assertEqual(test_user.user_id, 0)
        test_user.set_user_id(100)
        self.assertEqual(test_user.user_id, 100)

    def test_set_user_id_with_illegal_id_raises_credentialserror(self):
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

    def test_hash_returns_user_id(self):
        self.assertEqual(hash(self.test_user), self.test_user.user_id)

    def test_users_with_same_id_are_equal(self):
        user1 = User(11, "testName1", "testFirstName1", "testLastName1")
        user2 = User(11, "testName2", "testFirstName2", "testLastName2")
        self.assertEqual(user1, user2)

    def test_user_and_clique_with_same_id_are_not_equal(self):
        user = User(1, "testName", "testFirstName", "testLastName")
        clique = Clique(1, "testName", "test description", user)
        self.assertNotEqual(user, clique)

    def test_lt_sorts_users_correctly(self):
        list_of_users = [
            User(0,'aaaaaa','a','a'),
            User(0,'aaaaaa','a','b'),
            User(0,'aaaaaa','a','bc'),
            User(0,'aaaaaa','a','bd'),
            User(0,'aaaaaa','b','bd'),
            User(0,'aaaaaa','bc','bd'),
            User(0,'aaaaaa','bd','bd'),
            User(0,'aaaaab','bd','bd'),
            User(0,'aaabaa','bd','bd'),
            User(0,'baaaaa','bd','bd'),
            User(1,'baaaaa','bd','bd'),
            User(57,'baaaaa','bd','bd')
        ]
        list_of_users_shuffled = list_of_users.copy()
        shuffle(list_of_users_shuffled)
        list_of_users_shuffled.sort()
        list(map(lambda val: self.assertEqual(val[0], val[1]), [(list_of_users[i], list_of_users_shuffled[i]) for i in range(len(list_of_users))]))

    def test_comparing_dissimilar_type_object_with_lt_raises_typeerror(self):
        user = User(1, "testName", "testFirstName", "testLastName")
        clique = Clique(1, "testName", "test description", user)
        self.assertRaises(TypeError, lambda: user < clique)
