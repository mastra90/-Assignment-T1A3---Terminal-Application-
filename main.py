import os
from formatting import press_enter, top_lines, bot_lines

# A function to print the main menu of the application
def main_menu():
    os.system('cls')
    print("Welcome to the Address Book application!\n")
    print("1. View all contacts")
    print("2. Search contacts")
    print("3. Add new contact")
    print("4. Edit a contact")
    print("5. Delete a contact")
    print("6. Quit application\n")
    user_input = input("Please enter your choice (1-6): ")
    return user_input

# Function to clear terminal
def clear():
    os.system('cls')

# Main program
user_input = ""
while user_input != "6":
    user_input = main_menu()
    if user_input == "1":
        clear()
        top_lines()
        print("---All Contacts---\n")
        print("View all contacts - function")
        bot_lines()
        press_enter()
    elif user_input == "2":
        clear()
        top_lines()
        print("---Search Contacts---\n")
        print("Search contacts - function")
        bot_lines()
        press_enter()
    elif user_input == "3":
        clear()
        top_lines()
        print("---Add New Contact---\n")
        print("Add new contact - function")
        bot_lines()
        press_enter()
    elif user_input == "4":
        clear()
        top_lines()
        print("---Edit a Contact---\n")
        print("Edit a contact - function")
        bot_lines()
        press_enter()
    elif user_input == "5":
        clear()
        top_lines()
        print("---Delete a Contact---\n")
        print("Delete a contact - function")
        bot_lines()
        press_enter()
    elif user_input == "6":
        clear()
        print("\nYou have quit the application. Goodbye!\n")
   



