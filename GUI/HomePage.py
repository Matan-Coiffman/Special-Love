from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton


class DatingAppHomepage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My Dating App')
        self.setGeometry(100, 100, 300, 600)  # Adjust size as needed

        layout = QVBoxLayout()

        # Welcome Message
        welcome_label = QLabel('Welcome to My Dating App!')
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_label.setFont(QFont('Arial', 20))  # Make it stand out
        layout.addWidget(welcome_label)

        self.login_button = QPushButton('Login')
        layout.addWidget(self.login_button)

        # Signup Button (Sign Up)
        self.signup_button = QPushButton('Signup')
        layout.addWidget(self.signup_button)

        self.setLayout(layout)

