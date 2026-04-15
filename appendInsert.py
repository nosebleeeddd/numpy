import numpy as np

a = np.array([1,2,3])

# Appends to the end of previous array
a = np.append(a, [7,8,9])
print(a)

# Insert at a certain position
np.insert(a, 3, [4,5,6])
print(a)

