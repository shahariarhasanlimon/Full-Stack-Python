import functools
#anonymus Function --> Unnamed Function
#lambda arguments: expression

square = lambda x: x ** 2
print(square(5))  # Output: 25

# More examples
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8

is_even = lambda x: x % 2 == 0
print(is_even(4))  # Output: True
print(is_even(3))  # Output: False  

students = [
    {"name": "Alice", "age": 20},   
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 30}  
]
sorted_students = sorted(students, key=lambda student: student["age"])  
print(sorted_students)  # Output: [{'name': 'Alice', 'age': 20}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 30}]    



# map(), filter(), Reduce()

#map 
nums = [1, 2, 3, 4]

squared_nums = list(map(lambda x: x ** 2, nums))
print(squared_nums)  # Output: [1, 4, 9, 16]

#filter
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)  # Output: [2, 4]

#reduce
sum = functools.reduce(lambda x, y: x + y, nums)
print(sum)  # Output: 10


