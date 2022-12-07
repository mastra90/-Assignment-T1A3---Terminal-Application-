def all_contacts():

    contacts = {
        "Name" : " Riley",
        "Phone": " 0412 345 678",
        "Email": " riley@example.com\n",
        }
    
    # contact_list = [contacts]

    with open('contacts.txt', 'w') as f:
        for contacts in contacts.items():
            f.write ('%s:%s\n' % (contacts))

    # return contact_list

all_contacts()
    
    








