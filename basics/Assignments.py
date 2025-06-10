from typing import Dict, Union

# You have $50
# You buy an item that is $15
# With a tax of 3%
# print how much you have left

change = 50 - (15 + (15 * 0.03))
print("You have $", change, "left after buying the item with tax.")


# Ask use how many days until their birthday
# and print the number of weeks until

days_until_birthday = int(input("How many days until your birthday? "))
weeks_until_birthday = days_until_birthday // 7
print(f"There are {weeks_until_birthday} weeks until your birthday.")

print(
    f"There are " + str(round(days_until_birthday / 7, 2)),
    f" weeks until your birthday.",
)

# Create a list of 5 animals,
# delete the animal at index 3,
# append a new animal,
# delete the animal at the beginning of the list,
# print all the animals,
# print the first thee animals

animals = ["Dog", "Cat", "Elephant", "Lion", "Tiger"]
del animals[3]  # Delete the animal at index 3 (Lion)
animals.append("Giraffe")  # Append a new animal (Giraffe)
animals.pop(0)  # Delete the animal at the beginning of the list (Dog)
print("All animals:", animals)  # Print all the animals
for animal in animals:
    print(animal)  # Print each animal in the list
print("First three animals:", animals[:3])  # Print the first three animals


# Create a variable called grade holding an integer between 0 and 100.
# Code if, elif, else statements to print the letter grade of the number grade variable.
grade = int(input("Enter your grade (0-100): "))
if grade > 100:
    print("Your grade cannot be higher than 100.")
elif grade >= 90:
    print("Your letter grade is A.")
elif grade >= 80:
    print("Your letter grade is B.")
elif grade >= 70:
    print("Your letter grade is C.")
elif grade >= 60:
    print("Your letter grade is D.")
elif grade >= 0:
    print("Your letter grade is F.")
else:
    print("Your grade cannot be less than 0.")


# Create a variable create weekdays and assign it a list of the days of the week.
# Create a while loop that prints all elements in the list 3 times.
# When printing the elements, use a for loop to print the weekday.
# However, if the weekday in the for loop is Monday, skip it by continuing.
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
count = 0
while count < 3:
    print("All the weekdays", weekdays)
    for index, day in enumerate(weekdays):
        if day == "Monday":
            print("--------")
            continue  # Skip Monday
        print(f"{day} is the {index + 1} day of the week.")
    count += 1  # Increment the count to avoid infinite loop
# Print a message after the while loop ends
print("Finished printing weekdays 3 times, skipping Monday.")


# Based on the dictionary:
# my_vehicle = {
#     "model": "Ford",
#     "make": "Explorer",
#     "year": 2018,
#     "mileage": 40000
# }
# - Create a for loop to print all keys and values
# - Create a new variable vehicle2, which is a copy of my_vehicle
# - Add a new key 'number_of_tires' to the vehicle2 variable that is equal to 4
# - Delete the mileage key and value from vehicle2
# - Print just the keys from vehicle2
my_vehicle: Dict[str, Union[str, int]] = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000,
}
# Print all keys and values
for key, value in my_vehicle.items():
    print(f"{key}: {value}")
# Create a copy of my_vehicle
vehicle2 = my_vehicle.copy()
# Add a new key 'number_of_tires' to vehicle2
vehicle2["number_of_tires"] = 4
# Delete the mileage key and value from vehicle2
del vehicle2["mileage"]
# Print just the keys from vehicle2
print("Keys in vehicle2:", vehicle2.keys())


# - Create a function that takes in 3 parameters(firstname, lastname, age) and
# returns a dictionary based on those values
def create_person_dict(first: str, last: str, age: int) -> Dict[str, Union[str, int]]:
    return {"first": first, "last": last, "age": age}


print(create_person_dict("John", "Doe", 30))
print(create_person_dict(last="Doe", first="John", age=30))
