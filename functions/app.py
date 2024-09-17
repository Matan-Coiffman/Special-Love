import sys

from PyQt6.QtWidgets import QApplication, QPushButton
from flask import Flask

import check_handle
from GUI.HomePage import DatingAppHomepage
from GUI.SignUpPage import SignupPage
import data_handle
import loginAndSignup

# http://127.0.0.1:5000

app = Flask(__name__)


def run_gui_app():
    # Create the QApplication instance (needed to run any PyQt application)
    qt_app = QApplication(sys.argv)

    # Create instances of the homepage and signup page
    home_page = DatingAppHomepage()
    signup_page = SignupPage()
    login_btn = home_page.login_button
    signup_btn = home_page.signup_button

    # Switch to signup page when the signup button is clicked
    switch_page_on_button_click(signup_btn,
                                home_page, signup_page)

    # Show the homepage and start the PyQt event loop
    home_page.show()
    sys.exit(qt_app.exec())


@app.route('/signup')
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
    app.run()
    data_handle.test()
    run_gui_app()
