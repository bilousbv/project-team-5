from enum import Enum


class Commands(Enum):
    EXIT = ['exit', 'close']
    HELLO = 'hello'
    ALL_CONTACTS = 'all'
    ADD_CONTACT = 'add-contact'
    CHANGE_CONTACT = 'change-contact'
    PHONE = 'phone'
    ADD_EMAIL = "add-email"
    ADD_BIRTHDAY = 'add-birthday'
    SHOW_BIRTHDAY = 'show-birthday'
    BIRTHDAYS = 'birthdays'
    ADD_NOTE = 'add-note'
    SHOW_NOTES = 'all-notes'
    FIND_NOTE = 'find-note'
    DELETE_NOTE = 'delete-note'

    @classmethod
    def get_command(cls, command: str):
        for cmd in cls:
            if isinstance(cmd.value, list) and command in cmd.value:
                return cmd
            if isinstance(cmd.value, str) and command == cmd.value:
                return cmd
        return None
