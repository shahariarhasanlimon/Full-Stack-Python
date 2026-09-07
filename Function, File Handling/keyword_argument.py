#Keyword_Argument
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")   

greet(name="Alice", age=25)  # Output: Hello, Alice! You are 25 years old.
greet(age=30, name="Bob")    # Output: Hello, Bob! You are 30 years old.    

def greet_with_default(name, age=18):
    print(f"Hello, {name}! You are {age} years old.")
    
greet_with_default("Charlie")  # Output: Hello, Charlie! You are 18 years old.
greet_with_default("David", 25)  # Output: Hello, David! You are 25 years old.
