# for loop example
# A for loop is used to iterate over items in a collection.
# Here we have a list of fruits, and we print each one.

fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print("Current fruit:", fruit)

# Example with index and value using enumerate()
print("\nFruit list with index:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
