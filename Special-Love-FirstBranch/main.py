import sys

from PyQt6.QtWidgets import QApplication

from GUI.HomePage import DatingAppHomepage
from functions import data_handle, check_handle, loginAndSignup


if __name__ == '__main__':
    app = QApplication(sys.argv)
    homepage = DatingAppHomepage()  # Create an instance of the home page
    sys.exit(app.exec())
