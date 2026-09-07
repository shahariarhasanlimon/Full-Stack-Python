# {}
# Set
# Unordered collection of unique elements
# immutable, meaning you cannot change the elements once they are added
# No Duplicates: Sets automatically remove duplicate elements.

my_set = {1, 2, 3, 4, 5, 5, 4, 3}  # Duplicates will be removed
print(my_set)

set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a.union(set_b))  # Output: {1, 2, 3, 4, 5}
print(set_a.intersection(set_b))  # Output: {3}
print(set_a.difference(set_b))  # Output: {1, 2}
print(set_b.difference(set_a))  # Output: {4, 5}
