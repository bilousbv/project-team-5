from model.field import Field


class Name(Field):
    """
        Class for storing a contact's name. Inherits from Field.
    """

    def __init__(self, value: str):
        """
            Initializes the name with value.

            Args:
                value (str): The name's value.
        """
        super().__init__(value)