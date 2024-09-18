from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class Homepage(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        self.setWindowTitle('Welcome to My Dating App')
        self.setGeometry(100, 100, 600, 900)

        layout = QVBoxLayout()

        welcome_label = QLabel('Welcome to My Dating App!')
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_label.setFont(QFont('Arial', 24))
        layout.addWidget(welcome_label)

        signup_button = QPushButton('Sign Up')
        signup_button.clicked.connect(self.go_to_signup)
        layout.addWidget(signup_button)

        self.setLayout(layout)

    def go_to_signup(self):
        self.stack.setCurrentIndex(1)
