import unittest
from utils.helper import Helper

class TestHelper(unittest.TestCase):

    # Legal Characters --------------------------------------------------------------------

    def test_consists_of_legal_characters_returns_true_when_true(self):
        all_legal_chars = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!()-.?[]_'~;:!@#$%^&*+=åäöÅÄÖ"""
        self.assertTrue(Helper.consists_of_legal_characters(all_legal_chars))
    
    def test_consists_of_legal_characters_returns_false_when_false(self):
        all_legal_chars = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!()-.?[]_'~;:!@#$%^&*+=åäöÅÄÖ"""
        illegal_chars = """",/<>\\`{|}"""
        self.assertFalse(Helper.consists_of_legal_characters(all_legal_chars + illegal_chars))
        self.assertFalse(Helper.consists_of_legal_characters(all_legal_chars + ","))
    
    # Letters --------------------------------------------------------------------

    def test_contains_letters_returns_true_when_true(self):
        test_string1 = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!()-.?[]_'~;:!@#$%^&*+=åäöÅÄÖ"""
        test_string2 = """0123456789!()-.?[]_'~;a:!@#$%^&*+="""
        test_string3 = "mattiMeika123"
        self.assertTrue(Helper.contains_letters(test_string1))
        self.assertTrue(Helper.contains_letters(test_string2))
        self.assertTrue(Helper.contains_letters(test_string3))
    
    def test_contains_letters_returns_false_when_false(self):
        test_string1 = """0123456789!()-.?[]_'~;:!@#$%^&*+="""
        test_string2 = "3.14159265359"
        test_string3 = "+1551+"
        self.assertFalse(Helper.contains_letters(test_string1))
        self.assertFalse(Helper.contains_letters(test_string2))
        self.assertFalse(Helper.contains_letters(test_string3))

    # Lowercase Letters --------------------------------------------------------------------

    def test_contains_lowercase_letters_returns_true_when_true(self):
        test_string1 = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!()-.?[]_'~;:!@#$%^&*+=åäöÅÄÖ"""
        test_string2 = """ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ0123456789a!()-.?[]_'~;:!@#$%^&*+="""
        test_string3 = "mattiMeikäläinen123"
        self.assertTrue(Helper.contains_lowercase_letters(test_string1))
        self.assertTrue(Helper.contains_lowercase_letters(test_string2))
        self.assertTrue(Helper.contains_lowercase_letters(test_string3))
    
    def test_contains_lowercase_letters_returns_false_when_false(self):
        test_string1 = """ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!()-.?[]_'~;:!@#$%^&*+="""
        test_string2 = "+358401234567"
        test_string3 = "MATTIMEIKÄLÄINEN123"
        self.assertFalse(Helper.contains_lowercase_letters(test_string1))
        self.assertFalse(Helper.contains_lowercase_letters(test_string2))
        self.assertFalse(Helper.contains_lowercase_letters(test_string3))

    # Uppercase Letters --------------------------------------------------------------------

    def test_contains_uppercase_letters_returns_true_when_true(self):
        test_string1 = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!()-.?[]_'~;:!@#$%^&*+=åäöÅÄÖ"""
        test_string2 = """abcdefghijklmnopqrstuvwxyzA0123456789!()-.?[]_'~;:!@#$%^&*+="""
        test_string3 = "mattiMeikäläinen123"
        self.assertTrue(Helper.contains_uppercase_letters(test_string1))
        self.assertTrue(Helper.contains_uppercase_letters(test_string2))
        self.assertTrue(Helper.contains_uppercase_letters(test_string3))
    
    def test_contains_uppercase_letters_returns_false_when_false(self):
        test_string1 = """abcdefghijklmnopqrstuvwxyz0123456789!()-.?[]_'~;:!@#$%^&*+="""
        test_string2 = "+358401234567"
        test_string3 = "mattimeikäläinen123"
        self.assertFalse(Helper.contains_uppercase_letters(test_string1))
        self.assertFalse(Helper.contains_uppercase_letters(test_string2))
        self.assertFalse(Helper.contains_uppercase_letters(test_string3))

    # Numbers --------------------------------------------------------------------

    def test_contains_numbers_returns_true_when_true(self):
        test_string1 = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!()-.?[]_'~;:!@#$%^&*+=åäöÅÄÖ"""
        test_string2 = """abcdefghijklmnopqrstuvwxy0zABCDEFGHIJKLMNOPQRSTUVWXYZ!()-.?[]_'~;:!@#$%^&*+="""
        test_string3 = "mattiMeikäläinen123"
        self.assertTrue(Helper.contains_numbers(test_string1))
        self.assertTrue(Helper.contains_numbers(test_string2))
        self.assertTrue(Helper.contains_numbers(test_string3))
    
    def test_contains_numbers_returns_false_when_false(self):
        test_string1 = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!()-.?[]_'~;:!@#$%^&*+="""
        test_string2 = "huonomonotypesalasana"
        test_string3 = "mattiMeikäläinen"
        self.assertFalse(Helper.contains_numbers(test_string1))
        self.assertFalse(Helper.contains_numbers(test_string2))
        self.assertFalse(Helper.contains_numbers(test_string3))

    # Special Characters --------------------------------------------------------------------

    def test_contains_special_characters_returns_true_when_true(self):
        test_string1 = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!()-.?[]_'~;:!@#$%^&*+=åäöÅÄÖ"""
        test_string2 = """abcdefghijklmnopqrstuvwxyz.ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"""
        test_string3 = "mattiMeikäläinen123!"
        self.assertTrue(Helper.contains_special_characters(test_string1))
        self.assertTrue(Helper.contains_special_characters(test_string2))
        self.assertTrue(Helper.contains_special_characters(test_string3))
    
    def test_contains_special_characters_returns_false_when_false(self):
        test_string1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        test_string2 = "314159265359"
        test_string3 = "mattiMeikäläinen123"
        self.assertFalse(Helper.contains_special_characters(test_string1))
        self.assertFalse(Helper.contains_special_characters(test_string2))
        self.assertFalse(Helper.contains_special_characters(test_string3))
    
    # Valid usernames --------------------------------------------------------------------

    def test_is_valid_username_returns_true_when_true(self):
        test_name1 = "TheMachine"
        test_name2 = "0f**ksGiven"
        test_name3 = "mattiMeikäläinen123"
        test_name4 = "janitor69"
        self.assertTrue(Helper.is_valid_username(test_name1))
        self.assertTrue(Helper.is_valid_username(test_name2))
        self.assertTrue(Helper.is_valid_username(test_name3))
        self.assertTrue(Helper.is_valid_username(test_name4))
    
    def test_is_valid_username_returns_false_when_false(self):
        test_name1 = ""
        test_name2 = " "
        test_name3 = "matti,Meikäläinen123"
        test_name4 = "jani"
        test_name5 = "".join(["a" for x in range(201)])
        test_name6 = ".gitignore"
        test_name7 = "0.?5$9%+2*"
        self.assertFalse(Helper.is_valid_username(test_name1))
        self.assertFalse(Helper.is_valid_username(test_name2))
        self.assertFalse(Helper.is_valid_username(test_name3))
        self.assertFalse(Helper.is_valid_username(test_name4))
        self.assertFalse(Helper.is_valid_username(test_name5))
        self.assertFalse(Helper.is_valid_username(test_name6))
        self.assertFalse(Helper.is_valid_username(test_name7))

    # Valid passwords --------------------------------------------------------------------

    def test_is_valid_password_returns_true_when_true(self):
        test_name1 = "TheMachine69!"
        test_name2 = "0f**ksGiven"
        test_name3 = "matti.Meikäläinen123"
        test_name4 = "Janitor#69"
        self.assertTrue(Helper.is_valid_password(test_name1))
        self.assertTrue(Helper.is_valid_password(test_name2))
        self.assertTrue(Helper.is_valid_password(test_name3))
        self.assertTrue(Helper.is_valid_password(test_name4))
  
    
    def test_is_valid_password_returns_false_when_false(self):
        test_name1 = ""
        test_name2 = " "
        test_name3 = "matti,Meikäläinen123"
        test_name4 = "jani"
        test_name5 = "".join(["a" for x in range(201)])
        test_name6 = ".gitignore"
        test_name7 = "ABC123.!#"
        test_name8 = "abc123.!#"
        test_name9 = "abcABC.!#"
        test_name10 = "abcABC123"
        self.assertFalse(Helper.is_valid_password(test_name1))
        self.assertFalse(Helper.is_valid_password(test_name2))
        self.assertFalse(Helper.is_valid_password(test_name3))
        self.assertFalse(Helper.is_valid_password(test_name4))
        self.assertFalse(Helper.is_valid_password(test_name5))
        self.assertFalse(Helper.is_valid_password(test_name6))
        self.assertFalse(Helper.is_valid_password(test_name7))
        self.assertFalse(Helper.is_valid_password(test_name8))
        self.assertFalse(Helper.is_valid_password(test_name9))
        self.assertFalse(Helper.is_valid_password(test_name10))

    # Valid names --------------------------------------------------------------------

    def test_is_valid_name_returns_true_when_true(self):
        test_name1 = "Taneli"
        test_name2 = "Härkönen"
        test_name3 = "Matti"
        test_name4 = "Meikäläinen"
        test_name5 = "Liu"
        test_name6 = "Hu"
        test_name7 = "Wolfeschlegelsteinhausenbergerdorff"
        self.assertTrue(Helper.is_valid_name(test_name1))
        self.assertTrue(Helper.is_valid_name(test_name2))
        self.assertTrue(Helper.is_valid_name(test_name3))
        self.assertTrue(Helper.is_valid_name(test_name4))
        self.assertTrue(Helper.is_valid_name(test_name5))
        self.assertTrue(Helper.is_valid_name(test_name6))
        self.assertTrue(Helper.is_valid_name(test_name7))

    
    def test_is_valid_name_returns_false_when_false(self):
        test_name1 = ""
        test_name2 = " "
        test_name3 = "matti,Meikäläinen123"
        test_name4 = "Taneli Härkönen"
        test_name5 = "".join(["a" for x in range(201)])
        test_name6 = ".gitignore"
        test_name7 = "0.?5$9%+2*"
        self.assertFalse(Helper.is_valid_name(test_name1))
        self.assertFalse(Helper.is_valid_name(test_name2))
        self.assertFalse(Helper.is_valid_name(test_name3))
        self.assertFalse(Helper.is_valid_name(test_name4))
        self.assertFalse(Helper.is_valid_name(test_name5))
        self.assertFalse(Helper.is_valid_name(test_name6))
        self.assertFalse(Helper.is_valid_name(test_name7))

