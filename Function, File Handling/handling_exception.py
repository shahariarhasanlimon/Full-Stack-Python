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


def check_even_odd(num):
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

    def check_file(file_path):
        try:
            with open(file_path, 'r') as file:
                print(file.read())
        except FileNotFoundError as e:
            print('File not found.')
            print(e)

            # manually raise an exception
            def divide_numbers(a, b):
                if b == 0:
                    raise ValueError('Cannot divide by zero.')
                return a / b

            #custom error class
            class CustomError(Exception):
                pass

            #custom error handling
            try:
                check_file('non_existent_file.txt')
            except CustomError as e:
                print('Custom error occurred.')
                print(e)