import pickle
from colorama import init, Fore, Style

from constants.filepath import NOTES_BOOK_FILEPATH
from model.note import Note
from model.notes_book import NotesBook
from service.address_book_service import input_error
from model.tag import Tag

FIELDS = ['title', 'description']
QUIT_COMMAND = 'q'
init()


class NoteService:
    def add_field(self, note: Note, field_name: str):
        try:
            user_input = str(input(f'{Fore.BLUE}Enter the note {
                             field_name}(q - for quit): {Style.RESET_ALL}'))
            if user_input.lower() is QUIT_COMMAND:
                return None

            note[field_name] = user_input
            return note[field_name]
        except ValueError as e:
            print(f'{Fore.RED}{e}{Style.RESET_ALL}')
            return self.add_field(note, field_name)

    def add_note(self, note_book: NotesBook):
        note_id = note_book.get_next_id()
        note = Note(note_id)
        index = 0
        while True:
            field_index = FIELDS[-1]
            if index < len(FIELDS) - 1:
                field_index = FIELDS[index]

            field = self.add_field(note, field_index)
            index += 1

            # TODO Remove index condition for tags endless input
            if field is None or index >= len(FIELDS):

                while True:
                    tag = str(
                        input(f'{Fore.BLUE}Enter the note tag(q - for quit):{Style.RESET_ALL}'))
                    if tag.lower() == QUIT_COMMAND:
                        break
                    try:
                        self.add_tag(tag, note)
                        print(f'{Fore.GREEN}Tag was added successfully!{
                              Style.RESET_ALL}')
                    except ValueError as e:
                        print(e)

                if note.is_valid():
                    note_book.add_note(note)
                    print(f'{Fore.GREEN}Note was saved successfully!{
                          Style.RESET_ALL}')
                    break
                else:
                    del note
                    print(f'{Fore.RED}Note didn\'t saved. Title or Description is missing!{
                          Style.RESET_ALL}')
                    break

    @staticmethod
    def add_tag(tag: str, note: Note):
        if len(tag) == 0:
            raise ValueError(f'{Fore.RED}Tag should contain at least one character!{
                             Style.RESET_ALL}')
        for note_tag in note.tags:
            if note_tag.value == tag:
                raise ValueError(f'{Fore.RED}Note already contains this tag{
                                 Style.RESET_ALL}')

        note.tags.append(Tag(tag))

    @staticmethod
    @input_error
    def get_note_by_id(args, book: NotesBook):
        note_id, *_ = args
        note = book.find(int(note_id))
        if not note:
            return f"{Fore.RED}No note for such id{Style.RESET_ALL}"

        return note

    @input_error
    def get_notes_by_title(args, book: NotesBook):
        title, *_ = args
        notes = book.find_by_title(title)
        if not notes:
            return f"{Fore.RED}No note for such title{Style.RESET_ALL}"
        if len(notes) >= 1:
            return notes

    @staticmethod
    @input_error
    def delete_note(args, book: NotesBook):
        note_id, *_ = args
        note = book.find(int(note_id))
        if not note:
            return f"{Fore.RED}No note for such id.{Style.RESET_ALL}"
        confirmation = input(f"{Fore.YELLOW}Are you sure that you want to delete this note '{note_id}'?"
                             f"(yes/no):{Style.RESET_ALL}").strip().lower()
        if confirmation != "yes":
            return f"{Fore.RED}Deletion canceled.{Style.RESET_ALL}"

        book.remove_note(note)
        return f"{Fore.GREEN}Note '{note_id}' deleted successfully.{Style.RESET_ALL}"

    @staticmethod
    def save_data(book: NotesBook, path: str = NOTES_BOOK_FILEPATH):
        with open(path, "wb") as f:
            pickle.dump(book, f)

    @staticmethod
    def load_data(path: str = NOTES_BOOK_FILEPATH):
        try:
            with open(path, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return NotesBook()

    @staticmethod
    def find_notes_by_tag(args, book: NotesBook):
        notes_with_tag = []
        if len(args) < 1:
            return notes_with_tag
        tag_name, *_ = args
        for note in book.values():
            tags = note.tags
            for tag in tags:
                if tag.value == tag_name:
                    notes_with_tag.append(note)

        return notes_with_tag
