#Admin system for adding items 
# Creates an empty list for adding and removing items 
menu_items = []

def add_item_menu(name, price): 
    item = {
        "name": name.strip(), 
        "price": float(price)  
    }
    menu_items.append(item)
    print(f"{name} added to the menu.")


#Removes items from the list 
def remove_item_menu(name): 
 for item in menu_items:
    if item["name"].lower() == name.lower():
        menu_items.remove(item)
    print(f"{name} removed from the menu.")
    return
 print(f"{name} not found in the menu.") 

#Main Loop for repeating the process to add the items and it will stop when the use gives the quit command 
while True: 
    input_item = input("Enter an item on the menu(name, price) or q(quit): ")

    if input_item.lower() == "q":  
        break 

try: 
    name,price = input_item.split(",")
    add_item_menu(name, price) 
except: 
    print("Invalid input. Please try again.")

#Main Loop for repeating the process to remove the items and it will stop when the use gives the quit command
while True: 
    input_remove_item = input("Enter an item on the menu to remove or q(quit): ")

    if input_remove_item.lower() == "q": 
        break 
    remove_item_menu(input_remove_item) 

#Gives out the final menu list 
print("Final Menu List: ", menu_items)

'''
This code still has issue, fix soon 
''' 
