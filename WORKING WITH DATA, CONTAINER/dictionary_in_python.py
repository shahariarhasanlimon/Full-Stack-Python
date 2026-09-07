#Dictionary in Python
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print(my_dict)

# {}
# Key Value pairs
# indexing er sujog nai
# key gula unique hote hobe

a = {"name": "Alice", "age": 30, "city": "New York"}
print(a["name"])  # Output: Alice
print(a["age"])   # Output: 30
print(a["city"])  # Output: New York

for key in a:
    print(key, ":", a[key])
    