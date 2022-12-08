# A function to print the main menu of the application
def main_menu():
    print("Welcome to the Address Book application!\n")
    print("1. View all contacts")
    print("2. Search contacts")
    print("3. Enter new contact")
    print("4. Edit contact")
    print("5. Delete contact")
    print("6. Quit application\n")
    user_input = input("Please enter your choice (1-6): ")
    return user_input

main_menu()