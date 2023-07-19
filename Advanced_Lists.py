# Extending a list

fruits = ['apple', 'banana', 'orange']
additional_fruits = ['kiwi', 'grape']
fruits.extend(additional_fruits)
print(fruits)  # Output: ['apple', 'banana', 'orange', 'kiwi', 'grape']

# Concatenating lists

list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
print(concatenated_list)  # Output: [1, 2, 3, 4, 5, 6]

# Reversing list

numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # Output: [5, 4, 3, 2, 1]

# Sorting a list

numbers = [4, 2, 1, 3, 5]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4, 5]

# Counting occurrences of an element

numbers = [1, 2, 2, 3, 3, 3, 4, 5]
count = numbers.count(3)
print(count)  # Output: 3

# Finding the index of an element

fruits = ['apple', 'banana', 'orange', 'kiwi']
index = fruits.index('orange')
print(index)  # Output: 2

# Removing all elements from a list

numbers = [1, 2, 3, 4, 5]
numbers.clear()
print(numbers)  # Output: []

# Checking if an element exists in a list

fruits = ['apple', 'banana', 'orange', 'kiwi']
exists = 'apple' in fruits
print(exists)  # Output: True

exists = 'grape' in fruits
print(exists)  # Output: False

# List comprehension (creating a new list based on an existing list)

numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]



