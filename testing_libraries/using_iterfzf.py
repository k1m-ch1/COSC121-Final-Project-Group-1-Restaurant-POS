
from iterfzf import iterfzf

items = ["name: John", "age: 30", "country: US"]
choice = iterfzf(items)

print("You picked:", choice)

field = choice.split(":")[0]
new_value = input(f"Enter new value for {field}: ")
