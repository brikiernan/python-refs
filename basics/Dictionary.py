a_dictionary = {
    "hello": "A greeting or expression of goodwill.",
    "world": "The earth, together with all of its countries and peoples.",
    # "python": "A high-level programming language known for its readability and versatility.",
    # "dictionary": "A collection of key-value pairs, where each key is unique.",
    # "code": "A system of symbols and rules used to represent information or instructions.",
    # "function": "A block of reusable code that performs a specific task.",
    # "variable": "A named storage location in programming that can hold a value.",
    # "loop": "A programming construct that repeats a block of code multiple times.",
    # "condition": "A statement that controls the flow of execution based on whether it is true or false.",
    # "list": "An ordered collection of items that can be changed or modified.",
    # "set": "An unordered collection of unique items.",
    # "tuple": "An ordered collection of items that cannot be changed after creation.",
    # "class": "A blueprint for creating objects in object-oriented programming.",
    # "object": "An instance of a class that contains data and methods.",
    # "module": "A file containing Python code that can be imported and used in other programs.",
    # "package": "A collection of modules organized in a directory hierarchy.",
    # "exception": "An error that occurs during the execution of a program, disrupting its normal flow.",
    # "syntax": "The set of rules that defines the structure of a programming language.",
    # "algorithm": "A step-by-step procedure for solving a problem or performing a task.",
    # "debugging": "The process of finding and fixing errors in code.",
    # "comment": "A note in the code that is ignored by the interpreter, used for documentation.",
    # "syntax_error": "An error that occurs when the code does not conform to the syntax rules of the programming language.",
    # "runtime_error": "An error that occurs while the program is running, often due to invalid operations or conditions.",
    # "data_type": "A classification that specifies the type of data a variable can hold, such as integer, string, or boolean.",
    # "inheritance": "A mechanism in object-oriented programming where a class can inherit properties and methods from another class.",
    # "encapsulation": "The bundling of data and methods that operate on that data within a single unit, typically a class.",
    # "polymorphism": "The ability of different classes to be treated as instances of the same class through a common interface.",
    # "recursion": "A programming technique where a function calls itself to solve a problem.",
    # "iteration": "The process of repeating a set of instructions a certain number of times or until a condition is met.",
    # "API": "Application Programming Interface, a set of rules and protocols for building and interacting with software applications.",
    # "framework": "A collection of libraries and tools that provide a structure for building applications.",
}

a_dictionary["new_key"] = "This is a new key-value pair."

# print(a_dictionary)
# print("-------")
# print("Keys:", a_dictionary.keys())
# print("-------")
# print("Values:", a_dictionary.values())
# print("-------")
# print("Items:", a_dictionary.items())
# print(a_dictionary.get("hello", "Key not found"))
# print(a_dictionary["hello"])  # This will raise a KeyError if "hello" does not exist
# a_dictionary.pop("hello")  # Remove the key "hello" from the dictionary
# print(a_dictionary)

# for key, value in a_dictionary.items():
#     print(f"{key}: {value}")

# for item in a_dictionary:
#     print(item)

a_dictionary2 = a_dictionary.copy()  # Create a copy of the dictionary
a_dictionary2["new_key"] = "This is a new key-value pair."
a_dictionary2.pop("world")  # Remove the key "world" from the copied dictionary
print("Copied Dictionary:", a_dictionary2)
print(a_dictionary)
