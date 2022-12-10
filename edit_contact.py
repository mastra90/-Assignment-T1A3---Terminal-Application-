# A function to edit an existing contact
def edit_contact(contacts):
    name = input("Enter name of contact to edit: ")
    if name in contacts:
        phone_num = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        contacts[name] = [phone_num, email]
    else:
        print("Contact not found")