from PyQt6.QtWidgets import QPushButton

from flaskProject import check_handle


# Function to switch between pages
def switch_page(current_page, new_page):
    current_page.hide()
    new_page.show()


# Function to connect button click to page switch
def switch_page_on_button_click(button: QPushButton, current_page, new_page):
    button.clicked.connect(lambda: switch_page(current_page, new_page))


