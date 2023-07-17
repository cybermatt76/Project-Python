import re

# String formatting using format() method

name = "Alice"
age = 25
message = "My name is {} and I am {} years old.".format(name, age)
print(message)

# String alignment and padding

text = "Hello"
padded_text = text.center(10, "*")
print(padded_text)

# Counting occurrences of a substring

text = "Hello, hello, hello"
count = text.count("hello")
print(count)

# Checking if a string contains only digits

text = "12345"
print(text.isdigit())

text = "12A45"
print(text.isdigit())

# Checking if a string is a valid identifier

text = "my_var"
print(text.isidentifier())

text = "2_var"
print(text.isidentifier())

# String joining

words = ["Hello", "world", "!"]
joined_text = " ".join(words)
print(joined_text)

# String stripping

text = "   Hello, world!   "
print(text.strip())      # Removes leading and trailing spaces

text = "**Hello, world!**"
print(text.strip("*"))   # Removes leading and trailing asterisks

# Regular expressions for advanced string matching and manipulation



text = "Hello, 123 World! 456"
matches = re.findall(r'\d+', text)  # Extract all numeric substrings
print(matches)

new_text = re.sub(r'\d+', 'NUM', text)  # Replace numeric substrings
print(new_text)
