from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from colorama import Fore
from service.address_book_service import AddressBookService
from constants.commands import Commands
from service.notes_service import NoteService
from utils.parse_input import parse_input
from utils.table_printer import table_printer


def main():
    commands_completer = WordCompleter(
        Commands.all_commands(), ignore_case=True)

    address_book = AddressBookService.load_data()
    notes_book = NoteService.load_data()

    contacts_headers = [
        f"{Fore.LIGHTBLUE_EX}Contact Name{Fore.RESET}",
        f"{Fore.LIGHTBLUE_EX}Phones{Fore.RESET}",
        f"{Fore.LIGHTBLUE_EX}Birthday{Fore.RESET}",
        f"{Fore.LIGHTBLUE_EX}Email{Fore.RESET}"
    ]

    notes_headers = [
        f"{Fore.LIGHTBLUE_EX}Title{Fore.RESET}",
        f"{Fore.LIGHTBLUE_EX}Description{Fore.RESET}",
        f"{Fore.LIGHTBLUE_EX}Created{Fore.RESET}"
    ]

    print(f"{Fore.LIGHTCYAN_EX}Welcome to the assistant bot!{Fore.RESET}")
    while True:
        user_input = prompt("Enter a command: ", completer=commands_completer)
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
                contacts_rows = [
                    [record.name.value, '\n'.join(
                        p.value for p in record.phones), record.birthday.value, record.email]
                    for record in address_book.data.values()
                ]
                print(table_printer(contacts_headers, contacts_rows)
                      if contacts_rows else f"{Fore.RED}No contacts{Fore.RESET}")
            case Commands.ADD_BIRTHDAY:
                print(AddressBookService.add_birthday_to_contact(args, address_book))
            case Commands.SHOW_BIRTHDAY:
                print(AddressBookService.get_birthday_for_contact(
                    args, address_book))
            case Commands.BIRTHDAYS:
                print(AddressBookService.get_birthdays_for_next_week(address_book))
            case Commands.ADD_EMAIL:
                print(AddressBookService.add_email_to_contact(args, address_book))
            case Commands.ADD_NOTE:
                NoteService.add_note(NoteService(), notes_book)
            case Commands.SHOW_NOTES:
                notes_rows = [
                    [note.title, note.description, note.created_at]
                    for note in notes_book.data.values()
                ]
                print(table_printer(notes_headers, notes_rows)
                      if notes_rows else f"{Fore.RED}No notes{Fore.RESET}")
            case Commands.FIND_NOTE:
                notes = NoteService.get_notes_by_title(args, notes_book)
                notes_rows = [
                    [note.title, note.description, note.created_at]
                    for note in notes
                ]
                print(table_printer(notes_headers, notes_rows)
                      if notes_rows else f"{Fore.RED}No notes{Fore.RESET}")
            case Commands.DELETE_NOTE:
                print(NoteService.delete_note(args, notes_book))
            case Commands.HELP:
                print(AddressBookService.display_help())
            case _:
                print(f"Invalid command. Please check out available ones: {
                    Commands.all_commands()}")


if __name__ == "__main__":
    main()
