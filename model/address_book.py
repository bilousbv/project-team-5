from collections import UserDict
from model.record import Record
from colorama import init, Fore, Style

init()


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, record: Record):
        self.data.update({record.name.value: record})

    def find(self, name: str) -> Record:
        for k, v in self.data.items():
            if k == name:
                return v

    def show_all(self):
        if len(self.data.values()) is 0:
            print(f'{Fore.RED}There are no contacts saved{Style.RESET_ALL}')

        for record in self.data.values():
            print(str(record))

    def remove_record(self, record: Record):
        del self.data[record.name.value]
