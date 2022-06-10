# Calculations done in NumPy arrays are much faster than in Python lists.
import time
import numpy as np

# py_list = list(range(20000000))
# start = time.time()
# py_list = [i+2 for i in py_list]  # adding 2 to each element in the list
# end = time.time()
# print(end-start)  # time taken to perform the list comprehension
#
# py_arr = np.arange(20000000)
# start = time.time()
# py_arr = py_arr + 2  # adding 2 to each element in the array
# end = time.time()
# print(end-start)  # time taken to perform addition with numpy arrays
