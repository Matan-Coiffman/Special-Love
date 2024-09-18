import re


def is_strong_password(password):
    if len(password) < 8:
        return False
    has_letter = any(char.isalpha() for char in password)
    has_number = any(char.isdigit() for char in password)
    return has_letter and has_number


def check_age(age):
    try:
        age = int(age)
        return 18 <= age <= 120  # Assuming a reasonable age range
    except ValueError:
        return False


def check_string_name(name):
    if len(name) < 2:
        return False
    if not name.isalpha():
        return False
    return True


def check_phone_number(phone_number):
    if len(phone_number) != 10:
        return False
    if not phone_number.isdigit():
        return False
    return True
