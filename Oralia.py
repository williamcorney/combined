import sys, mido
from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget
from main import Tab1
from Tab2 import Tab2
from Tab3 import Tab3

class Oralia(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tabs = {}  # Dictionary to hold tab
        self.tab_widget = QTabWidget(self)  # QTabWidget object
        self.tab_widget.setTabPosition(QTabWidget.TabPosition.West)
        self.tab_widget.setTabPosition(QTabWidget.TabPosition.West)
        self.setCentralWidget(self.tab_widget)
        self.tabs["Practical"] = Tab1(self)
        self.tab_widget.addTab(self.tabs["Practical"], "Practical")
        self.tabs["Theory"] = Tab2(self)
        self.tab_widget.addTab(self.tabs["Theory"], "Theory")
        self.tabs["Settings"] = Tab3(self)
        self.tab_widget.addTab(self.tabs["Settings"], "Settings")

    def midi_handling (self,mididata):
        if self.tab_widget.currentIndex() == 0:
            self.tabs["Practical"].midi_handling(mididata)


app = QApplication([])
window = Oralia()
window.show()

with mido.open_input(callback=window.midi_handling) as inport:
    sys.exit(app.exec())