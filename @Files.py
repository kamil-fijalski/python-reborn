# Lesson about file handling
# "w" for writing, "r" for reading, "a" for appending

File1 = open("C:/Users/Kamil/PycharmProjects/python-reborn/QQQ.txt", "r")

print("File name: " + File1.name)

File1.close()

# better way
with open("QQQ.txt", "r") as File2:
    # file_content = File2.read()
    # print(file_content)
    first_line = File2.readline()
    print(first_line)
    second_line = File2.readline()
    print(second_line)

    much_characters = File2.readlines(20)
    print(much_characters)

print(first_line[5])
print(much_characters[0])

with open("QQZ.txt", "w") as File88:
    File88.write("Hello Python!\n")
    File88.write("Welcome to the Machine.\n")

lines = ["Xbox\n", "Play Station\n", "Switch\n"]
with open("QQR.txt", "w") as File99:
    for line in lines:
        File99.write(line)

