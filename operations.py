def print_list_of_contacts(phonebook):
    for x in phonebook:
        print(x)

def add_contact(phonebook, name, number, email):
    new_contact = {"name": name, "phone": number, "email": email}
    phonebook.append(new_contact)