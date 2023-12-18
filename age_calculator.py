import sys
from datetime import datetime
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton

class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age Calculator")
        grid = QGridLayout()

        name_label = QLabel("Name")
        self.name_input = QLineEdit()
        birth_label = QLabel("Date of birth")
        self.birth_input = QLineEdit()

        calculate_btn = QPushButton("Calculate age")
        calculate_btn.clicked.connect(self.calculate_age)
        self.output_label = QLabel("")

        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_input, 0, 1)
        grid.addWidget(birth_label, 1, 0)
        grid.addWidget(self.birth_input, 1, 1)
        grid.addWidget(calculate_btn, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_age(self):
        current_year = datetime.now().year
        date_of_birth = self.birth_input.text()
        year_of_birth = datetime.strptime(date_of_birth, "%m/%d/%Y").date().year
        age = current_year - year_of_birth
        self.output_label.setText(f"{self.name_input.text()} is {age} years old.")

app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())
