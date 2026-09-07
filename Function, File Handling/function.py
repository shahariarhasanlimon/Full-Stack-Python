# 2 types

# 1. User Defined Function --> Programmer nijer moto kore ekta function define kore. Example: def my_function(): pass

# 2. Built-in Function --> Python already provide some function. Example: print(), len(), type() etc.

# print() function is used to print the output on the console.
# input() function is used to take input from the user.
# Sum() function is used to calculate the sum of a list of numbers.

# print("Hello, World!")  # Output: Hello, World!
# user_name = input("Enter your name: ")  # Takes input from the user
# print(f"Hello, {user_name*2}!")  # Output: Hello, [User Name]!


# User Defined Function
# 1> No input, No output
def my_first_function(): # Function definition
    a = 10
    b = 20
    print(a + b)  # Output: 30

my_first_function() # Function call

# 2> Input, No return

def add_numbers(a, b): # arguments pass kore function define kora hocche
    print(a + b)  # Output: Sum of a and b

add_numbers(10, 20) # parameter pass kore function call kora hocche
add_numbers(5, 15) # Function call with different arguments

# 3> Input, Return
def multiply_numbers(a, b):
    return a * b  # Output: Product of a and b
result = multiply_numbers(5, 10) # Function call with different arguments
print(result) # Output: 50

# 4> No Input, Return
def get_greeting():
    return "Hello, World!"  # Output: Greeting message

greeting = get_greeting()
print(greeting)  # Output: Hello, World!
