lambda arguments: expression

square = lambda x: x ** 2
print(square(5))  # Output: 25

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]

students = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 22}, {'name': 'Carol', 'age': 28}]
students_sorted_by_age = sorted(students, key=lambda x: x['age'])
print(students_sorted_by_age)
# Output: [{'name': 'Bob', 'age': 22}, {'name': 'Alice', 'age': 25}, {'name': 'Carol', 'age': 28}]

is_even = lambda x: True if x % 2 == 0 else False
print(is_even(4))  # Output: True

from functools import partial

power = lambda x, y: x ** y
cube = partial(power, y=3)
print(cube(2))  # Output: 8

from itertools import groupby

words = ['apple', 'banana', 'cherry', 'avocado', 'blueberry']
grouped_by_first_letter = groupby(words, key=lambda x: x[0])
for key, group in grouped_by_first_letter:
    print(key, list(group))
# Output:
# a ['apple', 'avocado']
# b ['banana', 'blueberry']
# c ['cherry']

capitalized_words = map(lambda x: x.upper(), words)
print(list(capitalized_words))
# Output: ['APPLE', 'BANANA', 'CHERRY', 'AVOCADO', 'BLUEBERRY']

factorial = (lambda f: lambda x: 1 if x == 0 else x * f(f)(x - 1))(lambda f: lambda x: 1 if x == 0 else x * f(f)(x - 1))
print(factorial(5))  # Output: 120
