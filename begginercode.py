# Print Hello Python
print("Hello Python")

# this is the first comment
spam = 1  # and this is the second comment
# ... and now a third!
text = "# This is not a comment because it's inside quotes."

print('"Isn\'t," they said.')

s = 'First line.\nSecond line.'  # \n means newline
print(s)  # with print(), \n produces a new line

print('C:\some\name')  # here \n means newline!

print(r'C:\some\name')  # note the r before the quote

#Printing variables
name = "Alice"
age = 25
print("My name is", name, "and I am", age, "years old.")

# Formatting output using f-strings
name = "Bob"
age = 30
print(f"My name is {name} and I am {age} years old.")

# Printing the result of an expression

x = 5
y = 3
print("The sum of", x, "and", y, "is", x + y)

# printing multiple lines

print("Line 1")
print("Line 2")
print("Line 3")

# Printing formatting options

pi = 3.14159
print("The value of pi is approximately {:.2f}".format(pi))

# Printing with separators and end parameter:
print("Hello", "world", sep=", ", end="!")
print("Welcome", "to", "Python")

