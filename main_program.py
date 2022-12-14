import os
from add_new_contact import add_new_contact
from delete_contact import delete_contact
from edit_contact import edit_contact
from formatting import press_enter, top_lines, bot_lines
from main_menu import main_menu
from search_contact import search_contact
from text_file_config import read_contacts, save_contacts
from view_contacts import view_contacts


# Clear terminal
def clear():
    os.system('clear')


# Main program
contacts = read_contacts()
user_input = main_menu()
while user_input != "6": 

# View all contacts.
    if user_input == "1":
        clear()
        top_lines()
        text = "\nALL CONTACTS"
        title = "\x1B[1;4m" + text + "\x1B[0m" + ":\n"
        print(title)
        view_contacts(contacts)
        bot_lines ()
        press_enter()
    
# Search for a contact.  
    elif user_input == "2":
        clear()
        top_lines()
        text = "\nSEARCH CONTACTS"
        title = "\x1B[1;4m" + text + "\x1B[0m" + ":\n"
        print(title)
        search_contact(contacts)
        bot_lines()
        press_enter()

# Add a new contact.
    elif user_input == "3":
        clear()
        top_lines()
        text = "\nADD NEW CONTACT"
        title = "\x1B[1;4m" + text + "\x1B[0m" + ":\n"
        print(title)
        add_new_contact(contacts)
        press_enter()

# Edit a contact.
    elif user_input == "4":
        clear()
        top_lines()
        text = "\nEDIT A CONTACT"
        title = "\x1B[1;4m" + text + "\x1B[0m" + ":\n"
        print(title)
        edit_contact(contacts)
        bot_lines()
        press_enter()

# Delete a contact
    elif user_input == "5":
        clear()
        top_lines()
        text = "\nDELETE A CONTACT"
        title = "\x1B[1;4m" + text + "\x1B[0m" + ":\n"
        print(title)
        delete_contact(contacts)
        bot_lines()
        press_enter()

# Invalid entry (if user did not choose a number between 1-6)
    else:
        clear()
        top_lines()
        text = "\nERROR!"
        title = "\x1B[1;4m" + text + "\x1B[0m" + "\n"
        print(title)
        print("Your Input not valid.")
        print("Please enter a number between 1-6.\n")
        bot_lines()
        press_enter()

    save_contacts(contacts)
    user_input = main_menu()

clear()
top_lines()
print("\nYou have quit the application. Goodbye!\n")
bot_lines()

   




