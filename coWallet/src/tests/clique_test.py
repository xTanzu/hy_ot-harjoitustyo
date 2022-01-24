import unittest
from entities.clique import Clique
from entities.user import User

from random import shuffle

from utils.error import CredentialsError

class TestClique(unittest.TestCase):

    def setUp(self):
        user_info = [1, "TestUsername", "Firstname", "Lastname"]
        self.test_user = User(*user_info)
        self.clique_info = {
            "clique_id": 1234,
            "clique_name": "testCliqueName",
            "description": "Just a test clique",
            "head_user": self.test_user
        }
        self.test_clique = Clique(**self.clique_info)
    
    def test_clique_info_is_set(self):
        self.assertEqual(self.test_clique.clique_id, self.clique_info["clique_id"])
        self.assertEqual(self.test_clique.clique_name, self.clique_info["clique_name"])
        self.assertEqual(self.test_clique.description, self.clique_info["description"])
        self.assertEqual(self.test_clique.head_user, self.clique_info["head_user"])
        self.assertEqual(type(self.test_clique.members), list)
        self.assertEqual(len(self.test_clique.members), 0)

    def test_invalid_arguments_raise_credentialserror(self):
        self.assertRaises(CredentialsError, lambda: Clique('invalid_id', 'CliqueName', 'clique description', self.test_user))
        self.assertRaises(CredentialsError, lambda: Clique(1, '.InvalidCliqueName', 'clique description', self.test_user))
        self.assertRaises(CredentialsError, lambda: Clique(1, 'CliqueName', '{Invalid clique description}', self.test_user))

    def test_set_clique_id_sets_id_if_valid(self):
        self.assertEqual(self.test_clique.clique_id, 1234)
        self.test_clique.set_clique_id(1)
        self.assertEqual(self.test_clique.clique_id, 1)
        self.assertRaises(CredentialsError, lambda: self.test_clique.set_clique_id(-5))

    def test_insert_new_members_inserts_members_if_valid(self):
        user1 = User(1, 'username1', 'firstName1', 'lastName1')
        user2 = User(2, 'username2', 'firstName2', 'lastName2')
        user3 = User(3, 'username3', 'firstName3', 'lastName3')
        user4 = User(4, 'username4', 'firstName4', 'lastName4')
        clique = Clique(1, 'cliqueName', 'clique description', user1)
        dummyClique = Clique(0,'a','a', user1)
        self.assertEqual(clique.members, [])
        clique.insert_new_members(dummyClique)
        self.assertEqual(clique.members, [])
        clique.insert_new_members(user1)
        self.assertEqual(clique.members, [user1])
        clique.insert_new_members(user1)
        self.assertEqual(clique.members, [user1])
        clique.insert_new_members(user2, user3, user4)
        self.assertEqual(clique.members, [user1, user2, user3, user4])

    def test_insert_new_members_with_reset_resets_members(self):
        users = []
        for i in range(100):
            users.append(User(i, f'username{i}', f'firstName{i}', f'lastName{i}'))
        users.sort()
        clique = Clique(1, 'cliqueName', 'clique description', users[0])
        clique.insert_new_members(*users[:50])
        for i, member in enumerate(sorted(clique.members)):
            self.assertEqual(member, users[i])
        clique.insert_new_members(*users[50:], reset=True)
        members = sorted(clique.members)
        self.assertEqual(members[0], users[0])
        for i, member in enumerate(members[1:]):
            self.assertEqual(member, users[i+50])

    def test_str_returns_clique_name_desc(self):
        self.assertEqual(str(self.test_clique), f"{self.clique_info['clique_name']}: {self.clique_info['description']}")

    def test_repr_returns_full_info(self):
        repr_assertion = f"Clique({self.clique_info['clique_id']},'{self.clique_info['clique_name']}','{self.clique_info['description']}')"
        self.assertEqual(repr(self.test_clique), repr_assertion)

    def test_hash_returns_clique_id(self):
        self.assertEqual(hash(self.test_clique), self.clique_info["clique_id"])

    def test_cliques_with_same_id_are_equal(self):
        clique1_info = (57, "clique1Name", "clique1 description", self.test_user)
        clique2_info = (57, "clique2Name", "clique2 description", self.test_user)
        clique1 = Clique(*clique1_info)
        clique2 = Clique(*clique2_info)
        self.assertEqual(clique1, clique2)

    def test_cliques_with_different_id_are_not_equal(self):
        clique1_info = (57, "clique1Name", "clique1 description", self.test_user)
        clique2_info = (56, "clique2Name", "clique2 description", self.test_user)
        clique1 = Clique(*clique1_info)
        clique2 = Clique(*clique2_info)
        self.assertNotEqual(clique1, clique2)

    def test_user_and_clique_with_same_id_are_not_equal(self):
        user = User(1, "testName", "testFirstName", "testLastName")
        clique = Clique(1, "testName", "test description", user)
        self.assertNotEqual(clique, user)

    def test_lt_sorts_cliques_correctly(self):
        user1 = User(0,'aaaaaa','a','a')
        user2 = User(0,'aaaaaa','a','b')
        user3 = User(0,'aaaaaa','b','b')
        user4 = User(0,'aaaaab','b','b')
        list_of_cliques = [
            Clique(0, 'a', 'a', user1),
            Clique(0, 'b', 'a', user1),
            Clique(0, 'bc', 'a', user1),
            Clique(0, 'bd', 'a', user1),
            Clique(0, 'bd', 'a', user1),
            Clique(0, 'bd', 'b', user1),
            Clique(0, 'bd', 'bc', user1),
            Clique(0, 'bd', 'bd', user1),
            Clique(0, 'bd', 'bd', user2),
            Clique(0, 'bd', 'bd', user3),
            Clique(0, 'bd', 'bd', user4),
            Clique(1, 'bd', 'bd', user4),
            Clique(2, 'bd', 'bd', user4),
            Clique(3, 'bd', 'bd', user4),
        ]
        list_of_cliques_shuffled = list_of_cliques.copy()
        shuffle(list_of_cliques_shuffled)
        list_of_cliques_shuffled.sort()
        list(map(lambda val: self.assertEqual(val[0], val[1]), [(list_of_cliques[i], list_of_cliques_shuffled[i]) for i in range(len(list_of_cliques))]))

    def test_comparing_dissimilar_type_object_with_lt_raises_typeerror(self):
        user = User(1, "testName", "testFirstName", "testLastName")
        clique = Clique(1, "testName", "test description", user)
        self.assertRaises(TypeError, lambda: clique < user)