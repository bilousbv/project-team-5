from collections import UserDict
from model.record import Record
from colorama import init, Fore, Style

init()


class AddressBook(UserDict):
    def __init__(self):
        """
           Initializes the empty address book.
        """
        super().__init__()

    def add_record(self, record):
        """
            Adds a record to the address book.

            Args:
                record (Record): The record to add.
        """
        self.data.update({record.name.value: record})

    def find(self, name: str) -> Record:
        """
            Finds a record by name in the address book.

            Args:
                name (str): The name to search for.

            Returns:
                Record: The record if found, or None.
        """
        for k, v in self.data.items():
            if k == name:
                return v

    def show_all(self):
        """
            Show all contacts.
        """
        if len(self.data.values()) is 0:
            print(f'{Fore.RED}There are no contacts saved{Style.RESET_ALL}')

        for record in self.data.values():
            print(str(record))

    def remove_record(self, record: Record):
        """
            Deletes a record from the address book.

            Args:
                record (Record): Record to delete.
        """
        del self.data[record.name.value]
