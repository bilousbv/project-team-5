from assistant_bot.model.field import Field


class Tag(Field):
    def __init__(self, value: str):
        super().__init__(value)
