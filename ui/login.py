# login.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

from functions import check_handle


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
        check_handle.check_phone_number(self.phone_number_input)
        self.phone_number_input.setPlaceholderText('Phone Number')
        layout.addWidget(self.phone_number_input)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setPlaceholderText('Password')
        layout.addWidget(self.password_input)

        # Login Button
        login_button = QPushButton('Login')
        layout.addWidget(login_button)

        # Back Button
        back_button = QPushButton('Back')
        back_button.clicked.connect(self.go_back)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def go_back(self):
        # Navigate back to the homepage
        self.stack.setCurrentIndex(0)
