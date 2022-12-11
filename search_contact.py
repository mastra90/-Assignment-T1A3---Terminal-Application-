import os
from formatting import top_lines

# Search for a contact
def search_contact(contacts):
    name = input("Enter name of contact to search (case sensitive): ")

    if name in contacts:
        os.system('cls')
        top_lines()
        print("\n" + name + "'s contact info:\n")
        print(contacts[name][0] + "\n" + contacts[name][1] + "\n")
        
    else:
        os.system('cls')
        top_lines ()
        print("\nContact not found.\n")
        print("Please note: The search is case sensitive.\n")