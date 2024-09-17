import sys
import flaskProject
from PyQt6.QtWidgets import QApplication

from GUI.HomePage import DatingAppHomepage
from flaskProject import Navigation
from flaskProject.app import SignupPage

if __name__ == '__main__':
    app = QApplication(sys.argv)
    homepage = DatingAppHomepage()  # Create an instance of the home page
    signup_page = SignupPage()  # Create an instance of the signup page
    homepage.show()

    Navigation.switch_page(homepage, signup_page)
    sys.exit(app.exec())

