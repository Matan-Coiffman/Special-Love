from PyQt6.QtWidgets import QPushButton

from flaskProject import check_handle


def switch_page(current_page, new_page):
    """Switches from the current page to the new page."""
    current_page.hide()
    new_page.show()


def switch_page_on_button_click(button: QPushButton, current_page, new_page):
    button.clicked.connect(lambda: switch_page(current_page, new_page))


