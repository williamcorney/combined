from PyQt6.QtCore import pyqtSignal
from notehandler import Note_Handler
from gui import gui


class Tab1(Note_Handler,gui):
    note_on_signal = pyqtSignal(int, str)
    note_off_signal = pyqtSignal(int)
    def __init__(self, parent_widget, *args, **kwargs):
        super().__init__()
        # self.gui = gui()
        # self.parent_widget = parent_widget

