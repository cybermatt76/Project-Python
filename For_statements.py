# Iterating over a list

fruits = ['apple', 'banana', 'orange', 'kiwi']

for fruit in fruits:
    print(fruit)

# Iterating over a range of numbers

for num in range(1, 6):
    print(num)

# Iterating over characters in a string

message = "Hello, world!"

for char in message:
    print(char)

# Iterating over key-value pairs in a dictionary

student_grades = {'John': 85, 'Emily': 92, 'James': 78}

for name, grade in student_grades.items():
    print(f"{name}: {grade}")

# Using enumerate() for index-value iteration

fruits = ['apple', 'banana', 'orange']

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
