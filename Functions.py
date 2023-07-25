# defining functions

# def function_name(parameters):
#     # Function body
#     # Code to be executed
#     # ...

# A simple function without parameters

# def greet():
#     print("Hello, world!")
#
# # Call the function
# greet()  # Output: "Hello, world!"

# A function with parameters

# def add_numbers(a, b):
#     result = a + b
#     return result
#
# # Call the function and store the result in a variable
# sum_result = add_numbers(5, 3)
# print(sum_result)  # Output: 8

# A function with a default parameter

# def say_hello(name="Guest"):
#     print(f"Hello, {name}!")
#
# # Call the function without an argument
# say_hello()  # Output: "Hello, Guest!"
#
# # Call the function with an argument
# say_hello("John")  # Output: "Hello, John!"

# A function with a variable number of arguments (using "*args")

# def add_numbers(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
#
# # Call the function with different numbers of arguments
# print(add_numbers(1, 2, 3))  # Output: 6
# print(add_numbers(10, 20, 30, 40, 50))  # Output: 150

# A function with keyword arguments (using '**kwargs')

# def print_person_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
# # Call the function with keyword arguments
# print_person_info(name="John", age=30, city="New York")

# Functions as First-Class Citizens

# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# def calculator(operation):
#     if operation == "add":
#         return add
#     elif operation == "subtract":
#         return subtract
#
# operation_func = calculator("add")
# result = operation_func(5, 3)
# print(result)  # Output: 8

# Lambda Functions (Anonymous Functions)

# add = lambda a, b: a + b
# result = add(5, 3)
# print(result)  # Output: 8
#
# # Using lambda with map
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = map(lambda x: x**2, numbers)
# print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

# Decorators

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Something is happening before the function is called.")
#         result = func(*args, **kwargs)
#         print("Something is happening after the function is called.")
#         return result
#     return wrapper
#
# @my_decorator
# def say_hello(name):
#     print(f"Hello, {name}!")
#
# say_hello("John")

# Recursion

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)
#
# print(factorial(5))  # Output: 120

# Generator Functions

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibonacci = fibonacci_generator()
for i in range(10):
    print(next(fibonacci))
