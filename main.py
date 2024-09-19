import sys

from PyQt6.QtWidgets import QApplication, QStackedWidget

from ui.homePage import Homepage
from ui.signUp import SignUpPage
from ui.login import LoginPage
from pages import match_page

if __name__ == "__main__":

    app = QApplication(sys.argv)

    # Stack for switching between pages
    stack = QStackedWidget()
    homepage = Homepage(stack)
    signup_page = SignUpPage(stack)
    login_page = LoginPage(stack)


    # Add pages to the stack
    stack.addWidget(homepage)
    stack.addWidget(signup_page)
    stack.addWidget(login_page)


    # Start with the homepage
    stack.setCurrentIndex(0)
    stack.show()

    sys.exit(app.exec())
