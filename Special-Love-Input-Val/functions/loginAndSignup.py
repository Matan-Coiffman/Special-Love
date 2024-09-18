from functions import data_handle, check_handle


def set_user_name():
    return input('Enter your name: ')


def set_age():
    return input('Enter your second name: ')


def set_user_phone():
    return input('Enter your phone number: ')


def set_user_password():
    return input('Enter your password: ')


#
def validate_signup(user):
    """Validate the phone number and password inputs."""
    phone_number = user.phone_input.text()
    password = user.password_input.text()
    age = user.age_input.text()

    # Validate phone number
    if not check_handle.check_phone_number(phone_number):
        user.show_message("Invalid Input",
                          "The phone number format is invalid.")
        return

    # Validate password
    if not check_handle.is_strong_password(password):
        user.show_message("Invalid Input",
                          "Password must be at least 8 characters long and "
                          "contain both letters and numbers.")
        return

    if not check_handle.check_age(age):
        user.show_message("Age must be a number")
        return

    data_handle.add_user_info([name, age, password, phone_number])

    user.show_message("Success", "Signup successful!")


class User:
    name = set_user_name()
    password = set_user_password()
    age = set_age()
    phone = set_user_phone()
    hobbies = []
    interests = []
