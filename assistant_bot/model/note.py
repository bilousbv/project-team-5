from datetime import datetime
from colorama import init, Fore, Style

init()


class Note:
    def __init__(self, note_id: int):
        self.id = note_id
        self.title = None
        self.description = None
        self.tags = []
        self.created_at = datetime.now().strftime('%m/%d/%Y, %H:%M')

    def __getitem__(self, key: str):
        return self.__dict__[key]

    def __setitem__(self, key: str, value: str):
        if isinstance(value, str) and len(f'{value}') is not 0:
            self.__dict__[key] = value
        elif len(f'{value}') > 120:
            raise ValueError(f'{Fore.RED}{key.title()} should be less than 120 characters!{Style.RESET_ALL}')
        else:
            raise ValueError(f'{Fore.RED}{key.title()} should contain at least one character!{Style.RESET_ALL}')

    def is_valid(self):
        return self.title is not None and self.description is not None

    def __str__(self) -> str:
        return (f"Id: {self.id}; Title: {self.title}; Description: {self.description}; CreatedAt: {self.created_at}, "
                f"Tags: {'; '.join(t.value for t in self.tags)}")
