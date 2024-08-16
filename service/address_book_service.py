import pickle
from colorama import Fore
from model.record import Record
from model.address_book import AddressBook
from datetime import datetime, timedelta
from constants.filepath import ADDRESS_BOOK_FILEPATH


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
    @staticmethod
    @input_error
    def add_contact(book: AddressBook):
        name = input(f"{Fore.BLUE}Enter your name: {Fore.RESET}")
        record = Record(name)

        while True:
            phone = input(f"{Fore.BLUE}Enter your phone: {Fore.RESET}")
            is_added = record.add_phone(phone)
            if is_added:
                break
        while True:
            date_of_birth = input(
                f"{Fore.BLUE}Enter your birthday: {Fore.RESET}")
            is_added = record.add_birthday(date_of_birth)
            if is_added:
                break
        try:
            email = input(f"{Fore.BLUE}Enter your email: {Fore.RESET}")
            record.add_email(email)
        except ValueError as e:
            return f"{Fore.RED}{e}{Fore.RESET}"
        book.add_record(record)
        return f"{Fore.GREEN}Contact successfully added!{Fore.RESET}"

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
        except ValueError as e:
            return f"{Fore.RED}{e}{Fore.RESET}"

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
            birthday = datetime.strptime(birthday_str, "%d.%m.%Y").date()

            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday.replace(year=today.year + 1)

            if today <= birthday_this_year <= end_date:
                if birthday_this_year.weekday() in (5, 6):
                    birthday_this_year += timedelta(
                        days=(7 - birthday_this_year.weekday())
                    )

                upcoming_birthdays.append(
                    {
                        "name": name,
                        "congratulation_date": birthday_this_year.strftime("%d.%m.%Y"),
                    }
                )

        return upcoming_birthdays

    @staticmethod
    @input_error
    def add_email_to_contact(args, book: AddressBook):
        name, email_address, *_ = args
        record = book.find(name)
        if not record:
            return f"{Fore.YELLOW}No contact for such name{Fore.RESET}"
        try:
            record.add_email(email_address)
            return f"{Fore.GREEN}Email added{Fore.RESET}"
        except ValueError:
            return f"{Fore.RED}Invalid email address{Fore.RESET}"

    @staticmethod
    @input_error
    def delete_contacts(args, book):
        name, *_ = args
        record = book.find(name)
        if not record:
            return f"{Fore.YELLOW}No contact for such name{Fore.RESET}"
        confirmation = input(f"Are you sure that you want to delete this contact '{
                             name}'?(yes/no:").strip().lower()
        if confirmation != "yes":
            return f"{Fore.GREEN}Deletion canceled.{Fore.RESET}"

        book.remove_record(record)
        return f"{Fore.GREEN}Contact '{name}' deleted.{Fore.RESET}"

    @staticmethod
    def save_data(book: AddressBook, path: str = ADDRESS_BOOK_FILEPATH):
        with open(path, "wb") as f:
            pickle.dump(book, f)

    @staticmethod
    def load_data(path: str = ADDRESS_BOOK_FILEPATH):
        try:
            with open(path, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return AddressBook()
