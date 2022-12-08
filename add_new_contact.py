# A function to add a new contact
def add_new_contact(contacts):
    print("Please enter the following details (without spaces):\n")
    name = input("First name: ")
    last_name = input("Last name: ")
    if name and last_name in contacts:
        print("Contact already exists")
    else:
        phone_num = input("Phone number: ")
        email = input("Email address: ")
        contacts[name] = [last_name, phone_num, email]
        print("\n" + name + " " + last_name + " has been added to your contacts.")