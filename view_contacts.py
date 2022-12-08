# A function to view all the contacts
def view_contacts(contacts):
    for name in contacts:
        print (name + " " + contacts[name][0] + "____" + contacts[name][1] + "____" + contacts[name][2])