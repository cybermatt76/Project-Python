# Checking if a number is positive or negative

number = -5

if number > 0:
    print("The number is positive.")
else:
    print("The number is negative.")

# Checking if a number is even or odd

number = 7

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Checking if a person is eligible to vote

age = 19

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

# Checking if a password meets the required criteria

password = "pass123"

if len(password) >= 8 and password.isalnum():
    print("Valid password.")
else:
    print("Invalid password.")

# Checking if a string is empty

text = ""

if not text:
    print("The string is empty.")
else:
    print("The string is not empty.")
