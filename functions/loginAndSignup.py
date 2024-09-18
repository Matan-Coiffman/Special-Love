import check_handle


def set_user_name():
    return input('Enter your name: ')


def set_user_sec_name():
    return input('Enter your second name: ')


def set_user_phone():
    return input('Enter your phone number: ')


def set_user_password():
    return input('Enter your password: ')


def handle_signup(self):
    if not check_handle.check_string_name(
            self.username.u_name) and check_handle.check_phone_number(
            self.username.u_phone) and check_handle.check_password(
            self.username.u_password):
        print("Error: Invalid")
    else:
        print(f"Signup successful!")


def create_user():
    try:
        u_name = set_user_name()
        u_sec_name = set_user_sec_name()
        u_pass = set_user_password()
        u_phone = set_user_phone()
    except ValueError:
        print('Error')
    return u_name, u_sec_name, u_pass, u_phone


