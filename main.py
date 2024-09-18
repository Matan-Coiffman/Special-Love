import sys

from PyQt6.QtWidgets import QApplication, QStackedWidget

from ui.homePage import Homepage
from ui.signUp import SignUpPage

app = QApplication(sys.argv)

# Stack for switching between pages
stack = QStackedWidget()

# Pages
homepage = Homepage(stack)
signup_page = SignUpPage(stack)

# Add pages to the stack
stack.addWidget(homepage)
stack.addWidget(signup_page)

# Start with the homepage
stack.setCurrentIndex(0)
stack.show()

sys.exit(app.exec())
