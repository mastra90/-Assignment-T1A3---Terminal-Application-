import os
from formatting import top_lines, bot_lines, press_enter

# Add a new contact.
def add_new_contact(contacts):
    print("Please enter the following details:\n")
    name = input("Full name: ")

    if name.isspace():
        os.system('clear')
        top_lines ()
        print("\nYou cannot enter only spaces in the name field!\n") 
        bot_lines()
        press_enter()
        os.system('clear')
        top_lines()
        text = "\nADD NEW CONTACT"
        title = "\x1B[1;4m" + text + "\x1B[0m" + ":\n"
        print(title)
        add_new_contact(contacts)
    
    elif name == "":
        os.system('clear')
        top_lines ()
        print("\nYou cannot enter only spaces in the name field!\n") 
        bot_lines()
        press_enter()
        os.system('clear')
        top_lines()
        text = "\nADD NEW CONTACT"
        title = "\x1B[1;4m" + text + "\x1B[0m" + ":\n"
        print(title)
        add_new_contact(contacts)

    elif name in contacts:
            os.system('clear')  
            top_lines ()
            print("\nContact already exists.\n")
            bot_lines()
    else:
        phone_num = input("Phone number: ")
        while True:
            email = input("Email address: ")
            if " " in email:
                print("\nDo not use spaces in email addresses!")
                print("Please try again.\n")
            else:    
                contacts[name] = [phone_num, email]
                os.system('clear')
                top_lines ()
                print("\n" + name + " has been added to your contacts.\n")
                bot_lines()
                break