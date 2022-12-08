# A function to search for a particular contact
def search_contact(contacts):
    name = input("Enter name of contact to search (cap sensitive): ")
    if name in contacts:
        print(name + ": " + contacts[name][0] + ", " + contacts[name][1])
    else:
        print("\nContact not found")