# Lists as Stacks

stack = []  # Initialize an empty list as a stack

stack.append(1)  # Push 1 onto the stack
stack.append(2)  # Push 2 onto the stack
stack.append(3)  # Push 3 onto the stack

print(stack)  # Output: [1, 2, 3]

stack = [1, 2, 3]

top_element = stack.pop()  # Pop the last element from the stack
print(top_element)  # Output: 3
print(stack)        # Output: [1, 2]

#Lists as Queues

queue = []  # Initialize an empty list as a queue

queue.append(1)  # Enqueue 1 into the queue
queue.append(2)  # Enqueue 2 into the queue
queue.append(3)  # Enqueue 3 into the queue

print(queue)  # Output: [1, 2, 3]

queue = []  # Initialize an empty list as a queue

queue.append(1)  # Enqueue 1 into the queue
queue.append(2)  # Enqueue 2 into the queue
queue.append(3)  # Enqueue 3 into the queue

print(queue)  # Output: [1, 2, 3]

from collections import deque

queue = deque()  # Initialize an empty deque as a queue

queue.append(1)  # Enqueue 1 into the queue
queue.append(2)  # Enqueue 2 into the queue
queue.append(3)  # Enqueue 3 into the queue

front_element = queue.popleft()  # Dequeue the first element from the queue
print(front_element)  # Output: 1
print(queue)          # Output: deque([2, 3])

# List Comprehensions

# Squaring numbers from 1 to 5 using a list comprehension

squares = [x ** 2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

# Creating a new list with only the even numbers from an existing list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Combining elements from two lists using a list comprehension.

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 22]
people = [{'name': name, 'age': age} for name, age in zip(names, ages)]
print(people)
# Output: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 22}]

# Flattening a list of lists using a nested list comprehension

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [element for row in matrix for element in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


