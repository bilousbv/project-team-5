from collections import UserDict
from model.record import Record


class NoteBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_note(self, note):
        self.data.update({note.id: note})

    def get_next_id(self):
        if len(self.data) is 0:
            return 1
        else:
            return max(self.data, key=lambda x: x) + 1

    def show_all(self):
        for note in self.data.values():
            print(str(note))
