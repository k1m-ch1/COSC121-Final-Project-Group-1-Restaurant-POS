import bcrypt
import getpass
import admin_actions
from test1 import admin

PASSWORD_HASH_FILE = "./password_hash.txt"

def check_password():
    entered_password = getpass.getpass("password: ").encode('utf-8')
    with open("./password_hash.txt", 'r') as file:
            password_hash = file.read().encode('utf-8')
            return bcrypt.checkpw(entered_password, password_hash)

def main():
    # place a password condition here
    while not check_password():
        pass

    admin_actions.main()
