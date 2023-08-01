# Deleting a variable or object reference

variable_name = 10
del variable_name

# Deleting an element from a list

numbers = [1, 2, 3, 4, 5]
del numbers[2]  # Remove the element at index 2
print(numbers)  # Output: [1, 2, 4, 5]

# Deleting a slice from a list

numbers = [1, 2, 3, 4, 5]
del numbers[1:4]  # Remove elements from index 1 to 3 (exclusive)
print(numbers)   # Output: [1, 5]

# Deleting a dictionary key

person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
del person['age']  # Remove the 'age' key from the dictionary
print(person)      # Output: {'name': 'Alice', 'city': 'New York'}

# Deleting an element from a collection (e.g., set)

fruits = {'apple', 'banana', 'cherry'}
fruits.discard('banana')  # Remove 'banana' from the set using discard()
print(fruits)            # Output: {'cherry', 'apple'}

# tuple

fruits_tuple = ('apple', 'banana', 'cherry')
print(fruits_tuple)  # Output: ('apple', 'banana', 'cherry')

# sequence

numbers_list = [1, 2, 3, 4, 5]
print(numbers_list)       # Output: [1, 2, 3, 4, 5]
print(numbers_list[2])    # Output: 3 (accessing element at index 2)
print(numbers_list[1:4])  # Output: [2, 3, 4] (slicing)

