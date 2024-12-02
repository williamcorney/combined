from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt, pyqtSignal
import os
class Tab1(QWidget):
    note_on_signal = pyqtSignal(int, str)
    note_off_signal = pyqtSignal(int)
    def __init__(self, parent_widget, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.parent_widget = parent_widget

    def midi_handling(self, mididata):
        if self.parent_widget.currentIndex() == 1: self.parent_widget.widget(1).midiprocessor(mididata)
        if self.parent_widget.currentIndex() == 0: self.note_handler(mididata)