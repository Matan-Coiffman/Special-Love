# signup.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, \
    QPushButton, QComboBox, QMessageBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

from functions import check_handle


class SignUpPage(QWidget):
    def __init__(self, stack):
        super().__init__()

        self.stack = stack
        self.setWindowTitle('Sign Up')
        self.setGeometry(100, 100, 600, 900)

        layout = QVBoxLayout()

        # Title
        title_label = QLabel('Sign Up')
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QFont('Arial', 20))
        layout.addWidget(title_label)

        # Input Fields
        self.first_name_input = QLineEdit()
        self.first_name_input.setPlaceholderText('First Name')
        if not check_handle.check_string_name(self.first_name_input):
            QMessageBox.information(None, "Name Invalid, Try Again.")
        layout.addWidget(self.first_name_input)

        self.last_name_input = QLineEdit()
        self.last_name_input.setPlaceholderText('Last Name')
        if not check_handle.check_string_name(self.last_name_input):
            QMessageBox.information(None, "Last Name Invalid, Try Again.")
        layout.addWidget(self.last_name_input)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setPlaceholderText('Password')
        if not check_handle.check_password(self.password_input):
            QMessageBox.information(None, "Password Invalid, Try Again.")
        layout.addWidget(self.password_input)

        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText('Age')
        layout.addWidget(self.age_input)

        self.gender_input = QComboBox()
        self.gender_input.addItems(['Male', 'Female', 'Other'])
        layout.addWidget(self.gender_input)

        self.phone_number_input = QLineEdit()
        self.phone_number_input.setPlaceholderText('Phone Number')
        layout.addWidget(self.phone_number_input)

        # Sign Up Button
        signup_button = QPushButton('Submit')
        layout.addWidget(signup_button)

        # Back Button
        back_button = QPushButton('Back')
        back_button.clicked.connect(self.go_back)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def go_back(self):
        # Navigate back to the homepage
        self.stack.setCurrentIndex(0)
