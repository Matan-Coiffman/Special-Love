from functions import data_handle, check_handle



def set_user_name():
    return input('Enter your name: ')


def set_user_sec_name():
    return input('Enter your second name: ')


def set_user_phone():
    return input('Enter your phone number: ')


def set_user_password():
    return input('Enter your password: ')


def handle_user_creation():  # פונקציה שמטפלת באופן כללי ביצירת המשתמש
    user_info = create_user()
    for i in range(2):
        if not check_handle.check_string_name(user_info[i]):
            print('Error at \'app.py\' line 14 - check names  function')
    if not check_handle.is_strong_password(user_info[2]):
        print('Error at \'app.py\' line 16 - check password function')
    if not check_handle.check_phone_number(3):
        print('Error at \'app.py\' line 18 - check phone number function')
    data_handle.add_user_info(user_info[0], user_info[1], user_info[2],
                              user_info[i])


def create_user():
    try:
        u_name = set_user_name()
        u_sec_name = set_user_sec_name()
        u_pass = set_user_password()
        u_phone = set_user_phone()
    except ValueError:
        print('Error')
    return u_name, u_sec_name, u_pass, u_phone


