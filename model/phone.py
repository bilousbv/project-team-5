from colorama import Fore
from model.field import Field


class Phone(Field):
    def __init__(self, value: str):
        if len(str(value)) == 10:
            super().__init__(value)
        else:
            raise ValueError(
                f"{Fore.RED}Phone number must be 10 digits.{Fore.RESET}")
