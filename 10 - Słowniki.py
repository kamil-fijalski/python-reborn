birthdays = {'Kamil': '14 Kwi', 'Pati': '24 Lip'}

while name != '':
    print('Enter a name: ')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have information about ' + name)
        print('Could you tell me when is your birthday? ')
        bday = input()
        birthdays[name] = bday
        print('Birthday database was updated')
