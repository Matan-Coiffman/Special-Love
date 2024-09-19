import sys

from PyQt6.QtWidgets import QApplication, QStackedWidget

from ui.homePage import Homepage
from ui.signUp import SignUpPage
from ui.login import LoginPage
from pages import match_page

if __name__ == "__main__":

    app = QApplication(sys.argv)

    stack = QStackedWidget()
    homepage = Homepage(stack)
    signup_page = SignUpPage(stack)
    login_page = LoginPage(stack)

    stack.addWidget(homepage)
    stack.addWidget(signup_page)
    stack.addWidget(login_page)


    stack.setCurrentIndex(0)
    stack.show()

    sys.exit(app.exec())
