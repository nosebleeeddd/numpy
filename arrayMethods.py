# Methods to append, insert
# delete row/col from
# Array.


import numpy as np

a = np.array([1,2,3])

# Appends to the end of previous array
a = np.append(a, [7,8,9])
print(a)

# Insert at a certain position
a = np.insert(a, 3, [4,5,6])
print(a)

# Delete element by index from an array
a = np.array([[1,2,3], [4,5,6]])
print(np.delete(a, 1))
print(np.delete(a, 2))
print(np.delete(a, 3))

# Delete by axis, deletes a row from the array
a = np.array([[1,2,3], [4,5,6]])
print(np.delete(a, 1, 0))

# Delete the index column
a = np.array([[1,2,3], [4,5,6]])
print(np.delete(a, 1, 1))
