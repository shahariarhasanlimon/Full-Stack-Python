#Dictionary Comprehension
nums = list(range(1, 6))
# Using dictionary comprehension to create a dictionary with squares of the numbers 
result = {x: x**2 for x in nums}
print(result)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
result = {x: x**2 for x in nums if x % 2 == 0}  # Only even numbers
print(result)  # Output: {2: 4, 4: 16}
result = {x: x**2 for x in nums if x % 2 != 0}  # Only odd numbers
print(result)  # Output: {1: 1, 3: 9, 5: 25}
