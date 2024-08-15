from model.phone import Phone
from model.name import Name


class Record:
    """
        Class for storing contact information, including name, phone numbers, and birthday.

        Attributes:
            name (Name): The contact's name.
            phones (list of Phone): The contact's phone numbers.
            birthday (Birthday): The contact's birthday.
    """

    def __init__(self, name: str):
        """
            Initializes the record with the contact's name.

            Args:
                name (str): The contact's name.
        """
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone: str):
        """
            Adds a phone number to the record.

            Args:
                phone (str): The phone number to add.
        """
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str):
        """
            Removes a phone number from the record.

            Args:
                phone (str): The phone number to remove.
        """
        for i in self.phones[:]:
            if i.value == phone:
                self.phones.remove(i)

    def edit_phone(self, phone_to_edit: str, new_phone: str):
        """
           Edits a phone number in the record.

           Args:
               phone_to_edit (str): The old phone number.
               new_phone (str): The new phone number.
       """
        for i in self.phones[:]:
            if i.value == phone_to_edit:
                try:
                    self.phones.append(Phone(new_phone))
                except ValueError:
                    return "New phone value is incorrect"
                self.phones.remove(i)
                return "Phone updated"

        return "Phone to edit does not exists for such user"

    def find_phone(self, phone: str):
        """
            Finds a phone number in the record.

            Args:
                phone (str): The phone number to find.

            Returns:
                Phone: The phone number if found, or None.
        """
        for i in self.phones:
            if i.value == phone:
                return i

    def add_birthday(self, birthday):
        """
            Adds a birthday to the record.

            Args:
                birthday (str): The birthday to add.
        """
        self.birthday = birthday

    def __str__(self):
        """
            Returns a string representation of the record.

            Returns:
                str: The string representation of the record.
        """
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"
