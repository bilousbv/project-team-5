from model.field import Field


class Phone(Field):
    """
        Class for storing a contact's phone. Inherits from Field.
    """

    def __init__(self, value: str):
        """
            Initializes the phone field with value.

            Args:
                value (str): The phone's value.
        """
        if len(str(value)) == 10:
            super().__init__(value)
        else:
            raise ValueError("Wrong phone format")
