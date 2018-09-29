# Let's begin this madness
print("Hello Python!")

int1 = 10 + 10j
int2 = 20 + 5j

int3 = int1 * int2
print(int3)

print(5 / 3)   # floating
print(5 // 3)  # integer

str1 = "Apple"

print(str1[0])
print(str(len(str1)))
print(str1.replace("p", "x") + " " + str1.upper() + " " + str1.lower() + " " + str1.swapcase())
# method "find" works like "instr" in SQL

# tuples are immutable and they can be nesting
tuple1 = ("A", "B", 1, 2, 3.14, 2.73)
print(type(tuple1))
print(tuple1[2])
tupleStr = tuple1[0:2]
print(tupleStr)

tupleNest = (("Jazz", "Rock"), "Dance", ("Metal", "Folk"))
print(tupleNest[0][1])

# list are mutable -> square brackets / list can nested other lists and tuples
list1 = [5, 1, 3, 10, 8]
print(sorted(list1))
list1.extend([7, 12])  # extend adds two elements -> APPEND adds one element (list with elements 7, 12)
print(list1)
list1[0] = 100  # are mutable
print(list1)
del(list1[2])
print(list1)

str2 = "Quick brown fox jumps over the lazy dog"
listSplit = str2.split()
print(listSplit)
listSplit2 = listSplit[:]  # clone existing list

# sets / collection -> unique element => curly brackets
set1 = set(list1)
print(set1)
set1.add(256)
set1.add(512)
print(set1)
set1.remove(100)
print(set1)

check = 512 in set1  # checking if element exists in given set
print(check)

set88 = {2, 4, 5, 7, 9}
set99 = {1, 3, 5, 8, 9}
print(set88 & set99)  # intersect of the two sets / or "intersection" method
print(set88.union(set99))
print(set88.difference(set99))

# dictionaries -> key: value
# keys are immutable and unique, values can be mutable and duplicates
dict1 = {1: "one", 2: "two", 3: "three"}
print(dict1)
print(dict1[3])
dict1[1000] = "thousand"  # adding new element
print(dict1)
del(dict1[2])  # delete element
print(dict1)
print(2 in dict1)  # checking if element exists in dict
print(dict1.keys())
print(dict1.values())

age = 25
if age < 25:
    print("less")
elif age > 25:
    print("more")
else:
    print("equal")

squares = {"red", "blue", "yellow", "black", "purple"}
for i in squares:
    print(i)

str88 = ""
for r in range(10, 15):
    str88 = str88 + str(r) + " "
print(str88)

str99 = ""
while age < 30:
    str99 = str99 + "bu" + " "
    age += 1
print(str99 + "BUM!")


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


nn = input("Give me a word... ")
print(factorial(len(nn)))
