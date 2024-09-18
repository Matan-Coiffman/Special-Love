from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, \
    QPushButton, QMessageBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from functions import check_handle
from functions.check_handle import add_user_info, check_string_name, check_age, \
    is_strong_password, check_phone_number, user_exists


class LoginPage(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        self.setWindowTitle('Log In')
        self.setGeometry(100, 100, 600, 900)

        layout = QVBoxLayout()

        # Title
        title_label = QLabel('Log In')
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

        # Sign Up Button
        login_button = QPushButton('Submit')
        login_button.clicked.connect(self.validate_login())
        layout.addWidget(login_button)

        # Back Button
        back_button = QPushButton('Back')
        back_button.clicked.connect(self.go_back)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def validate_login(self):

        password = self.password_input.text()
        phone_number = self.phone_number_input.text()

        # Add the user to the database
        if user_exists(phone_number):
            self.show_message("Success", "Signup successful!")
        else:
            self.show_message("Failed", "Create an Account")

    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()

    def go_back(self):
        self.stack.setCurrentIndex(0)
