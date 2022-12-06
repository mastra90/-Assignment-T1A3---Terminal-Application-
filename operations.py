

def print_list_of_contacts(phonebook):
    for x in phonebook:
        print(x)

 
def add_contact(phonebook, Name, Phone, Email):
    new_contact = {"Name ": Name, "Phone ": Phone, "Email ": Email}
    phonebook.append(new_contact)

    with open('contacts.txt', 'a') as f:
        for new_contact in new_contact.items():
            f.write ('%s:%s\n' % (new_contact))














    # def add_contact(phonebook, full_name, phone, email):
    # new_contact = {"Name": full_name, "Number": phone, "Email": email}
    # phonebook.append(new_contact)