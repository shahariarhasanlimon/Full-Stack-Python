import os
import pathlib
# # file = open('name.txt', 'r')
# # content = file.read()
# # print(content)
# # file.close()

# with open('name.txt', 'r') as file:
#     content = file.read()
#     print(content)

# with open('name.txt', 'a') as file:
#     file.write('Hello World')
#     file.write('Hello Python')
#     file.write('Hello Django')
#     file.write('Hello Flask')
#     file.write('Hello FastAPI')
# lines = ['Hello World\n', 'Hello Python\n', 'Hello Django\n', 'Hello Flask\n', 'Hello FastAPI\n']
# with open('name.txt', 'a') as file:
#     file.writelines(lines)


if os.path.exists('name.txt'):
    print('File exists')
else:
    print('File does not exist')

    file_path = pathlib.Path('name.txt')
    if file_path.exists():
        print('File exists')
        print(os.path.abspath('name.txt'))
        print(os.path.getsize('name.txt'))

        with open('name.txt', 'r') as file:
            print(file.read(5))