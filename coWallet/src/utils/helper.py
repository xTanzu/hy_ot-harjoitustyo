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
        if not isinstance(id_value, int) \
            or id_value < 0:
            return False
        return True

    @staticmethod
    def is_valid_username(username:str) -> bool:
        if not isinstance(username, str) \
            or not bool(username) \
            or username.isspace() \
            or not Helper.consists_of_legal_characters(username) \
            or not 6 <= len(username) <= NAME_MAX_LENGTH \
            or Helper.contains_special_characters(username[0]) \
            or not Helper.contains_letters(username):
            return False
        return True

    @staticmethod
    def is_valid_password(password:str) -> bool:
        if not isinstance(password, str) \
            or not bool(password) \
            or password.isspace() \
            or not Helper.consists_of_legal_characters(password) \
            or not 8 <= len(password) <= NAME_MAX_LENGTH \
            or Helper.contains_special_characters(password[0]) \
            or not Helper.contains_lowercase_letters(password) \
            or not Helper.contains_uppercase_letters(password) \
            or not Helper.contains_numbers(password) \
            or not Helper.contains_special_characters(password):
            return False
        return True

    @staticmethod
    def is_valid_name(name:str) -> bool:
        if not isinstance(name, str) \
            or not bool(name) \
            or name.isspace() \
            or not Helper.consists_of_legal_characters(name, xtra_chars=" ") \
            or len(name) > NAME_MAX_LENGTH \
            or not Helper.contains_letters(name[0]):
            return False
        return True

    @staticmethod
    def is_valid_short_text(text:str) -> bool:
        if not isinstance(text, str) \
            or not Helper.consists_of_legal_characters(text, xtra_chars=" ,") \
            or len(text) > SHORT_TEXT_MAX_LENGTH:
            return False
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
