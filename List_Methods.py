# append(): Adds an element to the end of the list.

fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# extend(): Adds elements from an iterable to the end of the list.

fruits = ['apple', 'banana', 'cherry']
more_fruits = ['orange', 'grape']
fruits.extend(more_fruits)
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange', 'grape']

# insert(): Inserts an element at a specified position in the list

fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, 'orange')
print(fruits)  # Output: ['apple', 'orange', 'banana', 'cherry']

# remove(): Removes the first occurrence of a specified element from the list

fruits = ['apple', 'banana', 'cherry']
fruits.remove('banana')
print(fruits)  # Output: ['apple', 'cherry']

# pop(): Removes and returns the element at the specified index. If no index is provided, it removes and returns the last element

fruits = ['apple', 'banana', 'cherry']
removed_fruit = fruits.pop(1)
print(removed_fruit)  # Output: 'banana'
print(fruits)         # Output: ['apple', 'cherry']

# index(): Returns the index of the first occurrence of a specified element in the list

fruits = ['apple', 'banana', 'cherry']
index = fruits.index('banana')
print(index)  # Output: 1

# count(): Returns the number of occurrences of a specified element in the list

fruits = ['apple', 'banana', 'cherry', 'banana']
count_banana = fruits.count('banana')
print(count_banana)  # Output: 2

# sort(): Sorts the list in ascending order. It can also take an optional reverse argument to sort in descending order

numbers = [5, 2, 8, 1, 3]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 5, 8]

# reverse(): Reverses the elements in the list.

numbers.sort(reverse=True)
print(numbers)  # Output: [8, 5, 3, 2, 1]

# clear(): Removes all elements from the list, making it empty

fruits = ['apple', 'banana', 'cherry']
fruits.clear()
print(fruits)  # Output: []


