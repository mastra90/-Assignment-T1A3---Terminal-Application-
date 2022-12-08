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

# Main program
user_input = ""
while user_input != "6":
    user_input = main_menu()
    if user_input == "1":
        print("Views all contacts function")
    elif user_input == "2":
        print("Search contacts function")
    elif user_input == "3":
        print("Enter new contacts function")
    elif user_input == "4":
        print("Edit contacts function")
    elif user_input == "5":
        print("Delete contacts function")
    elif user_input == "6":
        print("Thanks for using the application!")
   



