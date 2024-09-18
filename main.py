import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, \
    QLineEdit, QPushButton, QMessageBox, QStackedWidget
from functions.check_handle import is_valid_phone_number, is_strong_password, check_string_name, check_age
from ui.homePage import Homepage
from ui.login import LoginPage
from ui.signUp import SignUpPage


class SignupWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle("Signup Form")

        # Create layout
        layout = QVBoxLayout()

        # Name label and input
        self.name_label = QLabel("Name:")
        layout.addWidget(self.name_label)
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter your name")
        layout.addWidget(self.name_input)

        # Age label and input
        self.age_label = QLabel("Age:")
        layout.addWidget(self.age_label)
        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Enter your age")
        layout.addWidget(self.age_input)

        # Phone number label and input
        self.phone_label = QLabel("Phone Number:")
        layout.addWidget(self.phone_label)
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Enter your phone number")
        layout.addWidget(self.phone_input)

        # Password label and input
        self.password_label = QLabel("Password:")
        layout.addWidget(self.password_label)
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setPlaceholderText("Enter your password")
        layout.addWidget(self.password_input)

        # Signup button
        self.signup_button = QPushButton("Sign Up")
        self.signup_button.clicked.connect(self.validate_signup)
        layout.addWidget(self.signup_button)

        # Set the layout to the window
        self.setLayout(layout)

    def validate_signup(self):
        """Validate the name, age, phone number, and password inputs."""
        name = self.name_input.text()
        age = self.age_input.text()
        phone_number = self.phone_input.text()
        password = self.password_input.text()

        # Validate name
        if not check_string_name(name):
            self.show_message("Invalid Input", "The name format is invalid.")
            return

        # Validate phone number
        if not is_valid_phone_number(phone_number):
            self.show_message("Invalid Input", "The phone number format is invalid.")
            return

        # Validate password
        if not is_strong_password(password):
            self.show_message("Invalid Input", "Password must be at least 8 characters long and contain both letters and numbers.")
            return

        # If all validations pass
        self.show_message("Success", "Signup successful!")

    def show_message(self, title, message):
        """Show a message box with the given title and message."""
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()


# Main Application
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create the QStackedWidget
    stack = QStackedWidget()

    # Add pages to the stack
    homepage = Homepage(stack)
    signup_page = SignUpPage(stack)
    login_page = LoginPage(stack)

    stack.addWidget(homepage)  # Index 0
    stack.addWidget(signup_page)  # Index 1
    stack.addWidget(login_page)  # Index 2

    # Show the initial homepage
    stack.setFixedSize(450, 600)
    stack.show()

    # Execute the application
    sys.exit(app.exec())
