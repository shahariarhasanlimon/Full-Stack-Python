# errors vs exceptions

# compile time error --> syntax error
# Run time error --> exception
#Errors are detected by the compiler, while exceptions are detected by the interpreter at runtime.
# exception --> Run time Error
#           --> IndexError, KeyError, ValueError, ZeroDivisionError, FileNotFoundError, TypeError, NameError

try:#je code a exception thakte pare, sei code a try block use kora hoy

    with open('name.txt', 'r') as file:
        print(file.read())
except FileNotFoundError as e:#je exception thakte pare, sei exception ke handle kora hoy
    print('File not found')
    print(e)