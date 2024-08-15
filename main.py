from colorama import Fore
from service.address_book_service import AddressBookService
from constants.commands import Commands
from utils.table_printer import table_printer
from utils.parse_input import parse_input


def main():
  book = AddressBookService.load_data()

  print("Welcome to the assistant bot!")
  contacts_headers = [f"{Fore.LIGHTBLUE_EX}Contact Name{Fore.RESET}", f"{
      Fore.LIGHTBLUE_EX}Phones{Fore.RESET}", f"{Fore.LIGHTBLUE_EX}Birthday{Fore.RESET}"]
  contacts_rows = [[record.name.value, '\n'.join(
      p.value for p in record.phones), record.birthday] for record in book.data.values()]
  while True:
    user_input = input("Enter a command: ")
    command, *args = parse_input(user_input)

    match Commands.get_command(command):
      case Commands.EXIT:
        AddressBookService.save_data(book)
        print("Good bye!")
        break
      case Commands.HELLO:
        print("How can I help you?")
      case Commands.ADD_CONTACT:
        print(AddressBookService.add_contact(args, book))
      case Commands.CHANGE_CONTACT:
        print(AddressBookService.change_contact_number(args, book))
      case Commands.PHONE:
        print(AddressBookService.get_phones_for_contact(args, book))
      case Commands.ALL_CONTACTS:
        print(table_printer(contacts_headers, contacts_rows))
      case Commands.ADD_BIRTHDAY:
        print(AddressBookService.add_birthday_to_contact(args, book))
      case Commands.SHOW_BIRTHDAY:
        print(AddressBookService.get_birthday_for_contact(args, book))
      case Commands.BIRTHDAYS:
        print(AddressBookService.get_birthdays_for_next_week(book))
      case _:
        print(f"Invalid command. Please check out available ones: {
            [command.value for command in Commands.__members__.values()]}")


if __name__ == "__main__":
  main()
