# EXPORTING AND IMPORTING
# NUMPY ARRAYS

import numpy as np

a = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[18,19,20,21,22,23]])


# export/save a numpy file
np.save("myarray.npy", a)

# load a numpy file
a = np.load("myarray.npy")
print(a)

# save CSV file, delimiter because its comma seperated
np.savetxt("myarray.csv", a, delimiter=",")

# loads the csv data
a = np.loadtxt("myarray.csv", delimiter=",")
print(a)
