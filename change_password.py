import bcrypt
import getpass

entered_password = getpass.getpass("Enter password: ").encode('utf-8')
h = bcrypt.hashpw(entered_password, bcrypt.gensalt())

with open("./password_hash.txt", 'w') as file:
    file.write(h.decode())

