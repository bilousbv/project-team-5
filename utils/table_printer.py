from prettytable import PrettyTable, ALL
from colorama import Fore, Style


def table_printer(headers, rows):
  table = PrettyTable()
  table.top_left_junction_char = f"{Fore.LIGHTCYAN_EX}╔"
  table.horizontal_char = "═"
  table.vertical_char = "║"
  table.junction_char = "╬"
  table.left_junction_char = "╠"
  table.right_junction_char = "╣"
  table.top_junction_char = "╦"
  table.top_right_junction_char = "╗"
  table.bottom_junction_char = "╩"
  table.bottom_left_junction_char = "╚"
  table.bottom_right_junction_char = f"╝{Style.RESET_ALL}"
  table.hrules = ALL
  table.field_names = headers
  table.add_rows(rows)
  return table
