import os
from formatting import top_lines, contact_not_found

# Search for a contact
def search_contact(contacts):
    name = input("Full name of contact to search (case sensitive): ")

    if name in contacts:
        os.system('clear')
        top_lines()
        text = "\nSEARCH RESULTS"
        title = "\x1B[1;4m" + text + "\x1B[0m" + ":\n"
        print(title)
        print("Name: " + name + "\n" + "Phone: " + contacts[name][0] + "\n" + "Email: " + contacts[name][1] + "\n")
        
    else:
        os.system('clear')
        top_lines ()
        contact_not_found()