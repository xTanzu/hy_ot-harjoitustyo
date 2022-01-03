import string
from config import NAME_MAX_LENGTH, SHORT_TEXT_MAX_LENGTH

class Helper:

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
