from typing import List


def my_function():
    print("This is my function")


my_function()


def print_message(message: str):
    print(message)


print_message("Hey Now!")


def print_full_name(first_name: str, last_name: str):
    print(f"{first_name} {last_name}")


print_full_name("John", "Doe")


def print_color_red():
    color = "\033[91mThis text is red\033[0m"
    print(color)  # ANSI escape code for red text


color = "\033[92mThis text is green\033[0m"
print(color)
print_color_red()


def print_numbers(highest: int, lowest: int):
    print(f"Highest: {highest}, Lowest: {lowest}")


# Reversing the order of arguments
print_numbers(lowest=20, highest=30)


def multiply_numbers(a: int, b: int) -> int:
    return a * b


solution = multiply_numbers(5, 10)
print(f"The solution is: {solution}")


def print_list_items(items: List[int]):
    for item in items:
        print(item)


number_list = [1, 2, 3, 4, 5]
print_list_items(number_list)


def buy_item(cost: float) -> float:
    return cost + add_tax(cost)


def add_tax(cost: float) -> float:
    tax_rate = 0.06375
    return round(cost * tax_rate, 2)


final_cost = buy_item(99.99)
print(f"The final cost after tax is: {final_cost}")
