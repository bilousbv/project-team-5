class Field:
    """
        Base class for storing field values of a record.

        Attributes:
            value (str): The value of the field.
    """

    def __init__(self, value: str):
        """
            Initializes the field with value.

            Args:
                value (str): The field's name.
        """
        self.value = value

    def __str__(self):
        """
            Returns a string representation of the record.

            Returns:
                str: The string representation of the field.
        """
        return str(self.value)