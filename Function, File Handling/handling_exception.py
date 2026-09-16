# errors vs exceptions

# compile time error --> syntax error
# Run time error --> exception
# Errors are detected by the compiler, while exceptions are detected by the interpreter at runtime.
# exception --> Run time Error
#           --> IndexError, KeyError, ValueError, ZeroDivisionError, FileNotFoundError, TypeError, NameError

# try block: code that may raise an exception
try:
    x = int(input('Enter a number: '))
    print(10 / x)
except ValueError as e:
    print('Invalid input! Please enter a valid integer.')
    print(e)
except ZeroDivisionError as e:
    print('Cannot divide by zero.')
    print(e)
finally:
    print('This block always runs.')

# file handling example
try:
    with open('name.txt', 'r') as file:
        print(file.read())
except FileNotFoundError as e:
    print('File not found.')
    print(e)
