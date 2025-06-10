first_name = input("Enter your first name: ")
print(f"Hello, {first_name}!")  # Using f-string for formatting
print("Hello, {}!".format(first_name))
print("Hello, {0} {1}!".format(first_name, "Doe"))
print("Hello, {first} {last}!".format(first=first_name, last="Doe"))

days = input("Enter the number of days until your birthday: ")

print(f"Hey {first_name}, your birthday is in {days} days!")
