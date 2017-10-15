import random

continues = 'T'

print('Play a game... Guess my secret number.')

while continues == 'T' or continues == 't' or continues == 'Y' or continues == 'y':
    secretNum = random.randint(0, 10)
    print('How do you think... What number did I choose?')
    try:
        ans = int(input())
    except ValueError:
        print('Unappropriated value!')
        break

    while int(ans) != secretNum:
        if int(ans) > secretNum:
            print('So close! Your number is too high!')
        else:
            print('So close! Your number is too low!')
        print('Try again!')
        try:
            ans = int(input())
        except ValueError:
            print('Unappropriated value')
            break

    if int(ans) == secretNum:
        print('Congratulations! Secret number was: ' + str(secretNum) + '.')
    print('Would you like play once again? [T/N]')
continues = input()
