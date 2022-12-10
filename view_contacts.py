# A function to view all the contacts
def view_contacts(contacts):
    for name in contacts:
        print (name + "\n" + contacts[name][0] + "\n" + contacts[name][1] + "\n")