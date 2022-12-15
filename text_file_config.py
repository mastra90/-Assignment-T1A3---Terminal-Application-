# Read the contacts.txt file
def read_contacts():
    contacts = {}
    file = open("contacts.txt", "r")

    for line in file.readlines():
        contact_details = line.split('|')
        name = ' '.join(contact_details[0:-2])
        phone_num = contact_details[-2]
        email = contact_details[-1]
        contacts[name] = [phone_num, email]
    file.close()
    return contacts

# Save changes to the contacts.txt file
def save_contacts(contacts):
    file = open("contacts.txt", "w")

    for name in contacts:
        phone_num = contacts[name][0]
        email = contacts[name][1]
        file.write(name + "|" + phone_num + "|" + email + "\n")
    file.close()