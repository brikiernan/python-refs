first_name = "John"
print(f"Hello, {first_name}!")  # Using f-string for formatting
print("Hello, {}!".format(first_name))
print("Hello, {0} {1}!".format(first_name, "Doe"))
print("Hello, {first} {last}!".format(first="John", last="Doe"))
print("Hello, {0} {1}!".format("John", "Doe"))

sentence = "The quick {} fox jumps over the lazy dog."
print(sentence.format("brown"))
print("The quick {color} fox jumps over the lazy dog.".format(color="red"))
