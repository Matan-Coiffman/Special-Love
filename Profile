import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QCheckBox, QPushButton, QSpinBox, QMessageBox, QComboBox
)

class ProfilePage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Dating Site Profile Page')

        layout = QVBoxLayout()

        # Age input
        self.age_label = QLabel('Age:')
        self.age_input = QSpinBox()
        self.age_input.setRange(18, 120)

        # City selection (using QComboBox for single selection)
        self.city_label = QLabel('City:')
        self.city_input = QComboBox()
        self.city_input.addItems(['Beer-Sheva', 'Tel-Aviv', 'Jerusalem', 'Petah-Tikva', 'Julis', 'Holon'])

        # Hobbies
        self.hobbies_label = QLabel('Hobbies:')
        self.hobbies = [
            QCheckBox('Sports'), QCheckBox('Cooking'), QCheckBox('Reading'),
            QCheckBox('Music'), QCheckBox('Traveling'), QCheckBox('Painting')
        ]

        # Lifestyle
        self.lifestyle_label = QLabel('Lifestyle:')
        self.lifestyles = [
            QCheckBox('Active'), QCheckBox('Sedentary'), QCheckBox('Works from Home'),
            QCheckBox('Frequent Traveler'), QCheckBox('Nightlife')
        ]

        # Interests
        self.interests_label = QLabel('Interests:')
        self.interests = [
            QCheckBox('Technology'), QCheckBox('Fashion'), QCheckBox('Philosophy'),
            QCheckBox('Art'), QCheckBox('Science'), QCheckBox('Politics'), QCheckBox('Fear of god')
        ]

        # Submit button
        self.submit_button = QPushButton('Submit Profile')
        self.submit_button.clicked.connect(self.submit_profile)

        # Adding widgets to the layout
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

        # Collect selected hobbies
        selected_hobbies = [hobby.text() for hobby in self.hobbies if hobby.isChecked()]

        # Collect selected lifestyle
        selected_lifestyles = [lifestyle.text() for lifestyle in self.lifestyles if lifestyle.isChecked()]

        # Collect selected interests
        selected_interests = [interest.text() for interest in self.interests if interest.isChecked()]

        # Create a message to display the collected information
        profile_info = f"Age: {age}\n"
        profile_info += f"City: {city}\n"
        profile_info += f"Hobbies: {', '.join(selected_hobbies)}\n"
        profile_info += f"Lifestyle: {', '.join(selected_lifestyles)}\n"
        profile_info += f"Interests: {', '.join(selected_interests)}"

        # Display the information in a message box
        QMessageBox.information(self, 'Profile Details', profile_info)

        # Print the information to the console
        print(profile_info)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProfilePage()
    window.show()
    sys.exit(app.exec())
