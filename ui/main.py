# main.py

import sys
from PyQt6.QtWidgets import QApplication, QStackedWidget
from homePage import Homepage
from signUp import SignUpPage
from login import LoginPage

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create the QStackedWidget
    stack = QStackedWidget()

    # Add pages to the stack
    homepage = Homepage(stack)
    signup_page = SignUpPage(stack)
    login_page = LoginPage(stack)

    stack.addWidget(homepage)    # Index 0
    stack.addWidget(signup_page) # Index 1
    stack.addWidget(login_page)  # Index 2

    # Show the initial homepage
    stack.setFixedSize(450, 600)
    stack.show()

    sys.exit(app.exec())
