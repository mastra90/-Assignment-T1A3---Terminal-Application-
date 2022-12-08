# A function to view all the contacts
def view_contacts(contacts):
    for name in contacts:
        print(name + ": \t\t" + contacts[name][0] + "\t\t" + contacts[name][1])