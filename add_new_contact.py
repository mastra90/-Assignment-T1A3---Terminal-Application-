import os
from formatting import top_lines

# Add a new contact
def add_new_contact(contacts):
    print("Please enter the following details:\n")
    name = input("Full name: ")

    if name in contacts:
        os.system('cls')
        top_lines ()
        print("\nContact already exists.\n")
        
    else:
        phone_num = input("Phone number: ")
        email = input("Email address: ")
        contacts[name] = [phone_num, email]
        print("\n" + name + " has been added to your contacts.\n")