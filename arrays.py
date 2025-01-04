# Importing the array module
import array

# Creating an array of integers
# 'i' represents integer data type
arr = array.array('i', [10, 20, 30, 40])

# Accessing elements using indices
print("First element:", arr[0])  # Output: 10
print("Second element:", arr[1])  # Output: 20

# Adding an element at the end of the array
arr.append(50)  # Append 50
print("Array after appending:", arr)  # Output: array('i', [10, 20, 30, 40, 50])

# Removing an element from the array
arr.remove(30)  # Removes the value 30
print("Array after removal:", arr)  # Output: array('i', [10, 20, 40, 50])

# Iterating through the array
print("Iterating over the array:")
for element in arr:
    print(element)
