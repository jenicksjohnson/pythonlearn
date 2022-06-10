# numpy,pandas,scipy are libraries used for data exploration and analysis.
# numpy provides linear algebra and statistical computing functions,mainly for numerical operations.
# Why Numpy&Scipy ->To perform basic scientific/statistical operations like:
#          -arrays,matrices,statistics,integration , diff.eqn solver etc
#          -but python can perform only some basic mathematical operations.
#          -so we use these libraries.

# Numpy stands for 'Numerical Python'
# Data stores in numpy as 'ndarray' objects.
##########################################################
#LIST vs ARRAY
# Internally it contains lists.
# array is same like list to store data.
# both are mutable,indexed
# both can be sliced/ slicing operation.


# import numpy as np
# import sys
# s=range(100)
# print(s)
# print(len(s))
# print(sys.getsizeof(s))  ##we get the bytes to store the object
# print(sys.getsizeof(s)*len(s))
##################################################
###########################attributes
# import numpy as np
# narray=np.array([12,45,78])    ##creating an array
# print(narray)               ##this is one dimenstional array
#
# import numpy as np
# narray=np.array([12,45,78])   # creating an array
# print(narray)
# print(type(narray))     # checking type of a variable
# print(narray.ndim)      #  to get the dimension of array
# print(narray.dtype)     # type of array/data stored in the array eg: float64  =>64bits =>64/8=>8bytes.
# print(narray.shape)     #  how many elements present in each dimension (columns,) or (rows,columns)
# print(narray.size)      #  total number of elements
# print(narray.data)      # memory address
# print(narray.itemsize)  # how many bytes required to store each data. 1byte=8bit.
########################################################

# import numpy as np
# narray=np.array([[10,20,30],[40,50,60]])
# print(narray)
# print(narray.ndim)
# print(narray.shape)
# print(narray.size)
# print(type(narray.shape))
# print(narray.shape[1])
# narray1=np.array([12,45,78],dtype='int64')
# ## change the data type as stored
# print(narray1.dtype)

########################################################
# import numpy as np
# arr = np.array(['apple', 'banana', 'cherry'])
# print(arr)
# print(arr.dtype)

########################################################
# array() creation
####1.
# import numpy as np
# a=np.array([1,2,3])
# print(a)
####2.
# import numpy as np
# a=np.array((1,2,3))
# print(a)
# print(a.ndim)
# print(a.dtype)
##############################################################
# import numpy as np
# narray=np.array([12,45,64],dtype='int64')
# print(narray.dtype)
# a=np.array([1.0,2.4,3.6])
# print(a)
# print(a.dtype)
# b=np.array([1,2,3,4.5])
# print(b)
# print(b.dtype)
#######################################################
# 3d
###################################
# import numpy as np
#
# a=np.array([[1,2],[3,4],[5,6]])
# print(a)
# print(a.ndim)
# print(a.shape)
#
# b=np.array([[[23,45,12],[12,46,85]],[[12,13,45],[79,86,45]]])
# print(b)
# print(b.ndim)
# print(b.shape)
#############################################################
#  by using arange
# import numpy as np
# a=np.arange(2,10)
# print(a)
# b=np.arange(6.0)
# print(b)
# b=np.arange(2,10,2)
# print(b)
# #
# z=np.arange(10,dtype='complex')
# print(z)
###################################
# setting zeros
# import numpy as np
#
# s=np.zeros(5)
# print(s)
# s=np.zeros((3,4))
# print(s)

########################################
# ##by default one in arrays
# import numpy as np
# r=np.ones(4)
# print(r)
# r=np.ones(4,dtype='int')
# print(r)
# r=np.ones((4))
# print(r)
# # # # # ##
# r=np.ones((4,4,2)) #4 matrx of 4x2
# print(r)
# print(r.ndim)

############################################
# ##if we use linspace it consider the end point
# import numpy as np
# a=np.linspace(2,10) # start and end points.
# print(a)  # we get default 50 points.
# # # #
# b=np.linspace(1,10,4)
# print(b)
# # # # # exclude last point.
# b=np.linspace(2,10,4,endpoint=False)
# print(b)

################################################
# ##eye:- gives an array filled with zero expect k-th diagonal to 1
# import numpy as np
# a=np.eye(3) # n=m by default (rows & columns)
# print(a)
# # # # # define where we want 1s.
# a=np.eye(3,k=2)
# print(a)
# # #
# a=np.eye(3,k=-2)
# print(a)
# # #
# a=np.eye(3,2)
# print(a)
# # # ## same to eye() we have identity fn. for sqr matrix
# a=np.identity(5)
# print(a)
###############################################
# ### random()-for creating random number array
# # functions in random module
# # -rand()
# # -randn()
# # randint()
import numpy as np
# a=np.random.rand(5) # uniformly distrbtd 5 random numbers
# print(a)
# # # # # # #
# a=np.random.rand(5,2) # uniformly distrbtd random numbers
# print(a)
# # # # # # #
# b=np.random.randn(4) # normal distrbtd random numbers
# print(b)
# b=np.random.randn(4,2) # normal distrbtd random numbers
# print(b)
# # # # # #
# c=np.random.randint(2,6) # gives a random num bw 2 and 4
# print(c)
# # print(type(c))
# # # # # # #
# c=np.random.randint(100,size=4)  # 4 random numbers
# print(c)
# # # # # # #
# c=np.random.randint(100,size=(2,3))
# print(c)
######################################################
#######################################################
##datatypes
## numerical data types
# Boolean,Integer,unsigned integer,float,complex

# bool           true,false
# int8           Byte (-128 to 127)
# int16          Integer (-32768 to 32767)
# int32          Integer (-2147483648 to 2147483647)
# int64          Integer (-9223372036854775808 to 9223372036854775807)
# uint8          Unsigned integer (0 to 255)
# uint16         Unsigned integer (0 to 65535)
# uint32         Unsigned integer (0 to 4294967295)
# uint64         Unsigned integer (0 to 18446744073709551615)
# intp           Integer used for indexing, typically the same as ssize_t
# float32        float
# float64
# complex64         Complex number, represented by two 32-bit floats (real and imaginary components)
# complex128
#
# i - integer
# f - float
# ? - bool
# U - unicode
#######################
#########################
# import numpy as np
# a=np.array([True,False,True])
# print(a)
# print(a.dtype)
# ###############################
# a=np.array([1+2j,2+4j,3+5j])
# print(a)
# print(a.dtype)
# ##############################
# a=np.array(["apple",'orange','cherry'])
# print(a)
# print(a.dtype)
# ##############################
# a=np.array([8,2,3])
# print(a)
# print(a.dtype)
# ##############################
# a=np.array([2147483647,25435545,3])
# print(a)
# print(a.dtype)
# ##############################
# a=np.array([-2147483648,25435545,3])
# print(a)
# print(a.dtype)
# ##############################
# a=np.array([8,2,3],dtype='f')
# print(a)
# print(a.dtype)
# #############################
##################################
import numpy as np
# a=np.array([8,0,-3],dtype='bool')
# print(a)
# print(a.dtype)
# ###############################
# a=np.array([-4,2,3,128,-128],dtype='uint8')
# print(a)
# print(a.dtype)
#####################################
# a=np.array([258,2,3],dtype='int8')
# print(a)
# print(a.dtype)
####################################
# a=np.array([128,2,3],dtype='int8')
# print(a)
# print(a.dtype)
####################################
# a=np.array([256,1,2],dtype='int8')
# print(a)
# print(a.dtype)
######################################
# indexing of arrays
# creating a scalar array
# import numpy as np
# a=np.array(5)
# print(a)
# print(type(a))
# print(a.ndim)
####################################
# #positioning
# a=np.array([1,2,3,4,5])
# print(a)
# ###
# print(a[0])  #0th elemnt
# print(a[3])
# print(a[-1])
#####################################
# b=np.array([[1,2],[3,4]])
# print(b)
# # #
# print(b[0][0]) # row and column
# print(b[0][1])
# print(b[1][1])
# print(b[-1][0])
# print(b[-1][-1])
# print(b[-2][-2])
# print(b[-2][-1])
# #############################
# c=[[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]]
# d=np.array(c)
# print(d)
# print(d.ndim)
# print(d[0][1][1]) # matrix,row,column
# print(d[1][0][0])
# print(d[1][2][3])
# ################################
# print(d[-2][-3][-4])
# print(d[-1][-3][-4])
# print(d[0])
# print(d[0][1])
# # ###assign values
# a=np.array([1,2,3,4,5])
# print(a)
# a[3]=100
# print(a)
# # # # #
# b=np.array([[1,2],[3,4]])
# print(b)
# b[0][1]=111
# print(b)
# d[0][1][1]=100
# print(d)
########################################
#######################################
# import numpy as np
# a=np.array([8,2,5,9,11,6])
# print(a)
# print(a[:])
# print(a[2:5])
# print(a[:4])
# print(a[:6:2])
# # printing backwards
# print(a[::-1])
#####################################
# in 2d array (x[srt:end:step,strt:end:step])
##1D array
# import numpy as np
# a=np.array([8,2,5,9,11,6])
# # # # #x[srt:end:stp]
# print(a)
# print(a[:])
# print(a[2:])
# print(a[2:5])
# print(a[:4])
# print(a[0:6:2])
# # # # print(a[-1])
# print(a[::-1])
#
# ##2D array=    x[srt:end:stp , srt:end:stp]
# import numpy as np
# x=np.array([[1,2],[3,4],[5,6]])
# print(x)
# # #
# print(x[1:,1:])   # row from 1 onwards,clm from 1 onwards
# # #
# print(x[1,:])
# y=np.array([[1,2,3,4],[5,6,7,8],[20,30,40,50]])
# print(y)
# print(y[1:,1:])
# # print(y[1,1])
# # # #
# print(y[::,::2])
# print(y[:,::2])
#
# #
# # ##3D array==> z[srt:end:stp,srt:end:stp,srt:end:stp] ie(matx,rows,clms)
# #
# z=[[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]]
# d=np.array(z)
# print(d)
# print(d[:,:,:1]) # all matrix ,all rows, 0th colm ie 0th colm of all matrx
# print(d[:,1:,::2])

##################################################################################
import numpy as np
## ####operations
# #scalar additions
# a=np.array([10,20,30,40,50])
# print(a)
# print(a+10)
# print(a[0]+10)
# # # # scalar multiplication
# a=np.array([10,20,30,40])
# print(a)
# print(a*5)
# # # #scalar exponent
# a=np.array([10,20,30,40])
# print(a)
# print(a**2)
# # # # # #scalar substraction
# a=np.array([10,20,30,40])
# print(a)
# print(a-5)
# # # # #operation b/w array are also element wise
# a=np.array([10,20,30,40,50])
# b=np.ones(5)+1
# print(a)
# print(b)
# print(a-b)
# print(a+b)
# # # # # #
# a1=np.array([[1,2],[3,4]])
# a2=np.array([[5,6],[7,8]])
# print(a1)
# print(a2)
# print(a1+a2)
# print("mul",a1*a2)  ##element wise multiplication
# matrix multi
# print("matrix mul",a1.dot(a2))
#
# # # # # # # #
# ##element wise comparison
# a=np.array([1,2,3,4,5])
# b=np.array([5,4,3,2,1])
# print(a==b)
# print(a>b)
# ##array wise comparison
# a=np.array([1,2,3,4,5])
# b=np.array([5,4,3,2,1])
# c=np.array([1,2,3,4,5])
# print(np.array_equal(a,b))
# print(np.array_equal(a,c))
#
#
# # # #transcendantal function(a function of not expressible as finite)
# a=np.arange(1,5)
# print(a)
# print(np.sin(a))
# print(np.log(a))
# print(np.exp(a))
# print(np.sqrt(a))
#
#
# # # # # # shape mismatch
# a=np.arange(5)
# b=np.arange(2)
# print(a)
# print(b)
# print(a.shape)
# print(b.shape)
# print(a+b)
#
# #it will add b to both rows of a1
# a1=np.array([[1,2],[3,4]])
# print("a1",a1)
# print(a1+b)
#
# # # # # # ##basic reductions
arr=np.array([10,20,90,100,70])
# print(arr.sum())
# print(np.sum(arr))
# print(arr.max())
# print(np.max(arr))
# print(arr.min())
# print(np.min(arr))
# print(np.average(arr))
#####################
# # # # #
# print(arr.argmin())  # #indeex of min element
# print(arr.argmax())   # #index of max element
# # # # # #
# x=np.array([[1,1],[2,2]])
# print(x)
# print(x.sum())
# print(x.sum(axis=0)) ##column wise addition  #######important
# print(x.sum(axis=1)) ##row wise addition
# # # # #
#########################################
# ## # #statistics
# x=np.array([1,2,3,1])
# x=np.array([[1,2,3],[5,6,7]])
# print(x.mean())
# print(np.mean(x))
# print(np.median(x))  #CENter value/middile value
# print(x.std())      ##standart deviation
# print(x.mean(axis=0)) #column wise
# # # # # # # #
#
#







