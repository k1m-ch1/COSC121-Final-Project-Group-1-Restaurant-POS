
from iterfzf import iterfzf
import re

FILENAME = "menu.txt"

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
    while (selected_item := iterfzf([f"{menu_item['name']} ({menu_item['id']})" for menu_item in menu_list], prompt="Select an item: ")) == None:
        pass
    return re.match(r'.*\((.+)\).*', selected_item).group(1)

def load_menu():
    menu = []
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    name, price = parts
                    menu.append({"name": name, "price": float(price)})
    except FileNotFoundError:
        print("Menu file not found.")
    return menu

def save_order(table, items):
    with open("orders.txt","a") as file:
        file.write(f"Table {table}: {', '.join(items)}\n")


def guest_order_flow():
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

def main():
    guest_order_flow()
