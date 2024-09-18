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

        def create_validated_input(placeholder, validation_function,
                                   echo_mode=None):
            """Creates a QLineEdit with input validation."""
            input_field = QLineEdit()
            input_field.setPlaceholderText(placeholder)
            if echo_mode:
                input_field.setEchoMode(echo_mode)

            while not validation_function(input_field.text()):
                # Provide a specific error message here
                QMessageBox.information(None, f"{placeholder} Invalid",
                                        "Try Again.")
                input_field = QLineEdit()
                input_field.setPlaceholderText(placeholder)
                if echo_mode:
                    input_field.setEchoMode(echo_mode)
            return input_field
        # Title
        title_label = QLabel('Sign Up')
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QFont('Arial', 20))
        layout.addWidget(title_label)

        # Input Fields
        self.first_name_input = create_validated_input(
                "First Name", check_handle.check_string_name
        )
        layout.addWidget(self.first_name_input)

        self.last_name_input = create_validated_input(
                "Last Name", check_handle.check_string_name
        )
        layout.addWidget(self.last_name_input)

        self.password_input = create_validated_input(
                "Password", check_handle.check_password,
                echo_mode=QLineEdit.EchoMode.Password
        )
        layout.addWidget(self.password_input)

        self.age_input = create_validated_input(
                "Age", lambda age: check_handle.check_age(age.text())
        )
        layout.addWidget(self.age_input)

        self.gender_input = QComboBox()
        self.gender_input.addItems(['Male', 'Female', 'Other'])
        layout.addWidget(self.gender_input)

        self.phone_number_input = create_validated_input(
                "Phone Number", check_handle.check_phone_number
        )
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
