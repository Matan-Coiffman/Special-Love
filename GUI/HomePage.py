import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, \
    QPushButton, QLineEdit
from PyQt6.QtGui import QFont


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

        # Login/Signup Buttons
        login_button = QPushButton('Login')
        signup_button = QPushButton('Signup')
        layout.addWidget(login_button)
        layout.addWidget(signup_button)

        self.setLayout(layout)
