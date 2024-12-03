
from gui import gui

class Note_Handler(gui):
    def __init__(self):
        super().__init__()
        self.gui = gui()
        pass

    def midi_handling(self, mididata):

        print (f"Required {self.required_notes} to midi note handler")

