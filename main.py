import sys

from PyQt6.QtWidgets import QApplication

from ui.homePage import Homepage
from ui.login import LoginPage
from ui.signUp import SignUpPage
from functions import data_handle, check_handle, loginAndSignup


def handle_user_creation():  # פונקציה שמטפלת באופן כללי ביצירת המשתמש
    user_info = loginAndSignup.create_user()
    for i in range(2):
        if not check_handle.check_string_name(user_info[i]):
            print('Error at \'app.py\' line 14 - check names  function')
    if not check_handle.check_password(user_info[2]):
        print('Error at \'app.py\' line 16 - check password function')
    if not check_handle.check_phone_number(3):
        print('Error at \'app.py\' line 18 - check phone number function')
    data_handle.add_user_info(user_info[0], user_info[1], user_info[2],
                              user_info[i])


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create the QStackedWidget
    stack = QStackedWidget()

    # Add pages to the stack
    homepage = Homepage(stack)
    signup_page = SignUpPage(stack)
    login_page = LoginPage(stack)

    stack.addWidget(homepage)  # Index 0
    stack.addWidget(signup_page)  # Index 1
    stack.addWidget(login_page)  # Index 2

    # Show the initial homepage
    stack.setFixedSize(450, 600)
    stack.show()

    sys.exit(app.exec())
