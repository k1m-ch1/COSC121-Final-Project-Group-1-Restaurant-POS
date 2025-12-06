from prompt_toolkit.shortcuts import radiolist_dialog, input_dialog

menu = [('name', 'Edit name'), ('age', 'Edit age'), ('quit', 'Quit')]

choice = radiolist_dialog(
    title="Menu",
    text="Choose item to edit",
    values=menu
).run()

if choice == "name":
    new_name = input_dialog(title="Name", text="Enter new name:").run()
