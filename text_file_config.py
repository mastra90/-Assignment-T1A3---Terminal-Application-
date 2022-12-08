# A function to read the contacts from the text file
def read_contacts():
    contacts = {}
    file = open("contacts.txt", "r")
    for line in file.readlines():
        contact_details = line.split()
        name = contact_details[0]
        last_name = phone_num = contact_details[1]
        phone_num = contact_details[2]
        email = contact_details[3].strip()
        contacts[name] = [last_name, phone_num, email]
    file.close()
    return contacts

    # A function to save changes to the contact book text file
def save_contacts(contacts):
    file = open("contacts.txt", "w")
    for name in contacts:
        last_name = contacts[name][0]
        phone_num = contacts[name][1]
        email = contacts[name][2]
        file.write(name + " " + last_name + " " + phone_num + " " + email + "\n")
    file.close()