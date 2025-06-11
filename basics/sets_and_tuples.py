my_set = {1, 2, 3, 5, 4, 4, 5, 1, 2}
print(my_set)
my_set.add(6)  # Adding an element to the set
print(my_set)
my_set.add(0)  # Adding an element to the set
print(my_set)
my_set.remove(3)  # Removing an element by value
print(my_set)
my_set.discard(7)  # Discarding an element that may not exist
print(my_set)
my_set.pop()  # Removing an arbitrary element
print(my_set)
print(len(my_set))  # Getting the number of elements in the set
print(2 in my_set)  # Checking if an element is in the set
print(3 in my_set)  # Checking if an element is in the set
# print(my_set.union({7, 8}))  # Union with another set
# print(my_set.intersection({1, 2, 3, 4}))  # Intersection with another set
# print(my_set.difference({1, 2}))  # Difference with another set
# print(my_set.symmetric_difference({1, 2, 3}))  # Symmetric difference with another set
my_set.update([6, 7])
print(my_set)

for item in my_set:
    print(item)

my_set.clear()
print(my_set)

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(my_tuple[0])  # Accessing an element by index
print(my_tuple[1:3])  # Slicing the tuple
print(len(my_tuple))  # Getting the number of elements in the tuple
print(2 in my_tuple)  # Checking if an element is in the tuple
# Tuples are immutable, so we cannot add or remove elements
# my_tuple.append(6)  # This will raise an AttributeError
# my_tuple.remove(2)  # This will raise an AttributeError
print(my_tuple.count(2))  # Counting occurrences of an element
print(my_tuple.index(3))  # Finding the index of an element
# Tuples can be unpacked
a, b, c, d, e = my_tuple
print(a, b, c, d, e)  # Unpacked values
