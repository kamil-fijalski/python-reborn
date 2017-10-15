import random

total = 0
for i in range(101):  # range zawsze jest o 1 mniejszy
    total = total + i
print(total)
print('')

for i in range(0, 10, 2):  # start, stop, krok
    print(i)
print('')

for i in range(5):
    print(random.randint(0, 10))  # zakres losowosci (0, 10 wlacznie)
