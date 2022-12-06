from operations import print_list_of_contacts, add_contact
from contacts_list import entire_contacts


list_of_contacts = entire_contacts()

def main_menu():
    print ("1. View Contacts")
    print ("2. Add Contact")
    print ("3. Delete Contact")
    print ("4. Quit")
    i = input("Select your option (1-4): ")
    return i

def add_new_contact():
    name = input("Whats the name of the new contact? \n")
    number = input("Whats the new contacts number? \n")
    email = input("Whats the new contacts email address? \n")

    add_contact(list_of_contacts, name, number, email)
    print(f"{name} will be added to your phonebook")

response = ""

while response != "4":
    response = main_menu()
    if response == "1":
        print_list_of_contacts(list_of_contacts)
    elif response == "2":
        add_new_contact()
    elif response == "3":
        print("Displays list of contacts and asks which one to delete")
    elif response == "4":
        continue
    else:
        print("Input not valid")
    input("Please press 'Enter' to proceed")


print("You have quit the application. Thanks!") 
