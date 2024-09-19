import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QCheckBox, QPushButton, QSpinBox, QMessageBox, QComboBox
)

class ProfilePage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Dating Site Profile Page')

        layout = QVBoxLayout()

        self.age_label = QLabel('Age:')
        self.age_input = QSpinBox()
        self.age_input.setRange(18, 120)

        self.city_label = QLabel('City:')
        self.city_input = QComboBox()
        self.city_input.addItems(['Beer-Sheva', 'Tel-Aviv', 'Jerusalem', 'Petah-Tikva', 'Julis', 'Holon'])

        self.hobbies_label = QLabel('Hobbies:')
        self.hobbies = [
            QCheckBox('Sports'), QCheckBox('Cooking'), QCheckBox('Reading'),
            QCheckBox('Music'), QCheckBox('Traveling'), QCheckBox('Painting')
        ]

        self.lifestyle_label = QLabel('Lifestyle:')
        self.lifestyles = [
            QCheckBox('Active'), QCheckBox('Sedentary'), QCheckBox('Works from Home'),
            QCheckBox('Frequent Traveler'), QCheckBox('Nightlife')
        ]

        self.interests_label = QLabel('Interests:')
        self.interests = [
            QCheckBox('Technology'), QCheckBox('Fashion'), QCheckBox('Philosophy'),
            QCheckBox('Art'), QCheckBox('Science'), QCheckBox('Politics'), QCheckBox('Fear of god')
        ]

        self.submit_button = QPushButton('Submit Profile')
        self.submit_button.clicked.connect(self.submit_profile)

        layout.addWidget(self.age_label)
        layout.addWidget(self.age_input)

        layout.addWidget(self.city_label)
        layout.addWidget(self.city_input)

        layout.addWidget(self.hobbies_label)
        for hobby in self.hobbies:
            layout.addWidget(hobby)

        layout.addWidget(self.lifestyle_label)
        for lifestyle in self.lifestyles:
            layout.addWidget(lifestyle)

        layout.addWidget(self.interests_label)
        for interest in self.interests:
            layout.addWidget(interest)

        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def submit_profile(self):
        age = self.age_input.value()
        city = self.city_input.currentText()

        selected_hobbies = [hobby.text() for hobby in self.hobbies if hobby.isChecked()]

        selected_lifestyles = [lifestyle.text() for lifestyle in self.lifestyles if lifestyle.isChecked()]

        selected_interests = [interest.text() for interest in self.interests if interest.isChecked()]


        profile_info = f"Age: {age}\n"
        profile_info += f"City: {city}\n"
        profile_info += f"Hobbies: {', '.join(selected_hobbies)}\n"
        profile_info += f"Lifestyle: {', '.join(selected_lifestyles)}\n"
        profile_info += f"Interests: {', '.join(selected_interests)}"

        QMessageBox.information(self, 'Profile Details', profile_info)

        print(profile_info)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProfilePage()
    window.show()
    sys.exit(app.exec())
