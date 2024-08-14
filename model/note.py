from datetime import datetime


class Note:
    def __init__(self, id):
        self.id = id
        self.title = None
        self.description = None
        self.created_at = datetime.now().strftime('%m/%d/%Y, %H:%M')

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value: str):
        if isinstance(value, str) and len(f'{value}') is not 0:
            self.__dict__[key] = value
        elif len(f'{value}') > 120:
            raise ValueError(f'{key.title()} should be less than 120 characters!')
        else:
            raise ValueError(f'{key.title()} should contain at least one character!')

    def is_valid(self):
        return self.title is not None and self.description is not None

    def __str__(self):
        return f"Id: {self.id}; Title: {self.title}; Description: {self.description}; CreatedAt: {self.created_at}"
