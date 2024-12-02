from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt, pyqtSignal
class Tab3(QWidget):
    note_on_signal = pyqtSignal(int, str)
    note_off_signal = pyqtSignal(int)
    def __init__(self, parent_widget, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.parent_widget = parent_widget