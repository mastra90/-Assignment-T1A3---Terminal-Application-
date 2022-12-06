


def entire_contacts():

    contact1 = {
        "Name" : " Riley",
        "Phone": " 0412 345 678",
        "Email": " riley@example.com"
        }
    contact_list = [contact1]

    with open('contacts.txt', 'w') as f:
        for contact1 in contact1.items():
            f.write ('%s:%s\n' % (contact1))
            
    return contact_list




   






   






# def entire_contacts():
#     contact1 = {
#         "name" : "Riley",
#         "phone": "0412 345 678",
#         "email": "riley@example.com"
#         }

#     contact2 = {
#         "name" : "Kara",
#         "phone": "0412 345 678",
#         "email": "kara@example.com"
#         }

#     contact3 = {
#         "name" : "Luke",
#         "phone": "0412 345 678",
#         "email": "luke@example.com"
#         }

#     contact4 = {
#         "name" : "Ash",
#         "phone": "0412 345 678",
#         "email": "ash@example.com"
#         }