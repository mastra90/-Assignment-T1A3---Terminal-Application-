import os
from formatting import top_lines


# A function to search for a particular contact
def search_contact(contacts):
    name = input("Enter name of contact to search (cap sensitive): ")
    if name in contacts:
        os.system('cls')
        top_lines()
        print("\n" + name + "'s contact info:\n")
        print(contacts[name][0] + "\n" + contacts[name][1] + "\n")
    else:
        os.system('cls')
        top_lines ()
        print("\nContact not found.\n")
        print("You may need to include an underscore (\"_\") in your search.\n")