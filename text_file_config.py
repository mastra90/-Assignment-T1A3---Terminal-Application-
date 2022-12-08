# A function to read the contacts from the text file
def read_contacts():
    contacts = {}
    file = open("contacts.txt", "r")
    for line in file.readlines():
        contact_details = line.split(',')
        name = contact_details[0]
        phone_num = contact_details[1]
        email = contact_details[2].strip()
        contacts[name] = [phone_num, email]
    file.close()
    return contacts

    # A function to save changes to the contact book text file
def save_contacts(contacts):
    file = open("contacts.txt", "w")
    for name in contacts:
        phone_num = contacts[name][0]
        email = contacts[name][1]
        file.write(name + "          " + phone_num + "          " + email + "\n")
    file.close()