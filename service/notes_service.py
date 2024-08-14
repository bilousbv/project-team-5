import pickle
from colorama import init, Fore, Style

from constants.filepath import NOTE_BOOK_FILEPATH
from model.note import Note
from model.note_book import NoteBook

FIELDS = ['title', 'description']
QUIT_COMMAND = 'q'
init()


class NoteService:
    def add_field(self, note: Note, field_name: str):
        try:
            user_input = str(input(f'{Fore.BLUE}Enter the note {field_name}(q - for quit):{Style.RESET_ALL}'))
            if user_input.lower() is QUIT_COMMAND:
                return None

            note[field_name] = user_input
            return note[field_name]
        except ValueError as e:
            print(f'{Fore.RED}{e}{Style.RESET_ALL}')
            self.add_field(note, field_name)

    def add_note(self, note_book: NoteBook):
        note_id = note_book.get_next_id()
        note = Note(note_id)
        index = 0
        while True:
            field = self.add_field(note, FIELDS[index] or FIELDS[-1])
            index += 1

            # TODO Remove index condition for tags endless input
            if field is None or index >= len(FIELDS):
                if note.is_valid():
                    print(f'{Fore.GREEN}Note was saved successfully!{Style.RESET_ALL}')
                    note_book.add_note(note)
                else:
                    print(f'{Fore.RED}Note didn\'t saved. Title or Description is missing!{Style.RESET_ALL}')
                    del note
                break

    @staticmethod
    def save_data(book: NoteBook, path: str = NOTE_BOOK_FILEPATH):
        with open(path, "wb") as f:
            pickle.dump(book, f)

    @staticmethod
    def load_data(path: str = NOTE_BOOK_FILEPATH):
        try:
            with open(path, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return NoteBook()