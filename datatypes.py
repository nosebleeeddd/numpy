# Data types in numpy
# If you mix data-types , the array
# sticks to one data-type

import numpy as np

# Type casting
a = np.array([[1,2,3],[4,"5",6],[7,8,9]], dtype=np.float32)    # or dtype="<U7"
print(a.dtype)
print(a[0][0].dtype)


# Dynamic Typing
# using this dict in array makes it become an object and remains obj
d = {'1':'A'}
a = np.array([[1,2,3],[4,d,6],[7,8,9]])

print(a.dtype)
# THE ELEMENT INSIDE REMAINS INT OR DICT WHEN PRINTING TYPE
print(type(a[1][1]))
