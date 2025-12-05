import bcrypt
import json
import constants
import uuid
from iterfzf import iterfzf
import questionary
from guest import select_item

# note that the 'format' dictionary can only be 'str', 'bool', 'float' and categories with strings for now
BARE_MINIMUM_MENU = {
    "format": {
        "name":"str",
        "category": [
            "appetizers",
            "main",
            "desert",
            "drinks"
        ],
        "price":"float",
        "description":"str",
        "available":"bool"
    },
    "menu": []
}

def load_menu(menu_file_path) -> dict:
    """Reads a file that stores the menu and returns it as a dictionary."""
    global BARE_MINIMUM_MENU
    menu = dict()

    try:
        with open(menu_file_path, 'r') as file:
                menu = json.loads(file.read())
    except (FileNotFoundError, json.JSONDecodeError):
        menu = BARE_MINIMUM_MENU
    return menu

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

def get_item(menu:dict) -> dict:
    """Prompt the user for an item and returns back the dictionary (note that it will modify the dictionary so be careful)"""
    menu_formatting = menu["format"]
    new_entry = {
        "id":str(uuid.uuid4())
    }
    for info_field_name, info_field_type in menu_formatting.items():
        if type(info_field_type) == list:
            new_entry[info_field_name] = questionary.select(f"Choose {info_field_name}: ", choices=info_field_type).ask()
        elif info_field_type == "str":
            new_entry[info_field_name] = questionary.text(f"Enter {info_field_name}: ").ask()
        elif info_field_type == "bool":
            new_entry[info_field_name] = questionary.confirm(f"{info_field_name} ?").ask()
        elif info_field_type == "float":
            new_entry[info_field_name] = questionary.text(f"Enter {info_field_name}: ", validate=lambda x: is_float(x) and float(x) > 0).ask()
    menu["menu"].append(new_entry)
    return menu

def remove_item(menu:dict) -> dict:
    """Removes a chosen item from the menu (menu dictionary will be modified. Be careful)"""
    target_item_id = select_item(menu["menu"])
    menu["menu"] = [menu_item for menu_item in menu["menu"] if menu_item["id"] != target_item_id]
    return menu


def view_menu(menu):
    pass

PASSWORD_HASH_FILE = "./password_hash.txt"

def check_password() -> bool:
    """"Prompt the user for a password and returns a boolean for whether the password is correct"""

    entered_password = questionary.password("password: ").ask().encode('utf-8')

    with open("./password_hash.txt", 'r') as file:
            password_hash = file.read().encode('utf-8')
            return bcrypt.checkpw(entered_password, password_hash)

def main():
    while not check_password():
        pass

    menu_file_path = constants.MENU_FILE
    menu = load_menu(menu_file_path)
    get_item(menu)
    save_menu(menu, menu_file_path)
    remove_item(menu)
    print(json.dumps(menu, indent=2))
    #print(select_item(menu["menu"]))
#    while True:
#        print("\nPOS Menu Options:")
#        print("1. View Menu")
#        print("2. Add Item")
#        print("3. Remove Item")
#        print("4. Quit")
#        
#        choice = input("Choose an option (1-4): ").strip()
#        
#        if choice == '1':
#            view_menu(menu)
#        elif choice == '2':
#            add_item(menu)
#        elif choice == '3':
#            remove_item(menu)
#        elif choice == '4':
#            print("Exiting program.")
#            break
#        else:
#            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
