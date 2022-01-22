import sys
import unittest
from utils.helper import Helper
from datetime import datetime

class TestHelper(unittest.TestCase):

    # Legal Characters ----------------------------------------------------------------------------

    def test_consists_of_legal_characters_returns_true_when_true(self):
        all_legal_chars = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!()-.?[]_'~;:!@#$%^&*+=åäöÅÄÖ"""
        self.assertTrue(Helper.consists_of_legal_characters(all_legal_chars))
    
    def test_consists_of_legal_characters_returns_false_when_false(self):
        all_legal_chars = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!()-.?[]_'~;:!@#$%^&*+=åäöÅÄÖ"""
        illegal_chars = """",/<>\\`{|}"""
        self.assertFalse(Helper.consists_of_legal_characters(all_legal_chars + illegal_chars))
        self.assertFalse(Helper.consists_of_legal_characters(all_legal_chars + ","))
    
    # Letters -------------------------------------------------------------------------------------

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

    # Lowercase Letters ---------------------------------------------------------------------------

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

    # Uppercase Letters ---------------------------------------------------------------------------

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

    # Numbers -------------------------------------------------------------------------------------

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

    # Special Characters --------------------------------------------------------------------------

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
    
    # Valid usernames -----------------------------------------------------------------------------

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
        test_name8 = 23
        self.assertRaises(ValueError, lambda: Helper.is_valid_username(test_name1))
        self.assertRaises(ValueError, lambda: Helper.is_valid_username(test_name2))
        self.assertRaises(ValueError, lambda: Helper.is_valid_username(test_name3))
        self.assertRaises(ValueError, lambda: Helper.is_valid_username(test_name4))
        self.assertRaises(ValueError, lambda: Helper.is_valid_username(test_name5))
        self.assertRaises(ValueError, lambda: Helper.is_valid_username(test_name6))
        self.assertRaises(ValueError, lambda: Helper.is_valid_username(test_name7))
        self.assertRaises(ValueError, lambda: Helper.is_valid_username(test_name8))

    # Valid passwords -----------------------------------------------------------------------------

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
        test_name11 = 23
        self.assertRaises(ValueError, lambda: Helper.is_valid_password(test_name1))
        self.assertRaises(ValueError, lambda: Helper.is_valid_password(test_name2))
        self.assertRaises(ValueError, lambda: Helper.is_valid_password(test_name3))
        self.assertRaises(ValueError, lambda: Helper.is_valid_password(test_name4))
        self.assertRaises(ValueError, lambda: Helper.is_valid_password(test_name5))
        self.assertRaises(ValueError, lambda: Helper.is_valid_password(test_name6))
        self.assertRaises(ValueError, lambda: Helper.is_valid_password(test_name7))
        self.assertRaises(ValueError, lambda: Helper.is_valid_password(test_name8))
        self.assertRaises(ValueError, lambda: Helper.is_valid_password(test_name9))
        self.assertRaises(ValueError, lambda: Helper.is_valid_password(test_name10))
        self.assertRaises(ValueError, lambda: Helper.is_valid_password(test_name11))

    # Valid names ---------------------------------------------------------------------------------

    def test_is_valid_name_returns_true_when_true(self):
        test_name1 = "Taneli"
        test_name2 = "Härkönen"
        test_name3 = "Matti"
        test_name4 = "Meikäläinen"
        test_name5 = "Liu"
        test_name6 = "Hu"
        test_name7 = "Wolfeschlegelsteinhausenbergerdorff"
        test_name8 = "Taneli Härkönen"
        self.assertTrue(Helper.is_valid_name(test_name1))
        self.assertTrue(Helper.is_valid_name(test_name2))
        self.assertTrue(Helper.is_valid_name(test_name3))
        self.assertTrue(Helper.is_valid_name(test_name4))
        self.assertTrue(Helper.is_valid_name(test_name5))
        self.assertTrue(Helper.is_valid_name(test_name6))
        self.assertTrue(Helper.is_valid_name(test_name7))
        self.assertTrue(Helper.is_valid_name(test_name8))

    
    def test_is_valid_name_raises_valueerror_when_false(self):
        test_name1 = ""
        test_name2 = " "
        test_name3 = "matti|Meikäläinen123"
        test_name4 = "Taneli/\\Härkönen"
        test_name5 = "".join(["a" for x in range(201)])
        test_name6 = ".gitignore"
        test_name7 = "0.?5$9%+2*"
        test_name8 = "Taneli\nHärkönen"
        test_name9 = "Taneli\rHärkönen"
        test_name10 = "Taneli\tHärkönen"
        test_name11 = "Taneli,Härkönen"
        self.assertRaises(ValueError, lambda: Helper.is_valid_name(test_name1))
        self.assertRaises(ValueError, lambda: Helper.is_valid_name(test_name2))
        self.assertRaises(ValueError, lambda: Helper.is_valid_name(test_name3))
        self.assertRaises(ValueError, lambda: Helper.is_valid_name(test_name4))
        self.assertRaises(ValueError, lambda: Helper.is_valid_name(test_name5))
        self.assertRaises(ValueError, lambda: Helper.is_valid_name(test_name6))
        self.assertRaises(ValueError, lambda: Helper.is_valid_name(test_name7))
        self.assertRaises(ValueError, lambda: Helper.is_valid_name(test_name8))
        self.assertRaises(ValueError, lambda: Helper.is_valid_name(test_name9))
        self.assertRaises(ValueError, lambda: Helper.is_valid_name(test_name10))
        self.assertRaises(ValueError, lambda: Helper.is_valid_name(test_name11))


    # Short texts ---------------------------------------------------------------------------------

    def test_is_valid_short_text_returns_true_when_true(self):
        test_text1 = """Lorem ipsum dolor sit ame, consectetur adipiscing elit. Duis dolor purus, condimentum nec mauris eu, suscipit ornare velit. Praesent ligula leo, ullamcorper ac quam vel, iaculis tristique elit. Duis id ipsum dui. Nunc dignissim purus a mauris molestie vestibulum. In non auctor quam, id bibendum lacus. Nam euismod fringilla enim, sit amet pellentesque lacus tincidunt non. Nulla commodo finibus felis id scelerisque. Suspendisse at laoreet lorem. Phasellus convallis turpis sit amet nulla congue, quis gravida risus tincidunt. Nullam sed tortor porta tortor molestie venenatis nec non velit. Nam nisl quam, dictum et consectetur nec, aliquet et justo. Proin imperdiet, sapien a aliquam rhoncus, nibh purus sollicitudin leo, a sodales eros risus vel nulla. Integer malesuada dictum mi, vel tempus ligula vulputate id. Proin cursus nisl orci, et ultrices leo luctus aliquam. Mauris vestibulum bibendum augue, egestas maximus nulla auctor ullamcorper. Pellentesque habitant morbi tristique senectus e netus et malesuada nunc."""
        test_text2 = "abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ!()-.?[]_'~;:!@#$%^&*+= ,"
        self.assertTrue(Helper.is_valid_short_text(test_text1))
        self.assertTrue(Helper.is_valid_short_text(test_text2))
    
    def test_is_valid_short_text_raises_valueerror_when_false(self):
        test_text1 = "".join(["a" for x in range(1025)])
        test_text2 = 23
        self.assertRaises(ValueError, lambda: Helper.is_valid_short_text(test_text1))
        self.assertRaises(ValueError, lambda: Helper.is_valid_short_text(test_text2))

    # timestamps ----------------------------------------------------------------------------------

    def test_is_valid_timestamp_returns_true_when_true(self):
        timestamp1 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        timestamp2 = '2022-01-22 06:16:37'
        timestamp3 = '1992-03-20 23:30:00'
        timestamp4 = '1970-01-01 00:00:00'
        timestamp5 = '2000-01-01 00:00:00'
        self.assertTrue(Helper.is_valid_timestamp(timestamp1))
        self.assertTrue(Helper.is_valid_timestamp(timestamp2))
        self.assertTrue(Helper.is_valid_timestamp(timestamp3))
        self.assertTrue(Helper.is_valid_timestamp(timestamp4))
        self.assertTrue(Helper.is_valid_timestamp(timestamp5))

    def test_is_valid_timestamp_raises_valueerror_when_false(self):
        timestamp1 = '0000-00-00 00:00:00'
        timestamp2 = '2022-22-01 06:16:37'
        timestamp3 = '22-01-2022 06:16:37'
        timestamp4 = '01-22-2022 06:16:37'
        timestamp5 = '2022-01-22 24:00:00'
        timestamp6 = '9999-99-99 00:00:00'
        timestamp7 = '0000-00-00 99:99:99'
        timestamp8 = '2022:01:22 06:16:37'
        timestamp9 = '2022-01-22 06-16-37'
        timestamp10 = '2022-01-22-06:16:37'
        timestamp11 = '2022-01-2206:16:37'
        timestamp12 = '20220122061637'
        timestamp13 = 'Jan-22-2022 00:00:00'
        self.assertRaises(ValueError, lambda: Helper.is_valid_timestamp(timestamp1))
        self.assertRaises(ValueError, lambda: Helper.is_valid_timestamp(timestamp2))
        self.assertRaises(ValueError, lambda: Helper.is_valid_timestamp(timestamp3))
        self.assertRaises(ValueError, lambda: Helper.is_valid_timestamp(timestamp4))
        self.assertRaises(ValueError, lambda: Helper.is_valid_timestamp(timestamp5))
        self.assertRaises(ValueError, lambda: Helper.is_valid_timestamp(timestamp6))
        self.assertRaises(ValueError, lambda: Helper.is_valid_timestamp(timestamp7))
        self.assertRaises(ValueError, lambda: Helper.is_valid_timestamp(timestamp8))
        self.assertRaises(ValueError, lambda: Helper.is_valid_timestamp(timestamp9))
        self.assertRaises(ValueError, lambda: Helper.is_valid_timestamp(timestamp10))
        self.assertRaises(ValueError, lambda: Helper.is_valid_timestamp(timestamp11))
        self.assertRaises(ValueError, lambda: Helper.is_valid_timestamp(timestamp12))
        self.assertRaises(ValueError, lambda: Helper.is_valid_timestamp(timestamp13))

    # Conversions Checks --------------------------------------------------------------------------
    # Transaction types ---------------------------------------------------------------------------

    def test_convert_transaction_type_returns_correctly_when_legal(self):
        valid_transaction_type1 = 0
        valid_transaction_type2 = 1
        valid_transaction_type3 = 2
        valid_transaction_type4 = 'deposit'
        valid_transaction_type5 = 'withdraw'
        valid_transaction_type6 = 'purchase'
        valid_transaction_type7 = False
        valid_transaction_type8 = True
        self.assertEqual(Helper.convert_transaction_type(valid_transaction_type1), 0)
        self.assertEqual(Helper.convert_transaction_type(valid_transaction_type2), 1)
        self.assertEqual(Helper.convert_transaction_type(valid_transaction_type3), 2)
        self.assertEqual(Helper.convert_transaction_type(valid_transaction_type4), 0)
        self.assertEqual(Helper.convert_transaction_type(valid_transaction_type5), 1)
        self.assertEqual(Helper.convert_transaction_type(valid_transaction_type6), 2)
        self.assertEqual(Helper.convert_transaction_type(valid_transaction_type7), 0)
        self.assertEqual(Helper.convert_transaction_type(valid_transaction_type8), 1)

    def test_convert_transaction_type_raises_valueerror_when_illegal(self):
        invalid_transaction_type1 = -1
        invalid_transaction_type2 = 3
        invalid_transaction_type3 = None
        invalid_transaction_type4 = 'nosto'
        invalid_transaction_type5 = '0'
        invalid_transaction_type6 = '1'
        invalid_transaction_type7 = [1,2,3,4]
        invalid_transaction_type8 = {1:"yy", 2:"kaa", 3:"koo"}
        self.assertRaises(ValueError, lambda: Helper.convert_transaction_type(invalid_transaction_type1))
        self.assertRaises(ValueError, lambda: Helper.convert_transaction_type(invalid_transaction_type2))
        self.assertRaises(ValueError, lambda: Helper.convert_transaction_type(invalid_transaction_type3))
        self.assertRaises(ValueError, lambda: Helper.convert_transaction_type(invalid_transaction_type4))
        self.assertRaises(ValueError, lambda: Helper.convert_transaction_type(invalid_transaction_type5))
        self.assertRaises(ValueError, lambda: Helper.convert_transaction_type(invalid_transaction_type6))
        self.assertRaises(ValueError, lambda: Helper.convert_transaction_type(invalid_transaction_type7))
        self.assertRaises(ValueError, lambda: Helper.convert_transaction_type(invalid_transaction_type8))

    # Currency amounts ----------------------------------------------------------------------------

    def test_convert_currency_amount_returns_correctly_when_legal(self):
        valid_amount1 = 0
        valid_amount2 = 1
        valid_amount3 = 256
        valid_amount4 = 9589273492
        valid_amount5 = 0.0
        valid_amount6 = 1.0
        valid_amount7 = 1.637236339
        valid_amount8 = 56872.873265
        self.assertEqual(Helper.convert_currency_amount(valid_amount1), 0)
        self.assertEqual(Helper.convert_currency_amount(valid_amount2), 100)
        self.assertEqual(Helper.convert_currency_amount(valid_amount3), 25600)
        self.assertEqual(Helper.convert_currency_amount(valid_amount4), 958927349200)
        self.assertEqual(Helper.convert_currency_amount(valid_amount5), 0)
        self.assertEqual(Helper.convert_currency_amount(valid_amount6), 100)
        self.assertEqual(Helper.convert_currency_amount(valid_amount7), 164)
        self.assertEqual(Helper.convert_currency_amount(valid_amount8), 5687287)

    def test_convert_currency_amount_raises_valueerror_when_illegal(self):
        invalid_amount01 = -1
        invalid_amount02 = -(sys.maxsize * 2 + 1)
        invalid_amount03 = -256
        invalid_amount04 = -1.0
        invalid_amount05 = -0.5
        invalid_amount06 = -0.000000001
        invalid_amount07 = -387465.5726386
        invalid_amount08 = -1.87346827
        invalid_amount09 = 'amount of money'
        invalid_amount10 = '0'
        invalid_amount11 = '1.5'
        invalid_amount12 = [1,2,3,4]
        invalid_amount13 = {1:"yy", 2:"kaa", 3:"koo"}
        invalid_amount14 = None
        invalid_amount15 = 1 - 2
        self.assertRaises(ValueError ,lambda: Helper.convert_currency_amount(invalid_amount01))
        self.assertRaises(ValueError ,lambda: Helper.convert_currency_amount(invalid_amount02))
        self.assertRaises(ValueError ,lambda: Helper.convert_currency_amount(invalid_amount03))
        self.assertRaises(ValueError ,lambda: Helper.convert_currency_amount(invalid_amount04))
        self.assertRaises(ValueError ,lambda: Helper.convert_currency_amount(invalid_amount05))
        self.assertRaises(ValueError ,lambda: Helper.convert_currency_amount(invalid_amount06))
        self.assertRaises(ValueError ,lambda: Helper.convert_currency_amount(invalid_amount07))
        self.assertRaises(ValueError ,lambda: Helper.convert_currency_amount(invalid_amount08))
        self.assertRaises(ValueError ,lambda: Helper.convert_currency_amount(invalid_amount09))
        self.assertRaises(ValueError ,lambda: Helper.convert_currency_amount(invalid_amount10))
        self.assertRaises(ValueError ,lambda: Helper.convert_currency_amount(invalid_amount11))
        self.assertRaises(ValueError ,lambda: Helper.convert_currency_amount(invalid_amount12))
        self.assertRaises(ValueError ,lambda: Helper.convert_currency_amount(invalid_amount13))
        self.assertRaises(ValueError ,lambda: Helper.convert_currency_amount(invalid_amount14))
        self.assertRaises(ValueError ,lambda: Helper.convert_currency_amount(invalid_amount15))
