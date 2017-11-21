print('Type number in decimal system: ')
num = int(input())

num_temp = num
end_string = ''

while num_temp > 1:
    next_num = num_temp % 2
    end_string = end_string + str(next_num)
    num_temp = int((num_temp-next_num)/2)

if num_temp == 1:
    end_string = end_string + '1'

print('Your number: ' + str(num))
print('In binary system it is: ' + end_string[::-1])

