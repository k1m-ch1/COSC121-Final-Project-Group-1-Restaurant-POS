import bcrypt
import json
import constants
import uuid
from iterfzf import iterfzf
import questionary
from guest import select_item, load_menu, view_menu, load_all_orders, handle_format_dict

def save_menu(menu:dict, menu_file_path:str) -> None:
    """Saves the menu as a dictionary to a designated file path"""
    with open(menu_file_path, 'w') as file:
        file.write(json.dumps(menu, indent=4))

def add_item(menu:dict) -> dict:
    """Prompt the user for an item and returns back the dictionary (note that it will modify the dictionary so be careful)"""
    format_dict = menu["format"]
    new_entry = {
        "id":str(uuid.uuid4())
    }
    new_entry.update(handle_format_dict(format_dict))
    menu["menu"].append(new_entry)
    return menu

def remove_item(menu:dict) -> dict:
    """Removes a chosen item from the menu (menu dictionary will be modified. Be careful)"""
    target_item_id = select_item(menu["menu"])
    menu["menu"] = [menu_item for menu_item in menu["menu"] if menu_item["id"] != target_item_id]
    return menu

def check_password() -> bool:
    """"Prompt the user for a password and returns a boolean for whether the password is correct"""

    entered_password = questionary.password("password: ").unsafe_ask().encode('utf-8')

    with open("./password_hash.txt", 'r') as file:
            password_hash = file.read().encode('utf-8')
            return bcrypt.checkpw(entered_password, password_hash)

def save_and_exit(menu:dict) -> None:
    save_menu(menu, constants.MENU_FILE)
    exit()

def view_all_orders(all_orders:dict) -> None:
    """View all orders from customers"""
    pass

def remove_orders(all_orders:dict) -> dict:
    """Remove customers orders when finished"""
    return all_orders

MENU_ACTION_DICT = {
    "view menu":view_menu,
    "add item":add_item,
    "remove item":remove_item,
    "save and exit":save_and_exit
}

ORDERS_ACTION_DICT = {
    "view all orders":view_all_orders,
    "remove orders":remove_orders
}

def main():
    while not check_password():
        pass
    menu = load_menu(constants.MENU_FILE)
    while True:
        choice = questionary.select("POS Menu Options: ",choices=list(MENU_ACTION_DICT.keys())).ask()
        MENU_ACTION_DICT[choice](menu)

if __name__ == '__main__':
    main()
