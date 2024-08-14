import re
from model.field import Field


class Email(Field):
    def __init__(self, email):
        self.value = self.validate_email(email)

    def validate_email(self, email):

        regex = r"^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        if not re.fullmatch(regex, email):
            raise ValueError("Invalid email address")
        return email
