import random


def testFunc(name):
    print('Hello ' + name + '!')


def getRandomNum(num):
    if num >= 0 and num < 4:
        return 'Not bad...'
    elif num >= 4 and num < 7:
        return 'Pretty cool!'
    elif num >= 7:
        return 'Great!'


r = random.randint(0, 10)
i = getRandomNum(r)
testFunc('Kamil')

print('Twoj szczesliwy numer na dzis: ' + str(r))
print(i)
