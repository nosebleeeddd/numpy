# List Vs Array Math

import numpy as np

#List
l1 = [1,2,3,4,5]
l2 = [6,7,8,9,0]

# Type cast to array
a1 = np.array(l1)
a2 = np.array(l2)

# PYTHON repeats list when using math operations
print(l1 * 5)
print(l1 + l2)
# ARRAY does the math operation
print(a1 * 5)
print(a1 + 10)

# SQUARE
a = np.array([[1,2,3],[4,5,6]])

print(np.sqrt(a))
