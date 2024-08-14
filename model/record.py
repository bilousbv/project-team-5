from colorama import Fore
from model.phone import Phone
from model.name import Name


class Record:
  def __init__(self, name: str):
    self.name = Name(name)
    self.phones = []
    self.birthday = None

  def add_phone(self, phone: str):
    try:
      self.phones.append(Phone(phone))
      return True
    except ValueError as e:
      print(e)
      return False

  def remove_phone(self, phone: str):
    for i in self.phones[:]:
      if i.value == phone:
        self.phones.remove(i)

  def edit_phone(self, phone_to_edit: str, new_phone: str):
    for i in self.phones[:]:
      if i.value == phone_to_edit:
        try:
          self.phones.append(Phone(new_phone))
        except ValueError:
          return f"{Fore.LIGHTRED_EX}New phone value is incorrect{Fore.RESET}"
        self.phones.remove(i)
        return f"{Fore.GREEN}Phone updated{Fore.RESET}"

    return f"{Fore.LIGHTRED_EX}Phone to edit does not exists for such user{Fore.RESET}"

  def find_phone(self, phone: str):
    for i in self.phones:
      if i.value == phone:
        return i

  def add_birthday(self, birthday):
    self.birthday = birthday

  def __str__(self):
    return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"
