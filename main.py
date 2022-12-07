from view_contacts import view_contacts
from contacts_list import all_contacts



def main_menu():
    print ("\nHello! Welcome to your Contact Book.\n")
    print ("1. View Contacts")
    print ("2. Add Contact")
    print ("3. Delete Contact")
    print ("4. Quit\n")
    i = input("Please select your option (1-4): ")
    return i



def add_new_contact():
    print ("\n=========New Contact Entry=========")
    print ("Please enter the following details:")
    name = input("\nFull name: ")
    phone = input("Contact number: ")
    email = input("Email address: ")
    
    all_contacts ()

    print ("\nThe following entry has been added to your Contact Book:\n")
    print(f"Name:     {name}")
    print(f"Phone:    {phone}")
    print(f"Email:    {email}\n")

    

response = ""

while response != "4":
    response = main_menu()
    if response == "1":
        view_contacts()
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






