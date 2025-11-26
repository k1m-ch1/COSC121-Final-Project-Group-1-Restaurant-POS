FILENAME = "menu.txt"

def load_menu():
    menu = []
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    name, price = parts
                    menu.append({"name": name.strip(), "price": float(price)})
    except FileNotFoundError:
        pass
    except ValueError:
        print("Warning: Could not parse some lines in menu.txt")
    return menu

def save_menu(menu):
    try:
        with open(FILENAME, "w") as file:
            for item in menu:
                file.write(f"{item['name']},{item['price']}\n")
    except IOError as e:
        print(f"Error saving menu: {e}")

def add_item(menu):
    try:
        user_input = input("Enter item name and price separated by comma (e.g., Apple, 1.5): ")
        name, price = user_input.split(",")
        name = name.strip()
        price = float(price.strip())
        
        menu.append({"name": name, "price": price})
        save_menu(menu)
        print(f"'{name}' added to menu.")
    except ValueError:
        print("Invalid input. Please use format: Name, Price (numeric)")

def remove_item(menu):
    name_to_remove = input("Enter the name of the item to remove: ").strip()
    
    found = False

    for item in menu[:]:
        if item["name"].lower() == name_to_remove.lower():
            menu.remove(item)
            found = True
            print(f"'{item['name']}' removed from menu.")
    
    if found:
        save_menu(menu)
    else:
        print(f"Item '{name_to_remove}' not found.")

def view_menu(menu):
    if not menu:
        print("\nThe menu is empty.")
    else:
        print("\n--- Current Menu ---")
        for i, item in enumerate(menu, 1):
            print(f"{i}. {item['name']}: ${item['price']:.2f}")
        print("--------------------\n")

def main():
    menu = load_menu()
    
    while True:
        print("\nPOS Menu Options:")
        print("1. View Menu")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Quit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == '1':
            view_menu(menu)
        elif choice == '2':
            add_item(menu)
        elif choice == '3':
            remove_item(menu)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()