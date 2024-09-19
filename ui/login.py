from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, \
    QPushButton, QMessageBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from functions.data_handle import get_user_info_by_phone
from pages import match_page


class LoginPage(QWidget):

    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        self.setWindowTitle('Login')
        self.setGeometry(100, 100, 600, 900)

        layout = QVBoxLayout()

        title_label = QLabel('Login')
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QFont('Arial', 20))
        layout.addWidget(title_label)

        self.phone_number_input = QLineEdit()
        self.phone_number_input.setPlaceholderText("Phone Number")
        layout.addWidget(self.phone_number_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        login_button = QPushButton('Login')
        login_button.clicked.connect(self.validate_login)
        layout.addWidget(login_button)

        self.stack.setCurrentIndex(3)

        back_button = QPushButton('Back')
        back_button.clicked.connect(self.go_back)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def validate_login(self):
        phone_number = self.phone_number_input.text()
        password = self.password_input.text()

        # Check if user exists in the database
        user_info = get_user_info_by_phone(phone_number)
        if user_info is None:
            self.show_message("Error", "User does not exist.")
            return

        if user_info['password'] != password:
            self.show_message("Error", "Incorrect password.")
            return

        self.show_message("Success", "Login successful!")
        print(
            f"User {user_info['first_name']} {user_info['last_name']} logged in successfully!")

        file_path = 'C://Users//jbt//PycharmProjects//Special-Love//user_info.csv'
        profiles = match_page.get_users_dictionary(file_path)
        print('hello')

        # Create and add the MatchPage widget
        match_page_widget = match_page.MatchPage(self.stack, profiles)
        if match_page_widget not in self.stack.widgets():
            self.stack.addWidget(match_page_widget)

        self.stack.setCurrentWidget(match_page_widget)  # Set to the new page
        self.stack.show()

    def go_back(self):
        self.stack.setCurrentIndex(0)

    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()
