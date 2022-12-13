import os
from formatting import top_lines

# Delete a contact
def delete_contact(contacts):
    name = input("Name of contact to delete (case sensitive): ")

    if name in contacts:
        del contacts[name]
        print("\n" + name + " has been removed from your contacts.\n")
        
    else:
        os.system('clear')
        top_lines ()
        print("\nContact not found.\n")
        print("Please note: The search is case sensitive.\n")
