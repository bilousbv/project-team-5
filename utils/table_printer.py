from prettytable import PrettyTable, ALL
from colorama import Fore


def table_printer(headers, rows):
  table = PrettyTable()
  table.top_left_junction_char = f"{Fore.LIGHTCYAN_EX}╔{Fore.RESET}"
  table.horizontal_char = f"{Fore.LIGHTCYAN_EX}═{Fore.RESET}"
  table.vertical_char = f"{Fore.LIGHTCYAN_EX}║{Fore.RESET}"
  table.junction_char = f"{Fore.LIGHTCYAN_EX}╬{Fore.RESET}"
  table.left_junction_char = f"{Fore.LIGHTCYAN_EX}╠{Fore.RESET}"
  table.right_junction_char = f"{Fore.LIGHTCYAN_EX}╣{Fore.RESET}"
  table.top_junction_char = f"{Fore.LIGHTCYAN_EX}╦{Fore.RESET}"
  table.top_right_junction_char = f"{Fore.LIGHTCYAN_EX}╗{Fore.RESET}"
  table.bottom_junction_char = f"{Fore.LIGHTCYAN_EX}╩{Fore.RESET}"
  table.bottom_left_junction_char = f"{Fore.LIGHTCYAN_EX}╚{Fore.RESET}"
  table.bottom_right_junction_char = f"{Fore.LIGHTCYAN_EX}╝{Fore.RESET}"
  table.hrules = ALL
  table.field_names = headers
  table.add_rows(rows)
  return table
