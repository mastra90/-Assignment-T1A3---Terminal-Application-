import os

# The main menu of the application
def main_menu():
    os.system('clear')
    print("Welcome to your Contacts Book application!\n")
    print("1. View all contacts")
    print("2. Search contacts")
    print("3. Add new contact")
    print("4. Edit a contact")
    print("5. Delete a contact")
    print("6. Quit application\n")
    user_input = input("Please enter your choice (1-6): ")
    return user_input