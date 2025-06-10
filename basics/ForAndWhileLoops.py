numbers = [1, 2, 3, 4, 5]
sum_of_numbers = 0
# Using a for loop to iterate through the list
for number in numbers:
    sum_of_numbers += number
print("End of for loop where the sum of numbers is", sum_of_numbers)


weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# Using a for loop to iterate through the list
for day in weekdays:
    print(f"Happy {day}!")


# for x in range(100, 120):
#     print(x)

i = 0
# Using a while loop to iterate until i is less than 5
while i < 5:
    i += 1
    if i == 3:
        continue
    print("i is", i)
    # Else will not execute if the loop is broken
    if i == 4:
        break
else:
    print("End of while loop where i is", i)
