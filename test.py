
def readfile():
    file = open('contacts.txt', 'r')
    read = file.readlines()
    modified = []

    for line in read:
        if line[-1] =='\n':
            modified.append(line[:-1])
        else:
            modified.append(line)

    print(modified)



# with open('contacts.txt', 'r') as f:
#         for contact1 in contact1.items():
#             f.write ('%s:%s\n' % (contact1))