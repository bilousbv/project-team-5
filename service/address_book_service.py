import pickle
from colorama import Fore
from model.record import Record
from model.address_book import AddressBook
from datetime import datetime, timedelta
from constants.filepath import FILEPATH


def input_error(func):
  def inner(*args, **kwargs):
    try:
      return func(*args, **kwargs)
    except (ValueError, IndexError):
      return f"{Fore.LIGHTRED_EX}Enter the argument for the command{Fore.RESET}"
    except KeyError:
      return f"{Fore.LIGHTRED_EX}No such contact{Fore.RESET}"

  return inner


class AddressBookService:

  def __init__(self):
    pass

  @staticmethod
  @input_error
  def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = f"{Fore.GREEN}Contact updated.{Fore.RESET}"
    if record is None:
      record = Record(name)
      book.add_record(record)
      message = f"{Fore.GREEN}Contact added.{Fore.RESET}"
    if phone:
      is_added = record.add_phone(phone)
      if not is_added:
        raise ValueError
    return message

  @staticmethod
  @input_error
  def change_contact_number(args, book: AddressBook):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if not record:
      return f"{Fore.YELLOW}No contact for such name{Fore.RESET}"
    return record.edit_phone(old_phone, new_phone)

  @staticmethod
  @input_error
  def get_phones_for_contact(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    if not record:
      return f"{Fore.YELLOW}No contact for such name{Fore.RESET}"
    phones = ""
    for phone in record.phones:
      phones = phones + " " + phone.value
    return phones

  @staticmethod
  @input_error
  def add_birthday_to_contact(args, book: AddressBook):
    name, date_of_birth, *_ = args
    record = book.find(name)
    if not record:
      return f"{Fore.YELLOW}No contact for such name{Fore.RESET}"
    try:
      datetime.strptime(date_of_birth, "%d.%m.%Y")
      record.add_birthday(date_of_birth)
      return f"{Fore.GREEN}Date of birth added{Fore.RESET}"
    except ValueError:
      return f"{Fore.RED}Wrong data format{Fore.RESET}"

  @staticmethod
  @input_error
  def get_birthday_for_contact(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    if not record:
      return f"{Fore.YELLOW}No contact for such name{Fore.RESET}"
    return record.birthday

  @staticmethod
  @input_error
  def get_birthdays_for_next_week(book: AddressBook):
    today = datetime.today().date()
    upcoming_birthdays = []
    end_date = today + timedelta(days=7)

    for record in book.data.values():
      name = record.name.value
      birthday_str = record.birthday
      birthday = datetime.strptime(birthday_str, '%d.%m.%Y').date()

      birthday_this_year = birthday.replace(year=today.year)

      if birthday_this_year < today:
        birthday_this_year = birthday.replace(year=today.year + 1)

      if today <= birthday_this_year <= end_date:
        if birthday_this_year.weekday() in (5, 6):
          birthday_this_year += timedelta(days=(7 -
                                          birthday_this_year.weekday()))

        upcoming_birthdays.append({
            'name': name,
            'congratulation_date': birthday_this_year.strftime('%d.%m.%Y')
        })

    return upcoming_birthdays

  @staticmethod
  def save_data(book: AddressBook, path: str = FILEPATH):
    with open(path, "wb") as f:
      pickle.dump(book, f)

  @staticmethod
  def load_data(path: str = FILEPATH):
    try:
      with open(path, "rb") as f:
        return pickle.load(f)
    except FileNotFoundError:
      return AddressBook()
