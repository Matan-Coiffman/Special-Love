import sys

from PyQt6.QtWidgets import QApplication, QPushButton
from flask import Flask

import check_handle
from GUI.HomePage import DatingAppHomepage
from GUI.SignUpPage import SignupPage
from flaskProject.Navigation import switch_page_on_button_click

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


if __name__ == '__main__':
    run_gui_app()
