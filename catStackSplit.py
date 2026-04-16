# Concatenation
# Stacking
# Splitting


import numpy as np

#a1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])

#a2 = np.array([[11,12,13,14,15], [16,17,18,19,20]])

# CONCATENATE adds the rows, depending on axis = different results
#a = np.concatenate((a1, a1), axis=0)
#print(a)

#a = np.concatenate((a1, a2)), axis=1)
#print(a)

# STACK, adds a new dimension
#a = np.stack((a1,a2))
#print(a)
# vstack, does concatenation on axis 0
#a = np.vstack((a1,a2))
#print(a)
# hstack, does concatenation on axis 1
#a = np.hstack((a1,a2))
#print(a)


# SPLIT,
#example array for split
a = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])

# splits a into 5 arrays on axis 1
print(np.split(a, 5, axis=1))
