from iterfzf import iterfzf
import re
from colorama import init, Fore, Back, Style
import json
import constants
from pypager.source import GeneratorSource
from pypager.pager import Pager
from prompt_toolkit.formatted_text import ANSI, to_formatted_text
from colorama import init, Fore, Style


# initialize colorama
init()

FILENAME = "menu.txt"

def view_menu(menu:dict) -> None:
    """Show the menu as pager"""

    def get_formatted_menu():
        for menu_item in menu["menu"]:
            ansi_line = "-"*20 + "\n"
            for menu_info_field_key, menu_info_field_value in menu_item.items():
                ansi_line += f"{menu_info_field_key}: {menu_info_field_value}\n"
            ansi_line += "-"*20 + "\n"
            fragments = list(to_formatted_text(ANSI(ansi_line)))
            # yield a list of (style_str, text) fragments
            yield fragments

    p = Pager()
    p.add_source(GeneratorSource(get_formatted_menu()))
    p.run()


def load_menu(menu_file_path) -> dict:
    """Reads a file that stores the menu and returns it as a dictionary."""
    menu = dict()
    try:
        with open(menu_file_path, 'r') as file:
                menu = json.loads(file.read())
    except (FileNotFoundError, json.JSONDecodeError):
        menu = constants.BARE_MINIMUM_MENU
    return menu

def select_item(menu_list:list) -> str:
    """
    Uses iterfzf to uniquely select an item inside the menu according to its name, while returning its UUID.

    Args:
        menu_list (list): A list of menu items in the menu dictionary.

    Returns:
        str: the UUID of the selected menu item
    """
    selected_item = ""
    # might want a more descriptive error handling
    # refactor later...
    while (selected_item := iterfzf([f"{Fore.GREEN}{menu_item['category']:{max(map(lambda menu_item: len(menu_item['category']), menu_list))}}{Style.RESET_ALL}: {menu_item['name']:20} ${str(menu_item['price']):5} ({str(menu_item['id'])})" for menu_item in menu_list], prompt="Select an item: ", ansi=True)) == None:
        pass
    return re.match(r'.*\((.+)\).*', selected_item).group(1)

def save_order(table, items):
    with open("orders.txt","a") as file:
        file.write(f"Table {table}: {', '.join(items)}\n")


def guest_order_flow():
    """
    menu = load_menu()

    print("\n--- Welcome Guest ---")
    table = input("Enter your table number: ")

    print("\n--- Menu ---")
    for i, item in enumerate(menu, 1):
        print(f"{i}. {item['name']} - ${item['price']}")

    print("\nType item numbers separated by commas (e.g., 1,3,5)")
    choices = input("Your choice: ").split(",")

    chosen_items = []
    for c in choices:
        c = c.strip()
        if c.isdigit() and 1 <= int(c) <= len(menu):
            chosen_items.append(menu[int(c)-1]["name"])

    save_order(table, chosen_items)
    print("\nOrder placed successfully!")
    print(f"Table {table} ordered: {', '.join(chosen_items)}")
    """

def main():
    guest_order_flow()
