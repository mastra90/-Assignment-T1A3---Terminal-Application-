import os
from formatting import top_lines, bot_lines

# Add a new contact.
def add_new_contact(contacts):
    print("Please enter the following details:\n")
    name = input("Full name: ")

    if name == " ":
        # os.system('clear')
        os.system('cls')
        top_lines ()
        print("\nDo not enter a space for name!\n") 
        bot_lines()
    elif name in contacts:
            # os.system('clear')
            os.system('cls')    
            top_lines ()
            print("\nContact already exists.\n")
            bot_lines()
    else:
        phone_num = input("Phone number: ")
        email = input("Email address: ")
        while True:
            if " " in email:
                # os.system('clear')
                os.system('cls')
                top_lines ()
                print("\nDo not use spaces in email addresses!\n")
                bot_lines()
                break
            else:    
                contacts[name] = [phone_num, email]
                print("\n" + name + " has been added to your contacts.\n")
                bot_lines()
                break