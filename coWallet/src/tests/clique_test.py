import unittest
from entities.clique import Clique
from entities.user import User

class TestClique(unittest.TestCase):

    def setUp(self):
        user_info = [1, "TestUsername", "Firstname", "Lastname"]
        user = User(*user_info)
        self.clique_info = {
            "clique_id": 1234,
            "clique_name": "testCliqueName",
            "description": "Just a test clique",
            "head_user": user
        }
        self.test_clique = Clique(**self.clique_info)
    
    def test_clique_info_is_set(self):
        self.assertEqual(self.test_clique.clique_id, self.clique_info["clique_id"])
        self.assertEqual(self.test_clique.clique_name, self.clique_info["clique_name"])
        self.assertEqual(self.test_clique.description, self.clique_info["description"])
        self.assertEqual(self.test_clique.head_user, self.clique_info["head_user"])

    def test_str_returns_clique_name_desc(self):
        self.assertEqual(str(self.test_clique), f"{self.clique_info['clique_name']}: {self.clique_info['description']}")

    def test_repr_returns_full_info(self):
        repr_assertion = f"Clique({self.clique_info['clique_id']},'{self.clique_info['clique_name']}','{self.clique_info['description']}')"
        self.assertEqual(repr(self.test_clique), repr_assertion)
