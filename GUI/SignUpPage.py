from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLineEdit, QPushButton, QLabel, QVBoxLayout, \
    QWidget

from functions.check_handle import check_string_name


class SignupPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Signup')
        self.setGeometry(100, 100, 300, 600)

        self.layout = QVBoxLayout()

        title_label = QLabel('Create an Account')
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QFont('Arial', 18))
        self.layout.addWidget(title_label)

        # Add input fields for signup (e.g., username, email, password)
        username_label = QLabel('Username:')
        self.username_input = QLineEdit()
        self.layout.addWidget(username_label)
        self.layout.addWidget(self.username_input)

        # Add more input fields as needed...

        signup_button = QPushButton('Signup')
        signup_button.clicked.connect(self.handle_signup)
        self.layout.addWidget(signup_button)

        self.setLayout(self.layout)

    # Function to handle the signup process
    def handle_signup(self):
        if not check_string_name(self.username_input.text()):
            print("Error: Invalid username (must not contain digits).")
        else:
            print(f"Signup successful! Username: {self.username_input.text()}")
