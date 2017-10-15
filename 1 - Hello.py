# This program says "Hello" and asks for a name

print('Hello world!')
print('What is your name?')
myName = input()

print('Nice to meet you ' + myName + '!')
print('The length of your name: ' + str(int(len(myName))))

print('How old are you?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
