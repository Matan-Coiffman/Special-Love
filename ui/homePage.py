# homepage.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from functions.check_handle import is_valid_phone_number, is_strong_password

class Homepage(QWidget):
    def __init__(self, stack):
        super().__init__()

        self.stack = stack  # Reference to QStackedWidget for navigation
        self.setWindowTitle('Welcome to My Dating App')
        self.setGeometry(100, 100, 600, 900)

        layout = QVBoxLayout()

        # Welcome Message
        welcome_label = QLabel('Welcome to My Dating App!')
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_label.setFont(QFont('Arial', 24))  # Make it stand out
        layout.addWidget(welcome_label)

        # Sign Up Button
        signup_button = QPushButton('Sign Up')
        signup_button.clicked.connect(self.go_to_signup)
        layout.addWidget(signup_button)

        # Login Button
        login_button = QPushButton('Login')
        login_button.clicked.connect(self.go_to_login)
        layout.addWidget(login_button)

        self.setLayout(layout)

    def go_to_signup(self):
        # Navigate to the Sign Up page
        self.stack.setCurrentIndex(1)

    def go_to_login(self):
        # Navigate to the Login page
        self.stack.setCurrentIndex(2)
