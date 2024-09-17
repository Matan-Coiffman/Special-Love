
# Function to check if a username contains any digits
def check_string_name(text):
    for c in text:
        if c.isdigit():
            return False
    return True


# Function to check if a phone number is valid
def check_phone_number(phone_number):
    if not phone_number.isdigit() or len(phone_number) != 10 or phone_number[0] != '0' or phone_number[1] != '5':
        return False
    return True


# Function to check if a password is valid
def check_password(password):
    if len(password) >= 8 or len(password) <= 16:
        return False
    elif password.isdigit():
        return False
    elif check_string_name(password):
        return False
    elif password[0] != password[0].upper():
        return False
    return True