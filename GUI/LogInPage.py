from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLineEdit, QPushButton, QLabel, QVBoxLayout, \
    QWidget

from GUI.HomePage import DatingAppHomepage
from flaskProject.Navigation import switch_page_on_button_click
from flaskProject.check_handle import check_string_name


class LoginPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Login')
        self.setGeometry(100, 100, 300, 600)

        self.layout = QVBoxLayout()

        title_label = QLabel('Login')
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QFont('Arial', 18))
        self.layout.addWidget(title_label)

        # Add input fields for signup (e.g., username, email, password)
        username_label = QLabel('Username:')
        self.username_input = QLineEdit()
        self.layout.addWidget(username_label)
        self.layout.addWidget(self.username_input)

        # Add more input fields as needed...
        home_page = DatingAppHomepage()
        login_page = SignupPage()
        login_button = home_page.login_button
        login_button = QPushButton('Login')
        login_button.clicked.connect(self.handle_login())
        self.layout.addWidget(login_button)

        self.setLayout(self.layout)

        switch_page_on_button_click(login_button, home_page, login_page)
    # Function to handle the signup process
    def handle_login(self):
        if not check_string_name(self.username_input.text()):
            print("Error: Invalid username or password.")
        else:
            print(f"Login successful! Username: {self.username_input.text()}")
