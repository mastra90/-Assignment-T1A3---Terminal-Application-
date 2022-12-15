import os
from formatting import top_lines
from formatting import top_lines, contact_not_found

# Edit a contact.
def edit_contact(contacts):
    name = input("Full name of contact to edit (case sensitive): ")
    if name in contacts:
        phone_num = input("Enter new phone number: ")
        while True:
            email = input("Enter new email address: ")
            if " " in email:
                print("\nDo not use spaces in email addresses!")
                print("Please try again.\n")
            else:
                contacts[name] = [phone_num, email]
                os.system('clear')
                top_lines()
                print("\n" + name + "'s information has been updated.\n")
                break
    else:
        os.system('clear')
        top_lines ()
        contact_not_found()