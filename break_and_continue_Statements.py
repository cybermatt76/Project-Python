# Using break to exit a loop

numbers = [1, 3, 5, 7, 9, 11, 13, 15]

for num in numbers:
    if num > 10:
        break
    print(num)


# Using continue to skip an iteration

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num % 2 == 0:
        continue
    print(num)

# Exiting nested loops with "break"

for i in range(5):
    for j in range(3):
        if i == 2 and j == 1:
            break
        print(f"i: {i}, j: {j}")

# Using "continue" in a nested loop

for i in range(3):
    for j in range(3):
        if i == j:
            continue
        print(f"i: {i}, j: {j}")

# Prime numbers using nested loops and a "break" statement

for num in range(2, 20):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, "is a prime number.")

# Skipping even numbers and multiples of 5 using "continue"

for num in range(1, 11):
    if num % 2 == 0 or num % 5 == 0:
        continue
    print(num)

# Printing a pattern using nested loops

rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# FizzBuzz game using if and elif

for num in range(1, 16):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


