from service.address_book_service import AddressBookService
from constants.commands import Commands


def parse_input(user_input: str):
  cmd, *args = user_input.split()
  cmd = cmd.strip().lower()
  return cmd, *args


def main():
  book = AddressBookService.load_data()
  print("Welcome to the assistant bot!")
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
        book.show_all()
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
