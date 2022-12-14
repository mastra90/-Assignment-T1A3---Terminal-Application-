# Read the contacts.txt file
def read_contacts():
    contacts = {}

    file = open("contacts.txt", "r")
    for line in file:
        contact_details = line.strip().split("|")
        name = contact_details[0]
        phone_num = contact_details[1]
        email = contact_details[2]
        contacts[name] = [phone_num, email]
    file.close()
    return contacts

# Save changes to the contacts.txt file
def save_contacts(contacts):
    file = open("contacts.txt", "w")
    for name in contacts:
        phone_num = contacts[name][0]
        email = contacts[name][1]
        file.writelines(name + "|" + phone_num + "|" + email + "\n")
    file.close()