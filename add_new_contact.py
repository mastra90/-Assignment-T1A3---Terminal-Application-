# A function to add a new contact
def add_new_contact(contacts):
    print("Please enter the following details:")
    print ("NOTE: Do not use spaces! Please use an underscore (\"_\") instead.\n")
    name = input("Full name: ")
    if name in contacts:
        print("Contact already exists")
    else:
        phone_num = input("Phone number: ")
        email = input("Email address: ")
        contacts[name] = [phone_num, email]
        print("\n" + name + " " + " has been added to your contacts.")