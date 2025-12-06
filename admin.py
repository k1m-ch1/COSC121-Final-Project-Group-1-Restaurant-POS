import bcrypt
import json
import constants
import uuid
from iterfzf import iterfzf
import questionary
from guest import select_item, load_menu, view_menu

def save_menu(menu:dict, menu_file_path:str) -> None:
    """Saves the menu as a dictionary to a designated file path"""
    with open(menu_file_path, 'w') as file:
        file.write(json.dumps(menu, indent=4))

def is_float(target_str:str) -> bool:
    """Checks whether a given string can be successfully converted to a float"""
    try:
        float(target_str)
        return True
    except:
        return False

def add_item(menu:dict) -> dict:
    """Prompt the user for an item and returns back the dictionary (note that it will modify the dictionary so be careful)"""
    menu_formatting = menu["format"]
    new_entry = {
        "id":str(uuid.uuid4())
    }
    for info_field_name, info_field_type in menu_formatting.items():
        if type(info_field_type) == list:
            new_entry[info_field_name] = questionary.select(f"Choose {info_field_name}: ", choices=info_field_type).unsafe_ask()
        elif info_field_type == "str":
            new_entry[info_field_name] = questionary.text(f"Enter {info_field_name}: ").unsafe_ask()
        elif info_field_type == "bool":
            new_entry[info_field_name] = questionary.confirm(f"{info_field_name} ?").unsafe_ask()
        elif info_field_type == "float":
            new_entry[info_field_name] = questionary.text(f"Enter {info_field_name}: ", validate=lambda x: is_float(x) and float(x) > 0).unsafe_ask()
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

ACTION_DICT = {
    "view menu":view_menu,
    "add item":add_item,
    "remove item":remove_item,
    "save and exit":save_and_exit
}

def main():
    while not check_password():
        pass
    menu_file_path = constants.MENU_FILE
    menu = load_menu(menu_file_path)
    while True:
        choice = questionary.select("POS Menu Options: ",choices=list(ACTION_DICT.keys())).ask()
        ACTION_DICT[choice](menu)

if __name__ == '__main__':
    main()
