from enum import Enum


class Commands(Enum):
    EXIT = ["exit", "close"]
    HELLO = "hello"
    HELP = "help"
    ALL_CONTACTS = "all-contacts"
    ADD_CONTACT = "add-contact"
    CHANGE_CONTACT = "change-contact"
    PHONE = "phone"
    ADD_EMAIL = "add-email"
    ADD_BIRTHDAY = "add-birthday"
    SHOW_BIRTHDAY = "show-birthday"
    BIRTHDAYS = "birthdays"
    ADD_NOTE = "add-note"
    SHOW_NOTES = "all-notes"
    FIND_NOTE = "find-note"
    DELETE_NOTE = "delete-note"

    @classmethod
    def get_command(cls, command: str):
        for cmd in cls:
            if isinstance(cmd.value, list) and command in cmd.value:
                return cmd
            if isinstance(cmd.value, str) and command == cmd.value:
                return cmd
        return None

    @classmethod
    def all_commands(cls):
        commands = []
        for cmd in cls:
            if isinstance(cmd.value, list):
                commands.extend(cmd.value)
            else:
                commands.append(cmd.value)
        return commands

    @staticmethod
    def completer(text, state):
        options = [
            command for command in Commands.all_commands() if command.startswith(text)
        ]
        if state < len(options):
            return options[state]
        else:
            return None
