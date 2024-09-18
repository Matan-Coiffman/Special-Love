import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, \
    QLineEdit, QPushButton, QMessageBox, QStackedWidget
from PyQt6.QtCore import Qt

from functions import check_handle, loginAndSignup
from ui.homePage import Homepage
from ui.login import LoginPage
from ui.signUp import SignUpPage


class SignupWindow(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        # Set window title
        self.setWindowTitle("Signup Form")

        # Create layout
        layout = QVBoxLayout()

        # Title
        title_label = QLabel('Sign Up')
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        # Input Fields
        self.first_name_input = QLineEdit()
        self.first_name_input.setPlaceholderText("First Name")
        layout.addWidget(self.first_name_input)

        self.last_name_input = QLineEdit()
        self.last_name_input.setPlaceholderText("Last Name")
        layout.addWidget(self.last_name_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Age")
        layout.addWidget(self.age_input)

        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Phone Number")
        layout.addWidget(self.phone_input)

        # Signup button
        self.signup_button = QPushButton("Sign Up")
        self.signup_button.clicked.connect(self.validate_signup)
        layout.addWidget(self.signup_button)

        # Back Button
        back_button = QPushButton('Back')
        back_button.clicked.connect(self.go_back)
        layout.addWidget(back_button)

        # Set the layout to the window
        self.setLayout(layout)

    def validate_signup(self):
        """Validate the phone number and password inputs."""
        first_name = self.first_name_input.text()
        last_name = self.last_name_input.text()
        phone_number = self.phone_input.text()
        password = self.password_input.text()
        age = self.age_input.text()

        # Validate phone number
        if not check_handle.check_phone_number(phone_number):
            self.show_message("Invalid Input",
                              "The phone number format is invalid.")
            return

        # Validate password
        if not check_handle.is_strong_password(password):
            self.show_message("Invalid Input",
                              "Password must be at least 8 characters long and "
                              "contain both letters and numbers.")
            return

        if not check_handle.check_age(age):
            self.show_message("Age must be a number")
            return

        self.show_message("Success", "Signup successful!")

    def show_message(self, title, message):
        """Show a message box with the given title and message."""
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()

    def go_back(self):
        # Navigate back to the homepage
        self.stack.setCurrentIndex(0)


# Main Application
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create the QStackedWidget
    stack = QStackedWidget()

    # Add pages to the stack
    homepage = Homepage(stack)
    signup_page = SignupWindow(stack)
    login_page = LoginPage(stack)

    stack.addWidget(homepage)  # Index 0
    stack.addWidget(signup_page)  # Index 1
    stack.addWidget(login_page)  # Index 2

    # Show the initial homepage
    stack.setFixedSize(450, 600)
    stack.show()

    # Execute the application
    sys.exit(app.exec())