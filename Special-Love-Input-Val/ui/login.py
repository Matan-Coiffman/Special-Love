import self
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, \
    QPushButton, QMessageBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

from functions import check_handle, data_handle


class LoginPage(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        self.setWindowTitle('Login')
        self.setGeometry(100, 100, 600, 900)

        layout = QVBoxLayout()

        title_label = QLabel('Login')
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QFont('Arial', 20))
        layout.addWidget(title_label)

        self.phone_number_input = QLineEdit()
        self.phone_number_input.setPlaceholderText("Phone Number")
        layout.addWidget(self.phone_number_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(self.password_input)

        login_button = QPushButton('Login')
        login_button.clicked.connect(self.validate_login)
        layout.addWidget(login_button)

        back_button = QPushButton('Back')
        back_button.clicked.connect(self.go_back)
        layout.addWidget(back_button)

        self.setLayout(layout)


def validate_login(self):
    phone_number = self.phone_number_input.text()
    password = self.password_input.text()

    if not check_handle.check_phone_number(phone_number):
        show_message("Invalid Input", "Invalid phone number format.")
        return

    user_info = data_handle.get_user_info_by_phone(phone_number)

    if user_info is None:
        show_message("Error", "User not found.")
        return

    if user_info['password'] != password:
        show_message("Error", "Incorrect password.")
        return

    show_message("Success", "Login successful!")
    # Here you would typically navigate to the main app interface


def go_back(self):
    self.stack.setCurrentIndex(0)


def show_message(title, message):
    msg_box = QMessageBox()
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    msg_box.exec()
