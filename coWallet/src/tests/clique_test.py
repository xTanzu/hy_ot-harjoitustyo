import unittest
from entities.clique import Clique

class TestClique(unittest.TestCase):

    def setUp(self):
        self.clique_info = {
            "clique_id": 1234,
            "clique_name": "testCliqueName",
            "description": "Just a test clique",
            "head_id": 1
        }
        self.test_clique = Clique(**self.clique_info)
    
    def test_clique_info_is_set(self):
        self.assertEqual(self.test_clique.clique_id, self.clique_info["clique_id"])
        self.assertEqual(self.test_clique.clique_name, self.clique_info["clique_name"])
        self.assertEqual(self.test_clique.description, self.clique_info["description"])
        self.assertEqual(self.test_clique.head_id, self.clique_info["head_id"])

    def test_str_returns_group_name_desc(self):
        self.assertEqual(str(self.test_clique), f"{self.clique_info['clique_name']}: {self.clique_info['description']}")

    def test_repr_returns_full_info(self):
        assertion = f"""Clique-object:
            id: {self.clique_info["clique_id"]},
            name: {self.clique_info["clique_name"]},
            description: {self.clique_info["description"][:100]},
            head_id: {self.clique_info["head_id"]}
        """
