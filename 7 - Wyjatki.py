def divideBy(num):
    try:
        return 100 / num
    except ZeroDivisionError:
        print('Divided by zero is forbidden!')


print(divideBy(10))
print(divideBy(24))
print(divideBy(0))
