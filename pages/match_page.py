import sys
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, \
    QHBoxLayout, QStackedWidget, QApplication
from PyQt6.QtGui import QFont, QPixmap, QPainter, QBrush
from PyQt6.QtCore import Qt


class MatchPage(QWidget):
    def __init__(self, stack, profile_data):
        super().__init__()
        self.stack = stack
        self.profile_data = profile_data
        self.setWindowTitle('Match')

        # Layout
        layout = QVBoxLayout()

        # Title
        title_label = QLabel(f"Match Profile: {self.profile_data['name']}")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setFont(QFont('Arial', 20))
        layout.addWidget(title_label)

        # Display Profile Image in Circular Shape
        self.create_circular_profile_image(layout)

        # Display Profile Info
        self.create_profile_info(layout)

        # Accept and Reject Buttons
        button_layout = QHBoxLayout()
        reject_button = QPushButton('✖')
        reject_button.clicked.connect(self.reject_profile)
        button_layout.addWidget(reject_button)

        accept_button = QPushButton('✔')
        accept_button.clicked.connect(self.accept_profile)
        button_layout.addWidget(accept_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def create_circular_profile_image(self, layout):
        # Assuming the profile image is stored at 'image_path'
        image_path = self.profile_data.get('image_path', 'default_image.png')
        pixmap = QPixmap(image_path)

        # Create a circular mask
        size = min(pixmap.width(), pixmap.height())  # To make the image square
        circular_pixmap = QPixmap(size, size)
        circular_pixmap.fill(
            Qt.GlobalColor.transparent)  # Transparent background

        # Create a QPainter to draw the circular image
        painter = QPainter(circular_pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QBrush(pixmap))
        painter.drawEllipse(0, 0, size, size)
        painter.end()

        # Add the circular image to the QLabel
        image_label = QLabel()
        image_label.setPixmap(circular_pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(image_label)

    def create_profile_info(self, layout):
        # Example profile fields - customize as needed
        name_label = QLabel(f"Name: {self.profile_data['name']}")
        name_label.setFont(QFont('Arial', 16))
        layout.addWidget(name_label)

        age_label = QLabel(f"Age: {self.profile_data['age']}")
        age_label.setFont(QFont('Arial', 16))
        layout.addWidget(age_label)

        bio_label = QLabel(f"Bio: {self.profile_data['bio']}")
        bio_label.setFont(QFont('Arial', 16))
        layout.addWidget(bio_label)

    def accept_profile(self):
        # Logic for accepting the profile
        print("Profile accepted!")
        # Navigate to next match or perform the next action

    def reject_profile(self):
        # Logic for rejecting the profile
        print("Profile rejected!")
        # Navigate to next match or perform the next action



if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Example profile data
    profile_data = {
        'name': 'Jane Doe',
        'age': 29,
        'bio': 'Loves hiking, photography, and reading books.',
        'image_path': 'C:/Users/jbt/PycharmProjects/pythonProject2/Special-Love/pages/jbt.jpg'
        # Use the full path
    }

    # Stack for switching between pages
    stack = QStackedWidget()

    # Pages
    match_page = MatchPage(stack, profile_data)

    # Add pages to the stack
    stack.addWidget(match_page)

    # Start with the match page
    stack.setCurrentIndex(0)
    stack.show()

    sys.exit(app.exec())
