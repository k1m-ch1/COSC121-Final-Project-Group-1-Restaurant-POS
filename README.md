# Restaurant POS ordering system

## Exposing the python program to the web

We use `gotty` to expose the terminal interface to the browser (probably not secure).

### Installing `gotty`

First install go.

```bash
sudo apt install go
```

or 

```bash
sudo pacman -Sy go
```

Make sure append the go directory to your PATH in your `.bashrc`

```bash
export PATH="$HOME/go/bin:$PATH"
```

Source your `.bashrc` or just open a new terminal

```bash
source ~/.bashrc
```

Then install `gotty`

```bash
go install github.com/sorenisanerd/gotty@latest
```

Check that gotty works

```bash
gotty -h
```
### Using `gotty`

#### Server Side

Make sure to first enter your virtual environment. Ex:

```bash
source ./venv/bin/activate
```

Then run your terminal based program (can use a different port too).

```bash
gotty -w -p 8080 python3 main.py
```

> [!NOTE]
> The flag `-w` enables standard in, into the program. This might be dangerous, and unsecure.

#### Client Side

Simply connect to it using your web browser. Using the previous example, use the url: `localhost:8080`.

To connect to it via the terminal, use `gotty-client`

```bash
go install github.com/moul/gotty-client/cmd/gotty-client@latest
```

To use it:

```bash
gotty-client -v2 localhost:8080
```

## Features

- Ability to login as guest/customers and order things
- Ability to login as admin/restaurant owner
- **Food info got: order id, name, price, category, short description, internal notes, in-stock, out of stock, time-based-availability**
- Category should include `["appetizers", "main", "desert", "drinks"]`
- Add colors and ANSI codes

### TODO displaying the menu

- [] design the "view menu" page
- [] design the fzf selection page

### TODO As Admin/Restaurant Owner

- `remove_item` needs to handle exception well to enable saving when hitting the escape key
- [x] password protected (make sure it's secure with hashing and stuff)
- [x] can add items (Tanatxx, lexsigma)
- [x] guest ordering system (Oudom)
- [x] search bar
- [x] can delete items (Tanatxx, lexsigma)
- [x] manage prices (Tanatxx, lexsigma)
- [x] store items and save it in file (Tanatxx, lexsigma)
- [x] make to format it well either in `csv` or `json` format
- [x] see what order is left to send out
- [x] manage customer's order (remove order once customer has paid)
- [x] print out receipt (lexsigma)
~- [] web storage~

### TODO As Guest


- [x] Assign table numbers or receipt number (Oudom)
- [x] But make sure to automatically assign table numbers and receipt numbers
- [x] pick food (Oudom)
- ~[] see what food will arrive or something~

### Technical Requirements

Technical Requirements: The project must use the following concepts in
Python:
- [x] Conditional Statements (obviously needed)
- [x] Loops (also need to order multiple items)
- [x] Function (different functions for different actions)
- [x] List, or Dictionary (for storage of food items, and customer orders)
- [x] Read/Write/Update/Delete to File (updating menus, and storage in a JSON file)
- [x] Interaction with the user through Terminal or other libraries (interaction through the terminal, with iterfzf acting as a search bar)

