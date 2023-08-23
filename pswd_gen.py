import random
import string


def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pswd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pswd) < min_length:
        new_char = random.choice(characters)
        pswd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special


generate_password(10)
