from collections import UserDict
from colorama import init, Fore, Style
from assistant_bot.model.note import Note

init()


class NotesBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_note(self, note: Note):
        self.data.update({note.id: note})

    def get_next_id(self):
        if len(self.data) == 0:
            return 1
        else:
            return max(self.data, key=lambda x: x) + 1

    def show_all(self):
        if len(self.data.values()) == 0:
            print(f'{Fore.RED}There are no notes saved{Style.RESET_ALL}')

        for note in self.data.values():
            print(str(note))

    def find(self, note_id: int) -> Note:
        for k, v in self.data.items():
            if k == note_id:
                return v

    def remove_note(self, note: Note):
        del self.data[note.id]
