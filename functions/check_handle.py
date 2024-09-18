# Function to check if a username contains any digits
import re

from PyQt6.QtWidgets import QMessageBox


def validate_signup(self):
    """Validate the phone number and password inputs."""
    phone_number = self.phone_input.text()
    password = self.password_input.text()
    age = self.age_input.text()

    # Validate phone number
    if not check_phone_number(phone_number):
        self.show_message("Invalid Input",
                          "The phone number format is invalid.")
        return

    # Validate password
    if not is_strong_password(password):
        self.show_message("Invalid Input",
                          "Password must be at least 8 characters long and "
                          "contain both letters and numbers.")
        return

    if not check_age(age):
        self.show_message("Age must be a number")
        return

    self.show_message("Success", "Signup successful!")




def is_strong_password(password):
    """Check if the password meets certain strength requirements."""
    if len(password) < 8:
        return False
    has_letter = any(char.isalpha() for char in password)
    has_number = any(char.isdigit() for char in password)
    return has_letter and has_number


def check_age(age):
    try:
        if type(age) == int:
            return True
    except:
        print("Age Must Be a Number. Try Again.")
        return False
    return False


def check_string_name(name):
    """Check if the name is valid."""
    if len(name) < 2:
        print("Name Must Be At Least 2 Characters Long. Try Again.")
        return False
    if not name.isalpha():
        print("Name Must Contain Only Letters. Try Again.")
        return False
    return True


def check_phone_number(phone_number):
    """Check if the phone number is valid."""
    if len(phone_number) != 10:
        print("Phone Number Must Be 10 Digits Long. Try Again.")
        return False
    if not phone_number.isdigit():
        print("Phone Number Must Contain Only Digits. Try Again.")
        return False
    return True


def check_hobbies(hobbies):
    """Check if the hobbies are valid."""
    if len(hobbies) < 2:
        print("Hobbies Must Be At Least 2 Characters Long. Try Again.")
        return False
    return True


def check_gender(gender):
    """Check if the gender is valid."""
    if gender not in ['Male', 'Female', 'Other']:
        print(
                "Gender Must Be One Of The Following: Male, Female, Other. "
                "Try Again.")
        return False
    return True
