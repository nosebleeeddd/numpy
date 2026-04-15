# Arrays in Numpy
# Faster and more efficient than python
# lists.
# Stores elements of same data type
# in contiguous memory blocks.

import numpy as np

# Array Manipulation
#a = np.array([1,2,3,4,5])
#print(a)
#print(a[1])
#print(a[1:])
#print(a[:2])
#a[2] = 10
#print(a)


# multi-dimensional arrays
#a_mul = np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(a_mul[0])                                 #[1,2,3]
#print(a_mul[0, 1])                              #2


# Array attributes

a_mul = np.array([[[1,2,3,1],[4,5,6,1],[7,8,9,1]],[[1,1,1,1],[1,1,1,1],[1,1,1,1]]])


# gets how many lists and how many elements
print(a_mul.shape)                              # (2, 3, 4)
# gets how many lists are in a section
print(a_mul.ndim)                               # 3
# number of elements
print(a_mul.size)                               # 24
# gets the datatype(some of numpy is statically typed in C.)
print(a_mul.dtype)                              # int32
