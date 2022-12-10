import os
from main_menu import main_menu
from formatting import press_enter, top_lines, bot_lines
from view_contacts import view_contacts
from search_contact import search_contact
from add_new_contact import add_new_contact
from text_file_config import read_contacts, save_contacts
from edit_contact import edit_contact

# Function to clear terminal
def clear():
    os.system('cls')

# Main program
contacts = read_contacts()
user_input = main_menu()
while user_input != "6": 
    if user_input == "1":
        clear()
        top_lines()
        print("---All Contacts---\n")
        view_contacts(contacts)
        bot_lines()
        press_enter()
        
    elif user_input == "2":
        clear()
        top_lines()
        print("---Search Contacts---\n")
        search_contact(contacts)
        bot_lines()
        press_enter()

    elif user_input == "3":
        clear()
        top_lines()
        print("---Add New Contact---\n")
        add_new_contact(contacts)
        bot_lines()
        press_enter()

    elif user_input == "4":
        clear()
        top_lines()
        print("---Edit a Contact---\n")
        edit_contact(contacts)
        bot_lines()
        press_enter()

    elif user_input == "5":
        clear()
        top_lines()
        print("---Delete a Contact---\n")
        print("Delete a contact - function")
        bot_lines()
        press_enter()

    else:
        clear()
        print("**********ERROR!**********\n")
        print("Your Input not valid\n")
        print("Please enter a number between 1-6\n")
        press_enter()

    save_contacts(contacts)
    user_input = main_menu()

print("\nYou have quit the application. Goodbye!\n")

   




