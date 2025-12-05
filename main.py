import guest
import admin
import questionary

users = {
    "guest":guest.main,
    "admin":admin.main,
}

if __name__ == "__main__":
    user = ""
    while user not in users.keys():
        user = questionary.text("User: ").ask()
    users[user]()
