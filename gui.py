from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from theory import Theory
class gui(QWidget,Theory):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.label = QLabel("Hello")
        self.button = QPushButton("GO")
        self.setLayout(self.layout)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.button_clicked)

    def button_clicked (self):
        self.label.setText(str(self.define_notes()))
        self.theorymode = "Scales"



