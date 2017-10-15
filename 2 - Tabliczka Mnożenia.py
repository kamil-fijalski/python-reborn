#!usr/bin/python3

print('Tabliczka mnozenia\n')

for i in range(1, 11):
    dataString = ''
    for j in range(1, 11):
        dataString = dataString + str(i * j) + '\t'
    print(dataString)
