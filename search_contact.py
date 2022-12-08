import os
from formatting import top_lines, bot_lines
# A function to search for a particular contact
def search_contact(contacts):
    name = input("Enter name of contact to search (cap sensitive): ")
    if name in contacts:
        os.system('cls')
        top_lines()
        print(name + "'s contact info:\n")
        print(name + " " + contacts[name][0] + ": \t" + contacts[name][1] + "\t" + contacts[name][2])
    else:
        print("\nContact not found")