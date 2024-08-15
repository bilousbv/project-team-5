import readline

from service.address_book_service import AddressBookService
from constants.commands import Commands
from service.notes_service import NoteService


def parse_input(user_input: str):
    if not user_input.strip():
        return None, []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    readline.set_completer(Commands.completer)
    if readline.__doc__ and 'libedit' in readline.__doc__:
        readline.parse_and_bind("bind ^I rl_complete")
    else:
        readline.parse_and_bind("tab: complete")

    address_book = AddressBookService.load_data()
    notes_book = NoteService.load_data()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match Commands.get_command(command):
            case Commands.EXIT:
                AddressBookService.save_data(address_book)
                NoteService.save_data(notes_book)
                print("Good bye!")
                break
            case Commands.HELLO:
                print("How can I help you?")
            case Commands.ADD_CONTACT:
                print(AddressBookService.add_contact(address_book))
            case Commands.CHANGE_CONTACT:
                print(AddressBookService.change_contact_number(args, address_book))
            case Commands.PHONE:
                print(AddressBookService.get_phones_for_contact(args, address_book))
            case Commands.ALL_CONTACTS:
                address_book.show_all()
            case Commands.ADD_BIRTHDAY:
                print(AddressBookService.add_birthday_to_contact(args, address_book))
            case Commands.SHOW_BIRTHDAY:
                print(AddressBookService.get_birthday_for_contact(
                    args, address_book))
            case Commands.BIRTHDAYS:
                print(AddressBookService.get_birthdays_for_next_week(address_book))
            case Commands.ADD_NOTE:
                NoteService.add_note(NoteService(), notes_book)
            case Commands.SHOW_NOTES:
                notes_book.show_all()
            case Commands.FIND_NOTE:
                print(NoteService.get_note_by_id(args, notes_book))
            case Commands.DELETE_NOTE:
                print(NoteService.delete_note(args, notes_book))
            case _:
                print(f"Invalid command. Please check out available ones: {
                    Commands.all_commands()}")


if __name__ == "__main__":
    main()
