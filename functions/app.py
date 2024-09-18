import sys

from PyQt6.QtWidgets import QApplication, QMessageBox
from flask import Flask

from functions import check_handle, loginAndSignup
import data_handle


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


def show_message(self, title, message):
    """Show a message box with the given title and message."""
    msg_box = QMessageBox()
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    msg_box.exec()
