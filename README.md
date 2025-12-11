# Restaurant POS ordering system

## Running the program locally

First clone the repository

```bash
git clone https://github.com/k1m-ch1/COSC121-Final-Project-Group-1-Restaurant-POS.git
```

Change directory into the folder

```bash
cd COSC121-Final-Project-Group-1-Restaurant-POS
```

Create a new virtual environment (recommended)

```bash
python3 -m venv venv
```

Activate the environment

```bash
source ./venv/bin/activate
```

Install of the requirements

```bash
pip install -r ./requirements.txt
```

## Exposing the python program to the web

We use `gotty` to expose the terminal interface to the browser (probably not secure).

### Installing `gotty`

First install go.

```bash
sudo pacman -Sy go
```

Or somehow through their [website](https://go.dev/doc/install)

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

## Project Description

### Introduction

- Python Restaurant POS System
- Tanay Mehra, Kimchour Ly, Bun Oudom, Han Alex  
- Computer Science A(Fall Semester)
- Professor Mat Nab 

### Problem Statement

- The Point of Sales (POS) system solves core business problems like slow, error-prone manual transactions, poor inventory tracking, and disorganized sales data by automating payments, managing stock in real-time, and centralizing customer/sales info, leading to faster service, fewer mistakes, better decision-making, and improved customer satisfaction. 
- It is important because a POS system helps businesses streamline operations, proper management, and shows vital information for both the customer and the business owners.  
- Who are the intended users? The intended are business owners who want to boost their business and have proper management 

### Project Objectives

1. The first goal of the project is to make an entry-level POS system using Python fundamentals we have learn
2. The second goal of the project is to make a POS system that is accessible to the admin using a password system to check and add items, pieces to the menu. Then for the customer to use the POS for ordering and see the total bill at the end. 

### System Overview / Concept

- The system works in two ways. First, the admin can enter the system using a password and a login method in which the admin user can check the menu, add or remove items from the menu, and manage orders. Second, the guest can enter their name and add items like appetizer, main course, drinks, and dessert, which also shows the price, which finish it will print out a table will the list of items and their total at the end. 

### Key Python Features Used

- [x] Conditional Statements (obviously needed)
- [x] Loops (also need to order multiple items)
- [x] Function (different functions for different actions)
- [x] List, or Dictionary (for storage of food items, and customer orders)
- [x] Read/Write/Update/Delete to File (updating menus, and storage in a JSON file)
- [x] Interaction with the user through Terminal or other libraries (interaction through the terminal, with iterfzf acting as a search bar)


### Problems faced during implementation

- Git version control
- deciding on the correct design decisions
- deciding on the correct way to implement a feature
- naming variables

### Future Enhancements

- Get it on the WEB! Use REST api... man...
- Get a GUI or a TUI
- Add transactions!
- Enable users to update their orders or sth...
- Improve security!
- Write cleaner, maintainable code with better documentation
- Get a database instead of storing in a damn JSON
- Backup said database too!

### Conclusion

What we learned:

- all the basic features of a programming language
- data representation and storage
- a few functions from a lot of libraries
- a bit of git and version control
- a bit of hashing
- documenting code, and writing maintainable code

### Member Contributions

- [commit history](https://github.com/k1m-ch1/COSC121-Final-Project-Group-1-Restaurant-POS/graphs/commit-activity)
- [contributor's page](https://github.com/k1m-ch1/COSC121-Final-Project-Group-1-Restaurant-POS/graphs/contributors)
- [todo at readme](https://github.com/k1m-ch1/COSC121-Final-Project-Group-1-Restaurant-POS#:~:text=TODO%20As%20Admin%2FRestaurant%20Owner)
