# String declaration and printing

name = "Alice"
print(name)

# String concatenation

greeting = "Hello"
name = "Alice"
message = greeting + " " + name
print(message)

# String Length

text = "Hello, world!"
length = len(text)
print(length)

# String indexing and slicing

text = "Hello, world!"
print(text[0])      # Accessing individual character
print(text[7:12])   # Slicing a substring

# String methods

text = "Hello, world!"

print(text.upper())         # Convert to uppercase
print(text.lower())         # Convert to lowercase
print(text.replace("o", "a"))  # Replace characters
print(text.split(", "))     # Split into a list of substrings
print(text.startswith("Hello"))  # Check if string starts with a certain substring
print(text.endswith("world!"))   # Check if string ends with a certain substring

# String formatting using f-strings (Python 3.6+)

name = "Alice"
age = 25
message = f"My name is {name} and I am {age} years old."
print(message)




