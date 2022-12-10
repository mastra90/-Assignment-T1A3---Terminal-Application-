import os
from formatting import top_lines


# A function to edit an existing contact
def edit_contact(contacts):
    name = input("Enter name of contact to edit (cap sensitive): ")
    if name in contacts:
        phone_num = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        contacts[name] = [phone_num, email]
        print("\n" + name + "'s information has been updated.\n")
    else:
        os.system('cls')
        top_lines ()
        print("\nContact not found.\n")
        print("You may need to include an underscore (\"_\") in your search.\n")