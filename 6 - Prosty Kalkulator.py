#!usr/bin/python3

print('Podaj pierwsza liczbe:')
firstNum = int(input())
print('Podaj druga liczbe:')
secondNum = int(input())
print('Jakie dzialanie chcesz wykonac?')
print('1 - Dodawanie, 2 - Odejmowanie, 3 - Mnozenie')
print('4 - Dzielenie, 5 - Potegowanie, 6 - Modulo')
action = int(input())

if action == 1:
    print('Wynik: ' + str(firstNum + secondNum))
elif action == 2:
    print('Wynik: ' + str(firstNum - secondNum))
elif action == 3:
    print('Wynik: ' + str(firstNum * secondNum))
elif action == 4:
    print('Wynik: ' + str(firstNum / secondNum))
elif action == 5:
    print('Wynik: ' + str(firstNum ** secondNum))
elif action == 6:
    print('Wynik: ' + str(firstNum % secondNum))
else:
    print('Niepoprawny wybor!')
