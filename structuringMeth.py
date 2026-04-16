# Array Structural methods
# Reshape can change shape and
# structure of arrays
# WE CAN TRANSPOSE AS WELL, making
# columns rows and rows columns

import numpy as np

a = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
print(a.shape)

# TRANSPOSEs whole array, make columns rows and rows columns
print(a.transpose())                                # or .T
# SWAP AXES, picks the two axis' to swap
print(a.swapaxes(0,1))


# RESHAPING , you can change how many elements and how many sections
print(a.reshape((5,4)))
print(a.reshape((20,)))                         # [ 1 ... 20] 1 list of 20
print(a.reshape((20, 1)))                       # [1] ... [20] 20 lists
print(a.reshape((2, 10)))                       # two lists [1..10] , [11..20]

# RESHAPE multi-dimensional arrays
print(a.reshape((2, 2, 5)))                     # 2 collections w/ 2 lists,5elem
print(a.reshape((2, 5, 2)))                     # 2 collections 5 lists, 2 elems
print(a.reshape((5, 2, 2)))                     # 5 collection w/ 2lists, 2 elem


# MUST STORE IN VARIABLE TO APPLY CHANGES, a =
a.reshape((10,2))
print(a)

# APPLIES RESHAPE W/o STORING IN VAR
a.resize((10,2))
print(a)


# FLATTEN array to one dimensional(DOESNT CHANGE ORIGINAL)
print(a.flatten())
# RAVEL returns array with flatten view(CHANGES ORIGINAL)
var1 = a.ravel()
var1[2] = 100
print(var1)
print(a)

# FLAT ATTRIBUTE
var = [v for v in a.flat]
print(var)
