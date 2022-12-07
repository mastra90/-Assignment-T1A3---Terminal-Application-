
def view_contacts():
    file = open('contacts.txt', 'r')
    read = file.read()
    file.close
    print(read)