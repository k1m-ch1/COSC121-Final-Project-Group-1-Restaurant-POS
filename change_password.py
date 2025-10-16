import bcrypt

pw = b'password123'
h = bcrypt.hashpw(pw, bcrypt.gensalt()) # Hash password

with open("./password_hash.txt", 'w') as file:
    file.write(str(h))

