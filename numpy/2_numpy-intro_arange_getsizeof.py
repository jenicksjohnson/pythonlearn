# NumPy, Pandas, SciPy are libraries used for data exploration and analysis.
# NumPy provides linea algebra and statistical computing functions, mainly numerical operations.

# Why use NumPy and SciPy?
# To perform basic scientific/statistical operations like:
# > Arrays, matrices, statistics, integration, differential equation solver etc.
# > Python can only perform some basic mathematical operations, so, we use these libraries.

# NumPy stands for "Numerical Python".
# Data stores in NumPy as 'ndarray' objects.

# List vs Array:
# > Both lists and arrays are mutable and indexable.
# > Both supports slicing operations.
# > List can contain elements of different data types; all elements in an array are the same data type.
# > Arrays need less memory than lists.
# > Operation performed on arrays are faster than lists.
# > Operations like +, * etc can be performed directly on arrays; not possible in lists.
# > NumPy is a package that must be installed in the current project
#   - Settings > Project > Python Interpreter > install "numpy"

import numpy as np
import sys

s = range(100)
s_lst = list(range(100))
print(s)
print(len(s))
print(sys.getsizeof(s))  # return size of object 's' in bytes
print(sys.getsizeof(s)*len(s))  # size of 100 's' objects
print(sys.getsizeof(s_lst))


A = np.arange(100)
print(A)
print(A.size)
print(A.itemsize)
print(A.itemsize * A.size)  # size of 100 elements in the array
print()

# my_lst = []
# my_arr = np.array(my_lst)
# print(sys.getsizeof(my_lst), sys.getsizeof(my_arr))
#
# my_lst = [1, 2, 3]
# my_arr = np.array(my_lst)
# print(sys.getsizeof(my_lst), sys.getsizeof(my_arr))
#
# my_lst = [1, 2, 3, 4, 5, 6]
# my_arr = np.array(my_lst)
# print(sys.getsizeof(my_lst), sys.getsizeof(my_arr))
# print()
#
# my_lst = []
# my_arr = np.array([])
# print(sys.getsizeof(my_lst), sys.getsizeof(my_arr))
#
# my_lst = [1]
# my_arr = np.array([1])
# print(sys.getsizeof(my_lst), sys.getsizeof(my_arr))
#
# my_lst = [1, 2]
# my_arr = np.array([1, 2])
# print(sys.getsizeof(my_lst), sys.getsizeof(my_arr))
#
# my_lst = [1, 2, 3]
# my_arr = np.array([1, 2, 3])
# print(sys.getsizeof(my_lst), sys.getsizeof(my_arr))
#
# my_lst = [1, 2, 3, 4]
# my_arr = np.array([1, 2, 3, 4])
# print(sys.getsizeof(my_lst), sys.getsizeof(my_arr))
#
# my_lst = [1, 2, 3, 4, 5]
# my_arr = np.array([1, 2, 3, 4, 5])
# print(sys.getsizeof(my_lst), sys.getsizeof(my_arr))
#
# my_lst = [1, 2, 3, 4, 5, 6]
# my_arr = np.array([1, 2, 3, 4, 5, 6])
# print(sys.getsizeof(my_lst), sys.getsizeof(my_arr))

