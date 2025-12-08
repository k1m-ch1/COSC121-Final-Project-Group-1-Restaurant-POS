import guest
import admin
import questionary

users = {
    "guest":guest.main,
    "admin":admin.main,
}

if __name__ == "__main__":
    user = ""
    user = questionary.select("User: ", choices=users.keys()).ask()
    users[user]()
