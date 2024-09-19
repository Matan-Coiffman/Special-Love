import sys
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, \
    QHBoxLayout, QStackedWidget, QApplication
from PyQt6.QtGui import QFont, QPixmap, QPainter, QBrush
from PyQt6.QtCore import Qt
import requests
from io import BytesIO
import csv


def get_users_dictionary(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        data = [
            {
                'name': row['first_name'],
                'age': row['age'],
                'bio': f"Interest: {row.get('intrests', 'N/A')}, Hobby: {row.get('hobbies', 'N/A')}, Lifestyle: {row.get(' lifestyle', 'N/A')}",
                'image_path': 'https://randomuser.me/api/portraits/men/1.jpg'
            }
            for row in csv_reader
        ]
    return data


def get_random_face_image_url():
    try:
        response = requests.get('https://randomuser.me/api/')
        response.raise_for_status()
        data = response.json()
        image_url = data['results'][0]['picture']['large']
        return image_url
    except Exception as e:
        print(f"Failed to get image URL: {e}")
        return 'https://randomuser.me/api/portraits/men/1.jpg'


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
        self.load_random_face_image()

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

    def load_random_face_image(self):
        try:
            image_url = get_random_face_image_url()
            print(f"Loading image from: {image_url}")

            response = requests.get(image_url)
            response.raise_for_status()

            img_data = response.content
            pixmap = QPixmap()
            pixmap.loadFromData(img_data)

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

        except Exception as e:
            print(f"Failed to load image: {e}")
            fallback_image_url = 'https://randomuser.me/api/portraits/men/1.jpg'
            response = requests.get(fallback_image_url)
            img_data = response.content
            pixmap = QPixmap()
            pixmap.loadFromData(img_data)

            size = min(pixmap.width(), pixmap.height())
            circular_pixmap = QPixmap(size, size)
            circular_pixmap.fill(Qt.GlobalColor.transparent)

            painter = QPainter(circular_pixmap)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            painter.setBrush(QBrush(pixmap))
            painter.drawEllipse(0, 0, size, size)
            painter.end()

            self.image_label.setPixmap(circular_pixmap)

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
            self.load_random_face_image()
            self.name_label.setText(f"Name: {self.profile_data['name']}")
            self.age_label.setText(f"Age: {self.profile_data['age']}")
            self.bio_label.setText(f"Bio: {self.profile_data['bio']}")
        else:
            self.title_label.setText("No more profiles")
            self.image_label.clear()
            self.name_label.clear()
            self.age_label.clear()
            self.bio_label.clear()


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#
#     # Load profiles from the CSV file
#     file_path = '../user_info.csv'  # Update with your file path
#     profiles = get_users_dictionary(file_path)
#
#     stack = QStackedWidget()
#
#     match_page = MatchPage(stack, profiles)
#
#     stack.addWidget(match_page)
#
#     stack.setCurrentIndex(0)
#     stack.show()
#
#     sys.exit(app.exec())
