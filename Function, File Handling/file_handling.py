# file = open('name.txt', 'r')
# content = file.read()
# print(content)
# file.close()

with open('name.txt', 'r') as file:
    content = file.read()
    print(content)