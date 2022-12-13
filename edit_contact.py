import os
from formatting import top_lines
from formatting import top_lines, contact_not_found

# Edit a contact.
def edit_contact(contacts):
    name = input("Full name of contact to edit (case sensitive): ")
    if name in contacts:
        phone_num = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        contacts[name] = [phone_num, email]
        print("\n" + name + "'s information has been updated.\n")
    else:
        os.system('clear')
        top_lines ()
        contact_not_found()