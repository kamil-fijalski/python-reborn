lists = [1, 2, 3, 4]
print(lists[1])

lista = []
for i in range(101):
    lista.append(i / 2 + 1)

print(lista[10])
print(lista.index(4))

lista.insert(10, 'dziesiec')
print(lista[10])
lista.remove('dziesiec')
print(lista[10])
print('')

listing = [5, 1, 8, 10, 4, 15, 100]
print(listing)
listing.sort()
print(listing)

imie = 'Kamil'
for i in imie:
    print('**' + i + '**')
