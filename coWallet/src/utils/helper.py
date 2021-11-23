import string

class Helper:
    
    special_characters = """!()-.?[]_'~;:!@#$%^&*+="""
    lowercase_letters = string.ascii_lowercase + "åäö"
    uppercase_letters = string.ascii_uppercase + "ÅÄÖ"
    letters = lowercase_letters + uppercase_letters

    def consists_of_legal_characters(word:str) -> bool:
        legal_characters = Helper.letters + string.digits + Helper.special_characters
        return not any([char not in legal_characters for char in word])
    
    def contains_letters(word:str) -> bool:
        return any([char in Helper.letters for char in word])
    
    def contains_lowercase_letters(word:str) -> bool:
        return any([char in Helper.lowercase_letters for char in word])

    def contains_uppercase_letters(word:str) -> bool:
        return any([char in Helper.uppercase_letters for char in word])
    
    def contains_numbers(word:str) -> bool:
        return any([char in string.digits for char in word])
    
    def contains_special_characters(word:str) -> bool:
        return any([char in Helper.special_characters for char in word])

    def is_valid_username(username:str) -> bool:
        if not bool(username):
            return False
        elif username.isspace():
            return False
        elif not Helper.consists_of_legal_characters(username):
            return False
        elif len(username) < 6:
            return False
        elif len(username) > 200:
            return False
        elif Helper.contains_special_characters(username[0]):
            return False
        elif not Helper.contains_letters(username):
            return False
        return True
    
    def is_valid_password(password:str) -> bool:
        if not bool(password):
            return False
        elif password.isspace():
            return False
        elif not Helper.consists_of_legal_characters(password):
            return False
        elif len(password) < 8:
            return False
        elif len(password) > 200:
            return False
        elif Helper.contains_special_characters(password[0]):
            return False
        elif not Helper.contains_lowercase_letters(password):
            return False
        elif not Helper.contains_uppercase_letters(password):
            return False
        elif not Helper.contains_numbers(password):
            return False
        elif not Helper.contains_special_characters(password):
            return False
        return True
    
    def is_valid_name(name:str) -> bool:
        if not bool(name):
            return False
        elif name.isspace():
            return False
        elif not Helper.consists_of_legal_characters(name):
            return False
        elif len(name) > 200:
            return False
        elif not Helper.contains_letters(name[0]):
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
