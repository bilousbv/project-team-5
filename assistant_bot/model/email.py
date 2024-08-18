import re
from assistant_bot.model.field import Field


class Email(Field):
    def __init__(self, email):
        super().__init__(self.validate_email(email))

    @staticmethod
    def validate_email(email):

        regex = r"^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        if not re.fullmatch(regex, email):
            raise ValueError("Invalid email address")
        return email
