

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
        print("\n=====Add Contact=====")
        name = input("Name: ")
        phone = input("Number: ")
        entry[name] = phone
        print(f"{name} is added.")
     


    