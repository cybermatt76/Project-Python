fruits = ['apple', 'banana', 'orange', 'kiwi']

print(fruits[0])  # Output: 'apple'
print(fruits[2])  # Output: 'orange'

fruits[1] = 'grape'  # Modifying the second element
print(fruits)  # Output: ['apple', 'grape', 'orange', 'kiwi']

fruits.append('melon')  # Adding a new element at the end
print(fruits)  # Output: ['apple', 'grape', 'orange', 'kiwi', 'melon']

fruits.insert(2, 'cherry')  # Adding an element at a specific index
print(fruits)  # Output: ['apple', 'grape', 'cherry', 'orange', 'kiwi', 'melon']

fruits.remove('orange')  # Removing a specific element
print(fruits)  # Output: ['apple', 'grape', 'cherry', 'kiwi', 'melon']

popped_fruit = fruits.pop()  # Removing and returning the last element
print(popped_fruit)  # Output: 'melon'
print(fruits)  # Output: ['apple', 'grape', 'cherry', 'kiwi']

print(len(fruits))  # Output: 4 (number of elements in the list)

for fruit in fruits:
    print(fruit)

print(fruits[1:3])  # Output: ['grape', 'cherry'] (elements at index 1 and 2)
print(fruits[:2])  # Output: ['apple', 'grape'] (elements up to index 2)
print(fruits[2:])  # Output: ['cherry', 'kiwi'] (elements from index 2 onwards)
