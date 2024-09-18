import sys

from PyQt6.QtWidgets import QApplication, QStackedWidget

from ui.homePage import Homepage
from ui.signUp import SignUpPage
from ui.login import LoginPage

app = QApplication(sys.argv)

# Stack for switching between pages
stack = QStackedWidget()

# Pages
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
