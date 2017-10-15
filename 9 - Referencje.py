list1 = [0, 1, 2, 3, 4, 5]
print('List1: ' + str(list1))

list2 = list1
list2[0] = 100

print('.')
print('List1: ' + str(list1))
print('List2: ' + str(list2))
print('.')
print('Start "copy" module.')

list3 = [100, 101, 102, 103, 104, 105]
print('List3: ' + str(list3))
list4 = list3.copy()
list4[0] = 200

print('.')
print('List3: ' + str(list3))
print('List4: ' + str(list4))

print('.')
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
print(str(grid))
print('.')
for i in range(6):
    for j in range(9):
        print(str(grid[j][i]) + '\t', end='')
    print('\n')
