from datetime import datetime

DATE_FORMAT = '%d.%m.%Y'


class Birthday:
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, DATE_FORMAT).date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
