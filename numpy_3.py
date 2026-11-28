import numpy as np

# Create the two NumPy arrays
a = np.array([12, 24, 36])
b = np.array([3, 6, 9])

# 1. Addition
addition = a + b  # or np.add(a, b)

# 2. Subtraction
subtraction = a - b  # or np.subtract(a, b)

# 3. Multiplication
multiplication = a * b  # or np.multiply(a, b)

# 4. Division
division = a / b  # or np.divide(a, b)

# Display the results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

#2
import numpy as np

# Create the NumPy array
numbers = np.array([11, 22, 33, 44, 55])

# Display the data type of the array's elements
print("Data type of elements:", numbers.dtype)

# Optional: Display the Python object type of the variable itself
print("Object type:", type(numbers))

#3
import numpy as np

# Method 1: Create directly using a nested list (2D array)
arr = np.array([
    [3, 6, 9],
    [12, 15, 18],
    [21, 24, 27]
])

# Display the 2D array
print(arr)

#4
import numpy as np

scores = np.array([55, 82, 74, 91, 68, 47])

# 1. Average of the scores
average_score = np.mean(scores)

# 2. Index of the lowest score
lowest_score_index = np.argmin(scores)

# 3. Highest score
highest_score = np.max(scores)

print("Average score:", average_score)
print("Index of lowest score:", lowest_score_index)
print("Highest score:", highest_score)

#5
import numpy as np

arr = np.array([5, 15, 25, 35, 45, 55])

# 1. Elements greater than 25
print("Elements greater than 25:", arr[arr > 25])

# 2. Elements less than 25
print("Elements less than 25:", arr[arr < 25])

# 3. Elements equal to 25
print("Elements equal to 25:", arr[arr == 25])

#6
import numpy as np

arr = np.array([
    [3, 6, 9],
    [12, 15, 18],
    [21, 24, 27]
])

# 1. Sum of all elements
total_sum = np.sum(arr)

# 2. Sum of each column (moving down across rows -> axis=0)
col_sum = np.sum(arr, axis=0)

# 3. Sum of each row (moving across columns -> axis=1)
row_sum = np.sum(arr, axis=1)

print("Sum of all elements:", total_sum)
print("Sum of each column (axis=0):", col_sum)
print("Sum of each row (axis=1):", row_sum)

#7
import numpy as np

arr = np.array([5, 15, 25, 35, 45, 55, 65, 75])

# 1. Elements from index 3 to the end
print("From index 3 to the end:", arr[3:])

# 2. Elements from the beginning up to index 6 (stop index is exclusive, so use 7)
print("From beginning up to index 6:", arr[:7])

# 3. Elements from index 2 to index 7 (stop index is exclusive, so use 8)
print("From index 2 to index 7:", arr[2:8])

#8
import numpy as np

arr = np.array([12, 24, 36, 48, 60, 72, 84, 96])

# 1. The last 2 elements
print("Last 2 elements:", arr[-2:])

# 2. All elements except the last 4 elements
print("All except last 4:", arr[:-4])

# 3. Elements from the 7th-last position (-7) up to the 3rd-last position (-3 -> stop at -2)
print("7th-last up to 3rd-last:", arr[-7:-2])

#9
import numpy as np

arr = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18])

# 1. Every third element starting from the first element (index 0, step 3)
print("Every third from first element:", arr[0::3])

# 2. Every third element starting from the second element (index 1, step 3)
print("Every third from second element:", arr[1::3])

# 3. Reverse the complete array (step -1)
print("Reversed array:", arr[::-1])

#10
import numpy as np

arr = np.array([22, 11, 44, 33, 66, 55, 77])

# 1. Find the minimum value
min_val = np.min(arr)

# 2. Find the index of the maximum value
max_idx = np.argmax(arr)

# 3. Display values less than 50
less_than_50 = arr[arr < 50]

# 4. Display the last 2 elements using negative indexing
last_2 = arr[-2:]

print("Minimum value:", min_val)
print("Index of maximum value:", max_idx)
print("Values less than 50:", less_than_50)
print("Last 2 elements:", last_2)

#11
import numpy as np

# Create the two NumPy arrays
a = np.array([15, 25, 35, 45])
b = np.array([5, 5, 5, 5])

# 1. Addition
addition = a + b

# 2. Subtraction
subtraction = a - b

# 3. Multiplication
multiplication = a * b

# 4. Division
division = a / b

# Display the results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

#12
import numpy as np

# Create the NumPy array
values = np.array([7, 14, 21, 28, 35, 42])

# 1. Display the data type of elements in values
print("Data type:", values.dtype)

# 2. Display the number of dimensions of values
print("Number of dimensions:", values.ndim)

#13
import numpy as np

# Method 1: Create directly using a nested list (2D array)
arr = np.array([
    [4, 8, 12],
    [16, 20, 24],
    [28, 32, 36]
])

# Display the 2D array
print(arr)

#14
import numpy as np

values = np.array([18, 32, 47, 29, 64, 51])

# 1. Total sum of the elements
total_sum = np.sum(values)

# 2. Position (index) of the smallest element
smallest_index = np.argmin(values)

# 3. Largest element
largest_element = np.max(values)

print("Total sum:", total_sum)
print("Index of smallest element:", smallest_index)
print("Largest element:", largest_element)

#15
import numpy as np

arr = np.array([9, 18, 27, 36, 45, 54])

# 1. Elements greater than 35
print("Elements greater than 35:", arr[arr > 35])

# 2. Elements less than 35
print("Elements less than 35:", arr[arr < 35])

# 3. Elements equal to 36
print("Elements equal to 36:", arr[arr == 36])

#16
import numpy as np

arr = np.array([
    [4, 8, 12],
    [16, 20, 24],
    [28, 32, 36]
])

# 1. Total sum of all elements
total_sum = np.sum(arr)

# 2. Sum of each column using axis=0
col_sum = np.sum(arr, axis=0)

# 3. Sum of each row using axis=1
row_sum = np.sum(arr, axis=1)

print("Total sum of all elements:", total_sum)
print("Sum of each column (axis=0):", col_sum)
print("Sum of each row (axis=1):", row_sum)

#17
import numpy as np

arr = np.array([9, 18, 27, 36, 45, 54, 63, 72])

# 1. Elements from index 1 to the end
print("From index 1 to the end:", arr[1:])

# 2. Elements from the beginning up to index 3 (stop index is exclusive, so use 4)
print("From beginning up to index 3:", arr[:4])

# 3. Elements from index 3 to index 7 (stop index is exclusive, so use 8)
print("From index 3 to index 7:", arr[3:8])

#18
import numpy as np

arr = np.array([13, 26, 39, 52, 65, 78, 91, 104])

# 1. The last 5 elements
print("Last 5 elements:", arr[-5:])

# 2. All elements except the last element
print("All except last element:", arr[:-1])

# 3. Elements from the 6th-last position (-6) up to the 3rd-last position (-3 -> stop at -2)
print("6th-last up to 3rd-last:", arr[-6:-2])

#19
import numpy as np

arr = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50, 55])

# 1. Every second element starting from index 2
print("Every second element from index 2:", arr[2::2])

# 2. Every third element starting from index 0
print("Every third element from index 0:", arr[0::3])

# 3. Reverse order with a step of 2
print("Reverse order with step 2:", arr[::-2])

#20
import numpy as np

arr = np.array([21, 42, 63, 84, 105, 126, 147])

# 1. Sum of all elements
total_sum = np.sum(arr)

# 2. Index of the largest element
largest_index = np.argmax(arr)

# 3. Elements greater than 70
greater_than_70 = arr[arr > 70]

# 4. First 3 elements using positive slicing
first_three = arr[:3]

# 5. Every second element using slicing
every_second = arr[::2]

print("Sum of all elements:", total_sum)
print("Index of largest element:", largest_index)
print("Elements greater than 70:", greater_than_70)
print("First 3 elements:", first_three)
print("Every second element:", every_second)
