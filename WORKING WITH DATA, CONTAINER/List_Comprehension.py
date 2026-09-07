#List Comprehension
a = [1, 2, 3, 4, 5]
# Using list comprehension to create a new list with squares of the elements    
squared = [x**2 for x in a]
print(squared)  # Output: [1, 4, 9, 16, 25] 
 #normal way
squared_normal = [] 
for x in a:
    squared_normal.append(x**2)     
print(squared_normal)  # Output: [1, 4, 9, 16, 25]
 