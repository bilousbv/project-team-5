from collections import UserDict
from colorama import init, Fore, Style
from model.note import Note

init()


class NotesBook(UserDict):
    def __init__(self):
        """
            Initializes the empty notes book.
        """
        super().__init__()

    def add_note(self, note):
        """
            Adds a note to the notes book.

            Args:
                note (Note): The note to add.
        """
        self.data.update({note.id: note})

    def get_next_id(self):
        """
            Generating id for new note

            Returns:

        """
        if len(self.data) is 0:
            return 1
        else:
            return max(self.data, key=lambda x: x) + 1

    def show_all(self):
        """
            Show all notes.
        """
        if len(self.data.values()) is 0:
            print(f'{Fore.RED}There are no notes saved{Style.RESET_ALL}')

        for note in self.data.values():
            print(str(note))

    def find(self, note_id: int) -> Note:
        """
            Finds a record by name in the address book.

            Args:
                note_id (int): The id to search for.

            Returns:
                Record: The note if found, or None.
        """
        for k, v in self.data.items():
            if k == note_id:
                return v

    def remove_note(self, note: Note):
        """
            Deletes a note from the notes book.

            Args:
                note (Note): Note to delete.
        """
        del self.data[note.id]
