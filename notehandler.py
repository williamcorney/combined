
from gui import gui

class Note_Handler(gui):
    def __init__(self):
        super().__init__()
        pass

    def midi_handling(self, mididata):

        if self.theorymode == "Scales":
            print ('SCALES!!')

        if mididata.type == "note_on":
            print (mididata.note % 12)

        print (f"Required {self.required_notes} to midi note handler")

        self.label.setText(str(self.required_notes))

