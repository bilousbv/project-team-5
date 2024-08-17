import readline
from colorama import Fore
from assistant_bot.service.address_book_service import AddressBookService
from assistant_bot.constants.commands import Commands
from assistant_bot.service.notes_service import NoteService
from assistant_bot.utils.parse_input import parse_input
from assistant_bot.utils.table_printer import table_printer


def main():
    readline.set_completer(Commands.completer)
    if readline.__doc__ and 'libedit' in readline.__doc__:
        readline.parse_and_bind("bind ^I rl_complete")
    else:
        readline.parse_and_bind("tab: complete")

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
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)
        except (KeyboardInterrupt, ValueError):
            print('\n')
            continue  # Control-C pressed. Try again.
        except EOFError:
            AddressBookService.save_data(address_book)
            NoteService.save_data(notes_book)
            print("\nGood bye!")
            break  # Control-D pressed. Exit the loop.
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
                print(NoteService.get_note_by_id(args, notes_book))
            case Commands.DELETE_NOTE:
                print(NoteService.delete_note(args, notes_book))
            case _:
                print(f"Invalid command. Please check out available ones: {
                    Commands.all_commands()}")


if __name__ == "__main__":
    main()
