from datetime import datetime
from colorama import init, Fore, Style

init()


class Note:
    """
         Class for storing contact information, including name, phone numbers, and birthday.

         Attributes:
             id (int): The note's id.
             title (str): The note's title.
             description (str): The note's description.
             created_at (str): The note's creation date.
     """
    def __init__(self, note_id: int):
        """
            Initializes the note with id.

            Args:
                note_id (int): The note's id.
        """
        self.id = note_id
        self.title = None
        self.description = None
        self.created_at = datetime.now().strftime('%m/%d/%Y, %H:%M')

    def __getitem__(self, key: str):
        """
            Representing getting existing item

            Args:
                key(str): The dictionary key

            Returns:
                str: String value or the item
        """
        return self.__dict__[key]

    def __setitem__(self, key: str, value: str):
        """
           Representing setting new item

           Args:
               key(str): The dictionary key
               value(str): New value for the field
        """
        if isinstance(value, str) and len(f'{value}') is not 0:
            self.__dict__[key] = value
        elif len(f'{value}') > 120:
            raise ValueError(f'{Fore.RED}{key.title()} should be less than 120 characters!{Style.RESET_ALL}')
        else:
            raise ValueError(f'{Fore.RED}{key.title()} should contain at least one character!{Style.RESET_ALL}')

    def is_valid(self):
        """
            Returns is note valid

            Returns:
                bool: The boolean value is note valid
        """
        return self.title is not None and self.description is not None

    def __str__(self):
        """
            Returns a string representation of the record.

            Returns:
                str: The string representation of the note.
        """
        return f"Id: {self.id}; Title: {self.title}; Description: {self.description}; CreatedAt: {self.created_at}"
