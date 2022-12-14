import os
from formatting import top_lines, contact_not_found

# Delete a contact.
def delete_contact(contacts):
    name = input("Full name of contact to delete (case sensitive): ")

    if name in contacts:
        del contacts[name]
        print("\n" + name + " has been removed from your contacts.\n")
        
    else:
        os.system('clear')
        top_lines ()
        contact_not_found()
