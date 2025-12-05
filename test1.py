username = "python"
password = "123"
orders = []
session_orders = []
menu = {}
attempts = 3

def admin():
    print("Welcome back Admin, What would you like to do?")
    while True:
        choice_input = input("1. Add items\n2. Delete items\n3. Manage price\n4. View menu\n5. Exit\n").strip()

        if not choice_input:
            print("Invalid input, please enter 1-5")
            continue

        try:
            choice = int(choice_input)
        except ValueError:
            print("Invalid input, please enter a number 1-5")
            continue

        match choice:
            case 1:
                add_items = input("What would you like to add? ")
                try:
                    price = float(input("Price: "))
                    if price <= 0:
                        print ("Invalid price, must be positive.")
                        continue
                except ValueError:
                    print ("Invalid input, please enter a valid number")
                    continue
                menu[add_items] = price
                print(f"{add_items} has been added to the menu")
            case 2:
                remove_items = input("What would you like to remove? ")
                if remove_items in menu:
                    del menu[remove_items]
                    print(f"{remove_items} has been removed from the menu")
                else:
                    print(f"{remove_items} not found in menu")
            case 3:
                change_price = input("Which item's price would you like to change? ")
                if change_price in menu:
                    new_price = float(input(f"Enter the new price for {change_price}: "))
                    menu[change_price] = new_price
                    print(f"{change_price}'s price has been changed to {new_price}")
                else:
                    print(f"{change_price} not found in menu.")
            case 4:
                if menu:
                    print("Current menu:")
                    for item, price in menu.items():
                        print(f"{item}: ${price}")
                    print (f"Total items: {len(menu)}")
                else:
                    print("Menu is currently empty.")
            case 5:
                print("Exiting admin panel...")
                return
            case _:
                print("Invalid input, Try again")
def guest():
    if not menu:
        print ("Nothing available right now, please come later.")
        return

    total = 0
    while True:
        print ("Current menu:")
        for item, price in menu.items():
            print (f"{item}: ${price}")

        ordering = input("What would you like to order? Enter exit to leave.")

        if ordering.lower() == "exit":
            print_receipt()
            print ("Thanks for visiting Python!")
            break
        if not ordering.lower():
            print ("Invalid order, Try again!")
            continue
        if ordering in menu:
            session_orders.append(ordering)
            orders.append(ordering)
            total += menu[ordering]
            print (f"You ordered {ordering}")
        else:
            print (f"{ordering} not in the menu.")

def login():
    global attempts
    while True:
        print ("Welcome to Python Restaurant")
        log_in = input("Would you like to proceed as Admin or Guest?")

        if log_in.lower() == "admin":
            while attempts > 0:
                input_username = input("Enter username: ")
                input_password = input("Enter password: ")

                if input_username == username and input_password == password:
                    print ("Login successful!")
                    admin()
                    break
                else:
                    attempts -= 1
                    print (f"Login failed, {attempts} left")

            if attempts == 0:
                print ("Too many attempts. Try again later")

        elif log_in.lower() == "guest":
            guest()
        else:
            print ("Invalid input. Enter Admin or Guest")

def print_receipt():
    if not session_orders:
        print("You haven’t ordered anything yet.")
        return

    print("\n========== RECEIPT ==========")
    total = 0
    for item in session_orders:
        price = menu[item]
        total += price
        print(f"{item} - ${price:.2f}")
    print("-----------------------------")
    print(f"Total: ${total:.2f}")
    print("=============================\n")
    session_orders.clear()

if __name__ == '__main__':
    login()
