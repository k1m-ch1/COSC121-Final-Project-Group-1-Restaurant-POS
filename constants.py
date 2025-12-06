MENU_FILE = "menu.json"
ORDERS_FILE = "orders.json"

# note that the 'format' dictionary can only be 'str', 'bool', 'float' and categories with strings for now
BARE_MINIMUM_MENU = {
    "format": {
        "name":"str",
        "category": [
            "appetizers",
            "main",
            "desert",
            "drinks"
        ],
        "price":"float",
        "description":"str",
        "available":"bool"
    },
    "menu": []
}

BARE_MINIMUM_ORDERS = {
    "format": {
        "name":"str",
        "orders":{
            "str":"int"
        },
        "description":"str",
    },
    "orders": []
}

PASSWORD_HASH_FILE = "./password_hash.txt"

