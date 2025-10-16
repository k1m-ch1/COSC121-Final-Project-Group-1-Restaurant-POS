import guest
import admin

users = {
    "guest":guest.main,
    "admin":admin.main,
}

if __name__ == "__main__":
    user = ""
    while user not in users.keys():
        user = input("User: ")
    users[user]()
