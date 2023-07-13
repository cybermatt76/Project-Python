import math
import random
import numpy as np

result = 5 + 3
print(result)

result = 10 - 4
print(result)

result = 7 * 2
print(result)

result = 15 / 3
print(result)

# Note: In Python 3, division of two integers returns a float.
# If you want integer division, you can use the // operator.

result = 2 ** 4
print(result)


# Modulo (remainder) calculation:

result = 17 % 5
print(result)

# Order of operations (parentheses)

result = (4 + 5) * 2
print(result)

# Using variables:

x = 6
y = 3
result = x * y + 2
print(result)

# Using the math module for advanced mathematical functions:



# Square root
result = math.sqrt(16)
print(result)

# Trigonometric functions
angle = math.pi / 4
result = math.sin(angle)
print(result)

# Logarithm
result = math.log10(100)
print(result)

# Factorial
result = math.factorial(5)
print(result)

# Random float between 0 and 1
result = random.random()
print(result)

# Random integer within a range
result = random.randint(1, 10)
print(result)

# Random choice from a sequence
fruits = ["apple", "banana", "orange"]
result = random.choice(fruits)
print(result)

# Array creation and operations
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = arr1 + arr2
print(result)

# Matrix multiplication
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

result = np.matmul(matrix1, matrix2)
print(result)

# Statistical operations
data = np.array([1, 2, 3, 4, 5])
mean = np.mean(data)
std_dev = np.std(data)

print(mean)
print(std_dev)
