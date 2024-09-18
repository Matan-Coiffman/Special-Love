from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from functions import check_handle
from functions.data_handle import get_user_info_by_phone


class LoginPage(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        self.setWindowTitle('Login')
        self.setGeometry(100, 100, 600, 900)

        layout = QVBoxLayout()

        # Title
        title_label = QLabel('Login')
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QFont('Arial', 20))
        layout.addWidget(title_label)

        # Input Fields
        self.phone_number_input = QLineEdit()
        self.phone_number_input.setPlaceholderText("Phone Number")
        layout.addWidget(self.phone_number_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        # Login Button
        login_button = QPushButton('Login')
        login_button.clicked.connect(self.validate_login)
        layout.addWidget(login_button)

        # Back Button
        back_button = QPushButton('Back')
        back_button.clicked.connect(self.go_back)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def validate_login(self):
        phone_number = self.phone_number_input.text()
        password = self.password_input.text()

        # Validate phone number format
        if not check_handle.check_phone_number(phone_number):
            self.show_message("Invalid Input", "Phone number must be 10 digits.")
            return

        # Check if user exists in the database
        user_info = get_user_info_by_phone(phone_number)
        if user_info is None:
            self.show_message("Error", "User does not exist.")
            return

        # Check if the password matches
        if user_info['password'] != password:
            self.show_message("Error", "Incorrect password.")
            return

        # Successful login
        self.show_message("Success", "Login successful!")
        print(f"User {user_info['first_name']} {user_info['last_name']} logged in successfully!")

    def go_back(self):
        self.stack.setCurrentIndex(0)

    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()
