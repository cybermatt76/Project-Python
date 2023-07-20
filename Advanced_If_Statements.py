# Checking multiple conditions

age = 25
income = 50000

if age >= 18 and income > 30000:
    print("You are eligible for a loan.")
else:
    print("You are not eligible for a loan.")

# Nested if statements

num = 15

if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
else:
    print("The number is not positive.")

# Using elif for multiple conditions

grade = 85

if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
elif grade >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Checking membership in a list

fruits = ['apple', 'banana', 'orange']

if 'apple' in fruits:
    print("Apple is in the fruit list.")
else:
    print("Apple is not in the fruit list.")

# Using the ternary operator

age = 22

message = "You are eligible." if age >= 18 else "You are not eligible."
print(message)

