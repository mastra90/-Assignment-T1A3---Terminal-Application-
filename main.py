

def main_menu():
    print ("\nHello! Welcome to your Contact Book.\n")
    print ("1. View Contacts")
    print ("2. Add Contact")
    print ("3. Delete Contact")
    print ("4. Search")
    print ("5. Quit\n")

entry = {}
user_input = 0
main_menu()
while user_input != "5":

    user_input = (input("Type in a number (1-5): "))

    if user_input == "1":
        print("\n======All contacts======\n")
        for i in entry.keys():
            print("Name: ", i, "\tNumber:", entry[i])
        print()
    elif user_input == "2":
        print("\n======Add Contact======\n")
        name = input("Full name: ")
        phone = input("Contact number: ")
        entry[name] = phone
        print(f"\n{name} has been added.")
        input("\nPress 'Enter' to continue\n")

    elif user_input == "3":
        print("\n======Lookup Number======\n")
        name = input("Name: ")
        if name in entry:
            print(f"\n{name}'s number is:",entry[name])
            print()
        else:
            print ()
            print(name, "was not found")
            print ()

    elif user_input == "4":
        print("\n======Delete Contact======\n")
        name = input("Name of contact (case sensitive): ")
        if name in entry:
            del entry[name]
            print(f"\n{name} has been removed.")
            input("\nPress 'Enter' to continue\n") 
        else:
            print()
            print(name, "was not found\n")
            input("Press 'Enter' to continue\n")

    elif user_input == "5":
        print("\nYou have quit the application. Thanks!\n") 

    else:
        print("Invalid entry")
        input("Press 'Enter' to continue\n")