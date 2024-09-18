from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from functions import check_handle
from functions.check_handle import add_user_info, check_string_name, check_age, \
    is_strong_password, check_phone_number


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

        # Input fields
        self.first_name_input = QLineEdit()
        self.first_name_input.setPlaceholderText("First Name")
        layout.addWidget(self.first_name_input)

        self.last_name_input = QLineEdit()
        self.last_name_input.setPlaceholderText("Last Name")
        layout.addWidget(self.last_name_input)

        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Age")
        layout.addWidget(self.age_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        self.phone_number_input = QLineEdit()
        self.phone_number_input.setPlaceholderText("Phone Number")
        layout.addWidget(self.phone_number_input)

        # Sign Up Button
        signup_button = QPushButton('Submit')
        signup_button.clicked.connect(self.validate_signup)
        layout.addWidget(signup_button)

        # Back Button
        back_button = QPushButton('Back')
        back_button.clicked.connect(self.go_back)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def validate_signup(self):
        # Get the input values
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        age = self.age_input.text()
        password = self.password_input.text()
        phone_number = self.phone_number_input.text()

        # Validate the inputs
        if not check_string_name(first_name):
            self.show_message("Invalid Input", "First name is invalid.")
            return
        if not check_string_name(last_name):
            self.show_message("Invalid Input", "Last name is invalid.")
            return
        if not check_age(age):
            self.show_message("Invalid Input", "Age must be between 18 and 120.")
            return
        if not is_strong_password(password):
            self.show_message("Invalid Input", "Password must be at least 8 characters long and contain both letters and numbers.")
            return
        if not check_phone_number(phone_number):
            self.show_message("Invalid Input", "Phone number must be 10 digits.")
            return

        # Add the user to the database
        add_user_info(first_name, last_name, age, password, phone_number)
        self.show_message("Success", "Signup successful!")

    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()

    def go_back(self):
        self.stack.setCurrentIndex(0)
