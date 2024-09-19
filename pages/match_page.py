import sys
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, \
    QHBoxLayout, QStackedWidget, QApplication
from PyQt6.QtGui import QFont, QPixmap, QPainter, QBrush
from PyQt6.QtCore import Qt
import csv


def get_users_dictionary(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        data = [
            {
                'name': row['first_name'],
                'age': row['age'],
                'bio': f"Interest: {row.get('intrests', 'N/A')}, Hobby: {row.get('hobbies', 'N/A')}, Lifestyle: {row.get('lifestyle', 'N/A')}",
                'image_path': 'funny_image.png'
            }
            for row in csv_reader
        ]
    return data



class MatchPage(QWidget):
    def __init__(self, stack, profiles):
        super().__init__()
        self.stack = stack
        self.profiles = profiles
        self.current_profile_index = 0
        self.profile_data = self.profiles[self.current_profile_index]

        self.setWindowTitle('Match')

        self.layout = QVBoxLayout()

        self.title_label = QLabel(
                f"Match Profile: {self.profile_data['name']}")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setFont(QFont('Arial', 20))
        self.layout.addWidget(self.title_label)

        self.image_label = QLabel()
        self.layout.addWidget(self.image_label)
        self.create_circular_profile_image()

        self.name_label = QLabel()
        self.age_label = QLabel()
        self.bio_label = QLabel()
        self.create_profile_info()

        button_layout = QHBoxLayout()
        reject_button = QPushButton('✖')
        reject_button.clicked.connect(self.reject_profile)
        button_layout.addWidget(reject_button)

        accept_button = QPushButton('✔')
        accept_button.clicked.connect(self.accept_profile)
        button_layout.addWidget(accept_button)

        self.layout.addLayout(button_layout)
        self.setLayout(self.layout)

    def create_circular_profile_image(self):
        image_path = self.profile_data.get('image_path', 'default_image.png')
        pixmap = QPixmap(image_path)

        size = min(pixmap.width(), pixmap.height())
        circular_pixmap = QPixmap(size, size)
        circular_pixmap.fill(Qt.GlobalColor.transparent)

        painter = QPainter(circular_pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QBrush(pixmap))
        painter.drawEllipse(0, 0, size, size)
        painter.end()

        self.image_label.setPixmap(circular_pixmap)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def create_profile_info(self):
        self.name_label.setText(f"Name: {self.profile_data['name']}")
        self.name_label.setFont(QFont('Arial', 16))
        self.layout.addWidget(self.name_label)

        self.age_label.setText(f"Age: {self.profile_data['age']}")
        self.age_label.setFont(QFont('Arial', 16))
        self.layout.addWidget(self.age_label)

        self.bio_label.setText(f"Bio: {self.profile_data['bio']}")
        self.bio_label.setFont(QFont('Arial', 16))
        self.layout.addWidget(self.bio_label)

    def accept_profile(self):
        print(f"Profile {self.profile_data['name']} accepted!")
        self.load_next_profile()

    def reject_profile(self):
        print(f"Profile {self.profile_data['name']} rejected!")
        self.load_next_profile()

    def load_next_profile(self):
        self.current_profile_index += 1

        if self.current_profile_index < len(self.profiles):
            self.profile_data = self.profiles[self.current_profile_index]

            self.title_label.setText(
                    f"Match Profile: {self.profile_data['name']}")
            self.create_circular_profile_image()
            self.name_label.setText(f"Name: {self.profile_data['name']}")
            self.age_label.setText(f"Age: {self.profile_data['age']}")
            self.bio_label.setText(f"Bio: {self.profile_data['bio']}")
        else:
            self.title_label.setText("No more profiles")
            self.image_label.clear()
            self.name_label.clear()
            self.age_label.clear()
            self.bio_label.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Load profiles from the CSV file
    file_path = 'C://Users//jbt//PycharmProjects//special_heart//Special-Love//user_info.csv'  # Update with your file path
    profiles = get_users_dictionary(file_path)

    print(profiles)

    stack = QStackedWidget()

    match_page = MatchPage(stack, profiles)

    stack.addWidget(match_page)

    stack.setCurrentIndex(0)
    stack.show()

    sys.exit(app.exec())
