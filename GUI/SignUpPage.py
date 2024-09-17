from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QPushButton


def __init__(self):
    super().__init__()

    self.setWindowTitle('Signup')
    self.setGeometry(100, 100, 300, 600)

    layout = QVBoxLayout()

    title_label = QLabel('Create an Account')
    title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    title_label.setFont(QFont('Arial', 18))
    layout.addWidget(title_label)

    # Add input fields for signup (e.g., username, email, password)
    username_label = QLabel('Username:')
    self.username_input = QLineEdit()
    layout.addWidget(username_label)
    layout.addWidget(self.username_input)

    # ... (Add more input fields as needed)

    signup_button = QPushButton('Signup')
    layout.addWidget(signup_button)

    self.setLayout(layout)