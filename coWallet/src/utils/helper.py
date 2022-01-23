from multiprocessing.sharedctypes import Value
import string
#import re
from datetime import datetime
from utils.config import NAME_MAX_LENGTH, SHORT_TEXT_MAX_LENGTH

class Helper:

    # Contains / Consists -------------------------------------------------------------------------

    special_characters = """!()-.?[]_'~;:!@#$%^&*+="""
    lowercase_letters = string.ascii_lowercase + "åäö"
    uppercase_letters = string.ascii_uppercase + "ÅÄÖ"
    letters = lowercase_letters + uppercase_letters

    @staticmethod
    def consists_of_legal_characters(word:str, xtra_chars:str = "") -> bool:
        legal_characters = Helper.letters + string.digits + Helper.special_characters
        legal_characters += xtra_chars
        return not any((char not in legal_characters for char in word))

    @staticmethod
    def contains_letters(word:str) -> bool:
        return any((char in Helper.letters for char in word))

    @staticmethod
    def contains_lowercase_letters(word:str) -> bool:
        return any((char in Helper.lowercase_letters for char in word))

    @staticmethod
    def contains_uppercase_letters(word:str) -> bool:
        return any((char in Helper.uppercase_letters for char in word))

    @staticmethod
    def contains_numbers(word:str) -> bool:
        return any((char in string.digits for char in word))

    @staticmethod
    def contains_special_characters(word:str) -> bool:
        return any((char in Helper.special_characters for char in word))

    @staticmethod
    def is_valid_id(id_value:int) -> bool:
        if not isinstance(id_value, int):
            raise ValueError("not an integer")
        if id_value < 0:
            raise ValueError("is negative")
        return True
    # Is Valid ------------------------------------------------------------------------------------
    @staticmethod
    def is_valid_username(username:str) -> bool:
        if not isinstance(username, str):
            raise ValueError("not a string of text")
        if not bool(username):
            raise ValueError("is empty")
        if username.isspace():
            raise ValueError("is only space characters")
        if not Helper.consists_of_legal_characters(username):
            raise ValueError("contains illegal characters")
        if len(username) < 6:
            raise ValueError("too short, minimum of 6 characters")
        if  NAME_MAX_LENGTH < len(username):
            raise ValueError(f"too long, maximum of {NAME_MAX_LENGTH} characters")
        if Helper.contains_special_characters(username[0]):
            raise ValueError("contains illegal special characters")
        if not Helper.contains_letters(username):
            raise ValueError("doesn't contain any letters")
        return True

    @staticmethod
    def is_valid_password(password:str) -> bool:
        if not isinstance(password, str):
            raise ValueError("not a string of text")
        if not bool(password):
            raise ValueError("is empty")
        if password.isspace():
            raise ValueError("is only space characters")
        if not Helper.consists_of_legal_characters(password):
            raise ValueError("contains illegal characters")
        if len(password) < 8:
            raise ValueError("too short, minimum of 8 characters")
        if  NAME_MAX_LENGTH < len(password):
            raise ValueError(f"too long, maximum of {NAME_MAX_LENGTH} characters")
        if Helper.contains_special_characters(password[0]):
            raise ValueError("starts with a special character")
        if not Helper.contains_lowercase_letters(password):
            raise ValueError("doesn't contain any lowercase letters")
        if not Helper.contains_uppercase_letters(password):
            raise ValueError("doesn't contain any uppercase letters")
        if not Helper.contains_numbers(password):
            raise ValueError("doesn't contain any numbers")
        if not Helper.contains_special_characters(password):
            raise ValueError("doesn't contain any special characters")
        return True

    @staticmethod
    def is_valid_name(name:str) -> bool:
        if not isinstance(name, str):
            raise ValueError("not a string of text")
        if not bool(name):
            raise ValueError("is empty")
        if name.isspace():
            raise ValueError("is only space characters")
        if not Helper.consists_of_legal_characters(name, xtra_chars=" "):
            raise ValueError("contains illegal characters")
        if  NAME_MAX_LENGTH < len(name):
            raise ValueError(f"too long, maximum of {NAME_MAX_LENGTH} characters")
        if not Helper.contains_letters(name[0]):
            raise ValueError("not starting with a letter")
        return True

    @staticmethod
    def is_valid_short_text(text:str) -> bool:
        if not isinstance(text, str):
            raise ValueError("not a string of text")
        if not Helper.consists_of_legal_characters(text, xtra_chars=" ,"):
            raise ValueError("contains illegal characters")
        if SHORT_TEXT_MAX_LENGTH < len(text):
            raise ValueError(f"too long, maximum of {SHORT_TEXT_MAX_LENGTH} characters")
        return True

    @staticmethod
    def is_valid_description(description:str) -> bool:
        if not isinstance(description, str):
            raise ValueError("description not a string of text")
        if not bool(description):
            raise ValueError("description is empty")
        if description.isspace():
            raise ValueError("description is only space characters")
        if not Helper.consists_of_legal_characters(description, xtra_chars=" ,"):
            raise ValueError("description contains illegal characters")
        if NAME_MAX_LENGTH < len(description):
            raise ValueError(f"description too long, max {NAME_MAX_LENGTH} chars")
        return True

    @staticmethod
    def is_valid_timestamp(timestamp:str) -> bool:
        # return re.match('\d{2}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', timestamp)
        datetime.strptime(timestamp,'%Y-%m-%d %H:%M:%S')
        return True

    # Conversions ---------------------------------------------------------------------------------

    @staticmethod
    def convert_transaction_type(transaction_type:'str/int/bool') -> int:
        transaction_types_str = ('deposit', 'withdraw', 'purchase')
        if isinstance(transaction_type, int) and 0 <= transaction_type <= 2:
            return transaction_type
        elif isinstance(transaction_type, str) and transaction_type in transaction_types_str:
            return transaction_types_str.index(transaction_type)
        else:
            raise ValueError(f"transaction_type: '{transaction_type}' not valid")

    @staticmethod
    def convert_to_euro(amount:'str/int/float') -> float:
        if not bool(amount):
            raise ValueError("amount is empty or zero")
        try:
            amount = float(amount)
        except ValueError as e:
            raise ValueError("amount not a number") from e
        if amount < 0:
            raise ValueError("amount is negative")
        if amount == 0:
            raise ValueError("amount is zero")
        return round(amount * 100, 0) / 100

    @staticmethod
    def convert_euro_to_cents(amount:'int/float') -> int:
        if not (isinstance(amount, int) or isinstance(amount, float)):
            raise ValueError("not 'int' or 'float'")
        if not 0 <= amount:
            raise ValueError("not non-negative")
        return amount * 100 if isinstance(amount, int) else int(round(amount * 100))

# if __name__ == "__main__":
#     username = "testUsername"
#     password = "abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ!()-.?[]_'~;:!@#$%^&*+="
#     first_name = "testFirstName"
#     last_name = "testLastName"
#     print(Helper.is_valid_username(username))
#     print(Helper.is_valid_password(password))
#     print(Helper.is_valid_name(first_name))
#     print(Helper.is_valid_name(last_name))
# import string
# special_characters = """!()-.?[]_'~;:!@#$%^&*+="""
# lowercase_letters = string.ascii_lowercase + "åäö"
# uppercase_letters = string.ascii_uppercase + "ÅÄÖ"
# letters = lowercase_letters + uppercase_letters + string.digits + special_characters
# all_string_chars = string.printable
# illegal_chars = "".join([char for char in all_string_chars if char not in letters])

# # illegal: ",/<>\\`{|} \t\n\r\x0b\x0c
