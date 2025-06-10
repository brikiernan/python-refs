like_coffee = True
like_tea = False

favorite_food = "Pizza"
favorite_number = 42
print(f"Do you like coffee? {like_coffee}")
print(type(like_coffee))
print(f"Do you like tea? {like_tea}")
print(type(like_tea))
print(f"My favorite number is {favorite_number}.")
print(type(favorite_number))
print(f"My favorite food is {favorite_food}.")
print(type(favorite_food))

# Comparison Operators
print(1 == 2)  # False
print(1 != 2)  # True
print(1 < 2)  # True
print(1 > 2)  # False
print(1 <= 2)  # True
print(1 >= 2)  # False

# Logical Operators
print(1 > 3 and 5 < 7)  # False
print(1 > 3 or 5 < 7)  # True
print(not (1 > 3))  # True
print(not (1 == 1))  # False
