# View all the contacts
def view_contacts(contacts):
    for name in contacts:
        print ("Name: " + name + "\n" + "Phone: " + contacts[name][0] + "\n" + "Email: " + contacts[name][1] + "\n")