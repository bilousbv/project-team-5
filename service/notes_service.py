import pickle
from colorama import init, Fore, Style

from constants.filepath import NOTES_BOOK_FILEPATH
from model.note import Note
from model.notes_book import NotesBook
from service.address_book_service import input_error

FIELDS = ['title', 'description']
QUIT_COMMAND = 'q'
init()


class NoteService:
    def add_field(self, note: Note, field_name: str):
        """
           Add a new note field.

           Args:
               note (Note): The note instance.
               field_name (str): The name of the field to add.

           Returns:
               str: Created field of None
        """
        try:
            user_input = str(input(f'{Fore.BLUE}Enter the note {field_name}(q - for quit):{Style.RESET_ALL}'))
            print(user_input.lower(),  QUIT_COMMAND)
            if user_input.lower() is QUIT_COMMAND:
                return None

            note[field_name] = user_input
            return note[field_name]
        except ValueError as e:
            print(f'{Fore.RED}{e}{Style.RESET_ALL}')
            return self.add_field(note, field_name)

    def add_note(self, note_book: NotesBook):
        """
           Add a new note.

           Args:
               note_book (NotesBook): The notes book instance.

           Returns:
               str: Success message indicating note creation.
        """
        note_id = note_book.get_next_id()
        note = Note(note_id)
        index = 0
        while True:
            field_index = FIELDS[-1]
            if index < len(FIELDS) - 1:
                field_index = FIELDS[index]

            field = self.add_field(note, field_index)
            index += 1
            print(field)

            # TODO Remove index condition for tags endless input
            if field is None or index >= len(FIELDS):
                if note.is_valid():
                    note_book.add_note(note)
                    print(f'{Fore.GREEN}Note was saved successfully!{Style.RESET_ALL}')
                    break
                else:
                    del note
                    print(f'{Fore.RED}Note didn\'t saved. Title or Description is missing!{Style.RESET_ALL}')
                    break

    @staticmethod
    @input_error
    def get_note_by_id(args, book: NotesBook):
        """
           Get the note by id.

           Args:
               args (List[str]): List containing the note id.
               book (NotesBook): The address book instance.

           Returns:
               str: The note or an error message.
           """
        note_id, *_ = args
        note = book.find(int(note_id))
        if not note:
            return f"{Fore.RED}No note for such id{Style.RESET_ALL}"

        return note

    @staticmethod
    @input_error
    def delete_note(args, book: NotesBook):
        """
           Deletes the existing note

            Args:
                args (List[str]): List containing the note id.
                book (AddressBook): The address book instance.

            Returns:
                str: Success message or error.
        """
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
        """
            Save the notes book to a file.
        """
        with open(path, "wb") as f:
            pickle.dump(book, f)

    @staticmethod
    def load_data(path: str = NOTES_BOOK_FILEPATH):
        """
            Load the notes book from a file.
        """
        try:
            with open(path, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return NotesBook()
