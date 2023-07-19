import random

# Counting from 1 to 5

count = 1
while count <= 5:
    print(count)
    count += 1

# Printing even numbers up to a given limit

limit = 10
num = 2
while num <= limit:
    print(num)
    num += 2

# User input validation

# password = input("Enter the password: ")
# while password != "secret":
#     print("Invalid password. Try again.")
#     password = input("Enter the password: ")
# print("Access granted!")

# Summing numbers until a negative number is entered

# total = 0
# number = int(input("Enter a number (or negative number to quit): "))
# while number >= 0:
#     total += number
#     number = int(input("Enter a number (or negative number to quit): "))
# print("Sum:", total)

# Infinite loop with a break statement

# while True:
#     user_input = input("Enter a command: ")
#     if user_input == "quit":
#         break
#     print("Executing command:", user_input)

# Fibonacci sequence

a, b = 0, 1
while a < 100:
    print(a)
    a, b = b, a + b

# Number guessing game

# number = random.randint(1, 100)
# guess = None
# attempts = 0
#
# while guess != number:
#     guess = int(input("Guess the number: "))
#     attempts += 1
#
#     if guess < number:
#         print("Too low!")
#     elif guess > number:
#         print("Too high!")
#     else:
#         print("Congratulations! You guessed the number in", attempts, "attempts.")

# Password attempts limit

# password = "secret"
# attempts = 0
#
# while attempts < 3:
#     input_password = input("Enter the password: ")
#     if input_password == password:
#         print("Access granted!")
#         break
#     else:
#         print("Incorrect password.")
#         attempts += 1
# else:
#     print("Access denied! Maximum attempts reached.")

#  Collatz sequence

number = int(input("Enter a positive integer: "))

while number != 1:
    print(number)
    if number % 2 == 0:
        number //= 2
    else:
        number = (number * 3) + 1

print(number)

