import bcrypt

with open("./password_hash.txt", 'r') as file:

    entered_pw = b"password123"
    password_hash = file.read().encode('utf-8')
    if bcrypt.checkpw(entered_pw, password_hash):
        print("Password match!")
    else:
        print("Incorrect password.")
