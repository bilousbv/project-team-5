from datetime import datetime

DATE_FORMAT = '%d.%m.%Y'


class Birthday:
    def __init__(self, value):
        try:
            birthday = datetime.strptime(value, DATE_FORMAT).date()
            self.birthday = birthday
            super().__init__(birthday)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
