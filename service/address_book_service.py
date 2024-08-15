import pickle
from model.record import Record
from model.address_book import AddressBook
from datetime import datetime, timedelta
from constants.filepath import ADDRESS_BOOK_FILEPATH


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Enter the argument for the command"
        except ValueError:
            return "Enter the argument for the command"
        except KeyError:
            return "No such contact"

    return inner


class AddressBookService:
    @staticmethod
    @input_error
    def add_contact(book: AddressBook):
        name = input("Enter your name:")
        record = Record(name)
        phone = input("Enter your phone:")
        try:
            record.add_phone(phone)
        except ValueError:
            return "Wrong phone format!"
        date_of_birth = input("Enter your birthday:")
        try:
            datetime.strptime(date_of_birth, "%d.%m.%Y")
            record.add_birthday(date_of_birth)
        except ValueError:
            return "Wrong data format!"
        # email = input("Enter your email:")   TODO change when email will be implemented
        book.add_record(record)
        return "Contact successfully added!"

    @staticmethod
    @input_error
    def change_contact_number(args, book: AddressBook):
        name, old_phone, new_phone, *_ = args
        record = book.find(name)
        if not record:
            return "No contact for such name"
        return record.edit_phone(old_phone, new_phone)

    @staticmethod
    @input_error
    def get_phones_for_contact(args, book: AddressBook):
        name, *_ = args
        record = book.find(name)
        if not record:
            return "No contact for such name"
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
            return "No contact for such name"
        try:
            datetime.strptime(date_of_birth, "%d.%m.%Y")
            record.add_birthday(date_of_birth)
            return "Date of birth added"
        except ValueError:
            return "Wrong data format"

    @staticmethod
    @input_error
    def get_birthday_for_contact(args, book: AddressBook):
        name, *_ = args
        record = book.find(name)
        if not record:
            return "No contact for such name"
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
            return "No contact for such name"
        try:
            record.add_email(email_address)
            return "Email added"
        except ValueError:
            return "Invalid email address"

    @staticmethod
    def save_data(book: AddressBook, path: str = FILEPATH):
        with open(path, "wb") as f:
            pickle.dump(book, f)

    @staticmethod
    @input_error
    def delete_contacts(args, book: AddressBook):
        """
           Deletes the existing contact

            Args:
                args (List[str]): List containing the name.
                book (AddressBook): The address book instance.

            Returns:
                str: Success message or error.
        """
        name, *_ = args
        record = book.find(name)
        if not record:
            return "No contact for such name."
        confirmation = input(f"Are you sure that you want to delete this contact '{name}'?(yes/no:").strip().lower()
        if confirmation != "yes":
            return "Deletion canceled."

        book.remove_record(record)
        return f"Contact '{name}' deleted."

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
