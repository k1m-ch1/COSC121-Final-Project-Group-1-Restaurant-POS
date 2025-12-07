import bcrypt
import json
from pypager.source import to_formatted_text, GeneratorSource
from pypager.pager import Pager
import constants
import uuid
import questionary
from guest import select_item, load_menu, view_menu, load_all_orders, handle_format_dict, print_receipt

def save_to_file(to_save:dict, saved_file_path:str) -> None:
    """Saves a dictionary to a designated json file path"""
    with open(saved_file_path, 'w') as file:
        file.write(json.dumps(to_save, indent=4))

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

def save_menu_and_exit(menu:dict) -> None:
    save_to_file(menu, constants.MENU_FILE)
    exit()

def view_all_orders(all_orders:dict) -> None:
    """View all orders from customers"""
    def get_orders():
        yield to_formatted_text(json.dumps(all_orders["orders"], indent=2))
    p = Pager()
    p.add_source(GeneratorSource(get_orders()))
    p.run()
"""
def select_item(menu_list:list) -> str|None:
    # might want a more descriptive error handling
    # refactor later...
    selected_item = iterfzf([f"{Fore.GREEN}{menu_item['category']:{max(map(lambda menu_item: len(menu_item['category']), menu_list))}}{Style.RESET_ALL}: {menu_item['name']:20} ${str(menu_item['price']):5} ({str(menu_item['id'])})" for menu_item in menu_list], prompt="Select an item: ", ansi=True)
    if selected_item == None:
        return None
    return re.match(r'.*\((.+)\).*', selected_item).group(1)
"""
def remove_orders(all_orders:dict) -> dict:
    """Remove customers orders when finished"""
    select_item()

    return all_orders

MENU_ACTION_DICT = {
    "view menu":view_menu,
    "add item":add_item,
    "remove item":remove_item,
    "save and exit":save_menu_and_exit
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
        all_orders = load_all_orders(constants.ORDERS_FILE)
        action_choice = questionary.select("Actions: ", choices=["manage menu", "manage orders", "exit"]).ask()
        if action_choice == "manage menu":
            choice = questionary.select("Menu Options: ",choices=list(MENU_ACTION_DICT.keys())).ask()
            MENU_ACTION_DICT[choice](menu)
        elif action_choice == "manage orders":
            choice = questionary.select("Order Options: ", choices=list(ORDERS_ACTION_DICT.keys())).ask()
            ORDERS_ACTION_DICT[choice]()
        else:
            save_menu_and_exit(menu)

if __name__ == '__main__':
    main()
