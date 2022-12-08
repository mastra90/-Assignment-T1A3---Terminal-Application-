# A function to add a new contact
def add_new_contact(contacts):
    name = input("Enter name and last name of contact: ")
    if name in contacts:
        print("Contact already exists")
    else:
        phone_num = input("Enter phone number: ")
        email = input("Enter email address: ")
        contacts[name] = [phone_num, email]