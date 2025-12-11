import guest
import admin
import questionary

users = {
    "guest":guest.main,
    "admin":admin.main,
    "exit":exit
}

if __name__ == "__main__":
    while True:
        user = questionary.select("User: ", choices=users.keys()).ask()
        users[user]()
