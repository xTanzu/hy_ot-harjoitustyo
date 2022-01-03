import unittest
from services.user_service import UserService
from services.clique_service import CliqueService

from utils.error import CredentialsError

class TestCliqueService(unittest.TestCase):
    
    def setUp(self):
        self.test_user_service = UserService("sqlite3_in_memory")
        self.test_clique_service = CliqueService("sqlite3_in_memory")

    def tearDown(self):
        self.test_user_service.disconnect_db()
        self.test_clique_service.disconnect_db()

    def test_legal_create_user_and_clique_are_succesful_and_found(self):
        user_info = ("testUsername", "testPassword1!", "testFirstName", "testLastName")
        user = self.test_user_service.create_user(*(user_info[:2] + user_info[1:]))
        self.assertTrue(user)
        clique_info = ("Test Clique Name", "test clique, description", user) # <-- muuta tää takasin head_id:ksi
        clique = self.test_clique_service.create_clique(*clique_info)
        self.assertTrue(clique)
        clique_tuple = (clique.clique_name, clique.description, clique.head_user)
        self.assertEqual(clique_tuple, clique_info) # <-- Muuta näitä assertteja
        cliques = self.test_clique_service.get_cliques_by_member(user)
        self.assertEqual(len(cliques), 1)
        clique_tuple = (cliques[0].clique_name, cliques[0].description, cliques[0].head_user)
        self.assertEqual(clique_tuple, clique_info) # <-- Muuta näitä assertteja
        # Tähän jäätiin ennen kuin muutettiin cliquen head takaisin vain id numeroksi (User olion sijaan)

    def test_illegal_create_user_and_clique_raises_credentialserror_and_is_not_found(self):
        user_info = ("testUsername", "testPassword1!", "testFirstName", "testLastName")
        user = self.test_user_service.create_user(*(user_info[:2] + user_info[1:]))
        self.assertTrue(user)
        clique_info = (5, "test clique description", user)
        self.assertRaises(CredentialsError, lambda: self.test_clique_service.create_clique(*clique_info))
        cliques = self.test_clique_service.get_cliques_by_head_id(1)
        self.assertEqual(len(cliques), 0)
        clique = self.test_clique_service.get_latest_clique_by_head_id(1)
        self.assertIsNone(clique)
