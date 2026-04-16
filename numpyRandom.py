# Random in numpy

import numpy as np

number = np.random.randint(100)
print(number)

# Dimension shape with random values
numbers = np.random.randint(100, size=(2,3,4))
print(numbers)

# Dimension shape with a range of random values
numbers1 = np.random.randint(40, 50, size=(2,3,4))
print(numbers1)

# CHOICE ,range of random numbers
numbers = np.random.choice([10,20,30,40,50], size=(5,10))
print(numbers)

# RANDOM BINOMIALS, 10 tries, 50% probability, 5 list of 10
numbers2 = np.random.binomial(10, p=0.5, size=(5,10))
print(numbers2)

# NORMAL, mean is 170cm, std is 15cm, 10 lists of 5
numbers3 = np.random.normal(loc=170, scale=15, size=(5,10))
print(numbers)
