# Restaurant POS ordering system

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

### The Slide Guide
### Slide 1 — Title Slide
• Python Restaurant POS System
• Tanay Mehra, Kimchour Ly, Bun Oudom, Han Alex  
• Computer Science A(Fall Semester)
• Professor Mat Nab 

### Slide 2 — Problem Statement
• The Point of Sala(POS) system solves core business problems like slow, error-prone manual transactions, poor inventory tracking, and disorganized sales data by automating payments, managing stock in real-time, and centralizing customer/sales info, leading to faster service, fewer mistakes, better decision-making, and improved customer satisfaction. 
• It is important because a POS system helps businesses streamline operations, proper management, and shows vital information for both the customer and the business owners.  
• Who are the intended users? The intended are business owners who want to boost their business and have proper management 

### Slide 3 — Project Objectives
• 2–4 clear goals of your project
1. The first goal of the project is to make an entry-level POS system using Python fundamentals we have learn
2. The second goal of the project is to make a POS system that is accessible to the admin using a password system to check and add items, pieces to the menu. Then for the customer to use the POS for ordering and see the total bill at the end. 

### Slide 4 — System Overview / Concept
• Short explanation of how the system works
The system works in two ways. First, the admin can enter the system using a password and a login method in which the admin user can check the menu, add or remove items from the menu, and manage orders. Second, the guest can enter their name and add items like appetizer, main course, drinks, and dessert, which also shows the price, which finish it will print out a table will the list of items and their total at the end. 

### Slide 5 — Key Python Features Used
List the main topics you applied, such as:
• Variables:
• Functions: The functions we used are for the admin, guest, menu, orders, change password, and the main function to tie all of it together
• Loops & Conditionals
• Lists / Dictionaries
• OOP Concepts (Classes, Objects, Methods)
• File Handling / Modules (if used)

### Slide 6 — Core Features / Functions
• Show and explain 2–4 important functions or features of
your program
• Keep code snippets short (5–8 lines max)
• Explain what the code does, not every line

### Slide 8 — Challenges & Solutions
• What was difficult?
• How did you solve it?
• What did you learn?

### Slide 9 — Demo
• Show your program running
• Demonstrate important features

### Slide 10 — Limitations/Challenges
• What is your problem during implementation how did you
solve it?
• What doesn’t work yet?
• What could be improved?

### Slide 11 — Future Enhancements
• Features you want to add if you had more time
• Example: GUI upgrade, login system, database support,
etc.
    - In the future, if we want to update this program, we would like to update the GUI from text-based to a visual-based GUI for easier navigation. 
    
### Slide 12 — Conclusion
• What did you learn about Python? : We learn the core basics of the fundamentals of Python from the syntax, variables, and functions. We also learned programming by doing practice. 
• How did this project help you understand programming? : This project helps us to understand programming by helping us to write a program based on what we learn.  

### Slide 13 — Member Contributions
• List each team member and their role/contribution
