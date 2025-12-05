# Restaurant POS ordering system

## Features

- Ability to login as guest/customers and order things
- Ability to login as admin/restaurant owner
- Food info got: order id, name, price, category, short description, internal notes, in-stock, out of stock, time-based-availability
- Add colors and ANSI codes

### TODO As Admin/Restaurant Owner

- [x] password protected (make sure it's secure with hashing and stuff)
- [x] can add items (Tanatxx, lexsigma)
- [x] guest ordering system (Oudom)
- [] search bar
- [x] can delete items (Tanatxx, lexsigma)
- [] manage prices (Tanatxx, lexsigma)
- [x] store items and save it in file (Tanatxx, lexsigma)
- [] make to format it well either in `csv` or `json` format
- [] see what order is left to send out
- [] manage customer's order (remove order once customer has paid)
- [x] print out receipt (lexsigma)
- [] web storage

### TODO As Guest


- [x] Assign table numbers or receipt number (Oudom)
- [] But make sure to automatically assign table numbers and receipt numbers
- [x] pick food (Oudom)
- [] see what food will arrive or something

### Technical Requirements

Technical Requirements: The project must use the following concepts in
Python:
- [x] Conditional Statements (obviously needed)
- [x] Loops (also need to order multiple items)
- [x] Function (different functions for different actions)
- [x] List, or Dictionary (for storage of food items, and customer orders)
- [x] Read/Write/Update/Delete to File (updating menus, and storage in a JSON file)
- [x] Interaction with the user through Terminal or other libraries (interaction through the terminal, with iterfzf acting as a search bar)
