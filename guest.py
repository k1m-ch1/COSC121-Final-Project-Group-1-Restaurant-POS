from iterfzf import iterfzf
import re
from colorama import init, Fore, Back, Style
import json
import constants
import questionary
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

def select_item(menu_list:list) -> str|None:
    """
    Uses iterfzf to uniquely select an item inside the menu according to its name, while returning its UUID.

    Args:
        menu_list (list): A list of menu items in the menu dictionary.

    Returns:
        str: the UUID of the selected menu item
    """
    # might want a more descriptive error handling
    # refactor later...
    selected_item = iterfzf([f"{Fore.GREEN}{menu_item['category']:{max(map(lambda menu_item: len(menu_item['category']), menu_list))}}{Style.RESET_ALL}: {menu_item['name']:20} ${str(menu_item['price']):5} ({str(menu_item['id'])})" for menu_item in menu_list], prompt="Select an item: ", ansi=True)
    if selected_item == None:
        return None
    return re.match(r'.*\((.+)\).*', selected_item).group(1)

def load_all_orders(all_orders_file_path:str) -> dict:
    """Returns an 'all_orders' dictionary by reading an all orders json file"""
    all_orders = dict()
    try:
        with open(all_orders_file_path, 'r') as file:
                all_orders = json.loads(file.read())
    except (FileNotFoundError, json.JSONDecodeError):
        all_orders = constants.BARE_MINIMUM_ORDERS
    return all_orders

def save_orders(orders:dict, all_orders_file_path:str) -> None:
    """Saves the customer's order into the orders file"""
    all_orders = load_all_orders(all_orders_file_path)
    all_orders["orders"].append(orders)
    with open(all_orders_file_path, 'w') as file:
        file.write(json.dumps(all_orders, indent=4))

def is_float(target_str:str) -> bool:
    """Checks whether a given string can be successfully converted to a float"""
    try:
        float(target_str)
        return True
    except:
        return False

def handle_format_dict(format_dict:dict, menu_list:list=list()) -> dict:
    """Returns a new entry based on the format dict. Prompt the user based on the format dict."""
    new_entry = dict()
    for info_field_name, info_field_type in format_dict.items():
        if type(info_field_type) == list:
            new_entry[info_field_name] = questionary.select(f"Choose {info_field_name}: ", choices=info_field_type).unsafe_ask()
        elif type(info_field_type) == dict:
            # when it's a dictionary, implement multiselect with quantity selection
            new_entry[info_field_name] = dict()
            while True:
                selected_item = select_item(menu_list)
                if selected_item == None:
                    break
                quantity = questionary.text("Enter the quantity: ",validate=lambda x:x.isdigit() and int(x) > 0).unsafe_ask()
                new_entry[info_field_name][selected_item] = int(quantity)

        elif info_field_type == "str":
            new_entry[info_field_name] = questionary.text(f"Enter {info_field_name}: ").unsafe_ask()
        elif info_field_type == "bool":
            new_entry[info_field_name] = questionary.confirm(f"{info_field_name} ?").unsafe_ask()
        elif info_field_type == "float":
            new_entry[info_field_name] = questionary.text(f"Enter {info_field_name}: ", validate=lambda x: is_float(x) and float(x) > 0).unsafe_ask()
        elif info_field_type == "int":
            new_entry[info_field_name] = questionary.text(f"Enter {info_field_name}: ", validate=lambda x: x.isdigit()).unsafe_ask()
    return new_entry


def add_order(all_orders:dict, menu:dict) -> dict:
    """Prompt the user for order details, and returns an order dictionary"""
    new_entry = handle_format_dict(all_orders["format"], menu["menu"])
    return new_entry


def view_orders(orders:dict) -> None:
    """Opens a pager that lets the customer view their orders"""
    pass

def order(orders:dict) -> dict:
    """Returns a dictionary of orders, such that the new order gets appended to it. Note that the orders dictionary will have the id of the item in the menu as the key, while the quantity of order will be its value"""
    pass
    return orders

def print_receipt(orders:dict, menu:dict) -> None:
    """Prints receipt given the order dictionary and the menu dictionary"""
    pass

GUEST_ACTION_DICT = {
    "view orders":view_orders,
}

def main():
    #while True:
    #    questionary.select("What would you like to do?", )
    all_orders = load_all_orders(constants.ORDERS_FILE)
    menu = load_menu(constants.MENU_FILE)
    print(add_order(all_orders, menu))

    #guest_order_flow()
if __name__ == "__main__":
    main()
