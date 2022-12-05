def main_menu():
    print ("1. View Contacts")
    print ("2. Add Contact")
    print ("3. Delete Contact")
    print ("4. Quit")
    i = input("Select your option (1-4): ")
    return i

reponse = ""

while reponse != "4":
    reponse = main_menu()
    if reponse == "1":
        print("Prints list of all contacts")
    elif reponse == "2":
        print("Asks for contact name, phone number and email address")
    elif reponse == "3":
        print("Displays list of contacts and asks which one to delete")
    elif reponse == "4":
        continue
    else:
        print("Input not valid")
    input("Please press 'Enter' to proceed")


print("You have quit the application. Thanks!") 
